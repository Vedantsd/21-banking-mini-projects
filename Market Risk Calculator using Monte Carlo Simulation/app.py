from flask import Flask, render_template, request
from datetime import datetime, timedelta
import yfinance as yf
import numpy as np
import pandas as pd


def monte_carlo_var(prices_dict, weights, portfolio_value, horizon_days, confidence, n_sim=10000):
    """
    
    Parameters used: 
    1. prices_dict -> A dictionary of closed prices of each index
    2. weights -> A tuple of weights for each index
    3. portfolio_value -> The total investment value
    4. horizon_days -> The time horizon to calculate VaR
    5. confidence -> The confidence level for estimation
    6. n_sim -> Number of simulations for the Monte Carlo simulations


    Steps to calculate VaR: 
    Step 1 -> Combine all the indices data into a single frame
    Step 2 -> Compute the daily log returns 
    Step 3 -> Calculate mean and covariance of returns 
    Step 4 -> Adjust mean and covariances of returns for the time horizon
    Step 5 -> Simulate the correlated returns
    Step 6 -> Compute the portfolio returns per simulation 
    Step 7 -> Calculate portfolio PnL 
    Step 8 -> Calculate the Value at Risk (VaR) at given confidence level

    """
    dataframe = pd.concat(prices_dict.values(), axis=1)
    dataframe.columns = prices_dict.keys()
    dataframe = dataframe.dropna()

    log_returns = np.log(dataframe / dataframe.shift(1)).dropna()

    mean_ret = log_returns.mean().values
    cov_ret = log_returns.cov().values

    mean_ret_hor = mean_ret * horizon_days
    cov_ret_hor = cov_ret * horizon_days

    sims = np.random.multivariate_normal(mean_ret_hor, cov_ret_hor, size=n_sim)

    portfolio_returns = sims.dot(np.array(weights))

    pnl = portfolio_value * portfolio_returns

    var = -np.percentile(pnl, (1-confidence)*100)

    return {
        "VaR": round(var, 4),
        "mean_pnl": round(pnl.mean(), 4),
        "worst_loss": round(pnl.min(), 4),
        "simulated_pnl": pnl
    }

def get_end_date(start_date, day_count):
    date_obj  = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=day_count)
    end_date = new_date.strftime('%Y-%m-%d')
    return end_date

def get_single_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']


def get_stock_data(start_date, end_date):
    prices_dict = {
        "Nifty": get_single_stock_data('^NSEI', start_date, end_date),
        "Sensex": get_single_stock_data('^BSESN', start_date, end_date),
        "BankNifty": get_single_stock_data('^NSEBANK', start_date, end_date)
    }

    return prices_dict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inputs.html')


@app.route('/submit', methods=['POST'])
def submit():

    total_investment = int(request.form.get('invested_amount'))

    start_date = request.form.get('start_day')
    day_count = int(request.form.get('day_count'))
    end_date = get_end_date(start_date, day_count)

    nifty_weight = int(request.form.get('nifty')) / 100
    sensex_weight = int(request.form.get('sensex')) / 100
    banknifty_weight = int(request.form.get('banknifty')) / 100

    confidence = int(request.form.get('confidence')) / 100

    weights = (nifty_weight, sensex_weight, banknifty_weight)
    prices_dict = get_stock_data(start_date, end_date)


    mc_result = monte_carlo_var(prices_dict=prices_dict, weights=weights, portfolio_value=total_investment, horizon_days=day_count, confidence=confidence)

    result = {
        "invested_amount": total_investment,
        "confidence": confidence,
        "weights": weights,
        "mean_pnl": mc_result["mean_pnl"],
        "worst_loss": mc_result["worst_loss"],
        "VaR": mc_result["VaR"]
    }

    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)