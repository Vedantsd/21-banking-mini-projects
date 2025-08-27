from flask import Flask, render_template, request
from datetime import date, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib   
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64



app = Flask(__name__)

# ------------------ Data ------------------
def get_stock_data(ticker_symbol):
    curr_date = date.today()
    prev_date = curr_date - timedelta(days=365)
    stock_data = yf.download(ticker_symbol, start=prev_date, end=curr_date)
    return stock_data

def prepare_features(stock_data):
    df = pd.DataFrame(stock_data)
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['Return'] = df['Close'].pct_change()
    df = df.dropna()

    X = df[['Close', 'MA5', 'MA10', 'Return']].values[:-1]
    y = df['Close'].values[1:]
    return X, y, df

# ------------------ Prediction ------------------
def predict_stock_value(stock_data):
    X, y, df = prepare_features(stock_data)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    last_features = X[-1].reshape(1, -1)
    next_value = model.predict(last_features)[0]

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    charts = {
        "history": plot_history(df),
        "pred_vs_actual": plot_pred_vs_actual(y_test, y_pred),
    }

    return next_value, rmse, r2, charts

# ------------------ Draw Charts ------------------
def plot_history(df):
    plt.figure(figsize=(8,4))
    plt.plot(df.index, df['Close'], label="Close", color="black")
    plt.plot(df.index, df['MA5'], label="MA5", color="blue")
    plt.plot(df.index, df['MA10'], label="MA10", color="orange")
    plt.legend()
    plt.title("Stock Price & Moving Averages")
    return fig_to_base64()

def plot_pred_vs_actual(y_test, y_pred):
    plt.figure(figsize=(8,4))
    plt.plot(y_test, label="Actual", color="black")
    plt.plot(y_pred, label="Predicted", color="green")
    plt.legend()
    plt.title("Prediction vs Actual (Test Data)")
    return fig_to_base64()

def fig_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return encoded

# ------------------ Routes ------------------
@app.route('/')
def display():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def show():
    ticker_symbol = request.form.get('stock_select')
    stock_data = get_stock_data(ticker_symbol)
    prediction, rmse, r2, charts = predict_stock_value(stock_data)

    return render_template(
        'index.html',
        prediction=prediction,
        rmse=round(rmse, 2),
        r2=round(r2, 2),
        charts=charts
    )

if __name__ == "__main__":
    app.run(debug=True)
