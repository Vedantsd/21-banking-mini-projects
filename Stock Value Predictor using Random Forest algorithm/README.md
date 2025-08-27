# 📈 Stock Value Predictor using Random Forest  

This project is a **machine learning-powered stock price prediction app** built with **Flask**.  
It uses **Random Forest Regression** on historical stock market data (fetched using `yfinance`) to predict the **next closing price** of a chosen stock or index.  

---

## 🚀 Features  

- **User-Friendly Web Interface**  
  - Search & select stocks/indices from a dropdown list.  
  - Clean and responsive design with **mobile compatibility**.  

- **Stock Price Prediction**  
  - Predicts the **next day’s closing price** using a trained **Random Forest model**.  
  - Uses technical indicators like:  
    - Moving Average (5-day & 10-day)  
    - Percentage Returns  
    - Previous Close Prices  

- **Model Accuracy Metrics**  
  - Displays **Root Mean Squared Error (RMSE)** for error analysis.  
  - Shows **R² Score** for variance explanation.  

- **Interactive Visualizations**  
  - 📊 **Historical Stock Prices Chart**  
  - 📊 **Prediction vs Actual Chart**  
  - Charts are rendered dynamically using **Matplotlib** and embedded in the webpage.  

- **Lightweight & Fast**  
  - Powered by **Flask backend** and **Scikit-learn**.  
  - No heavy database or APIs required (uses Yahoo Finance).  

- **Clean UI/UX**  
  - Minimal white-shaded design.  
  - Clear separation of input & output sections.  
  - Mobile-friendly layout with smooth transitions.  

---

## 🛠️ Tech Stack  

- **Backend:** Flask, Python  
- **Frontend:** HTML, CSS, JavaScript (Select2 for stock search)  
- **Machine Learning:** Scikit-learn (Random Forest)  
- **Data Source:** Yahoo Finance (`yfinance`)  
- **Visualization:** Matplotlib  

---

⚡ *Note:* Predictions are based only on past 1-year prices & simple technical indicators.  
Real-world stock movements depend on many factors not included here (macro trends, news, events, etc.).  
