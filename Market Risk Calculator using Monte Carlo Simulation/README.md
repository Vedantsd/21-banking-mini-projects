<<<<<<< HEAD
# 📊 Market Risk Calculator using Monte Carlo Simulation (Flask Web App)

A **fintech web application** built with **Flask** that calculates the **Value at Risk (VaR)** of a portfolio consisting of **Nifty50, Sensex, and Bank Nifty** indices using **Monte Carlo simulations**.  

The app allows users to input their portfolio weights, investment horizon, and confidence level, then simulates potential losses and calculates **VaR, Mean P&L, and Worst-case Loss**.

---

## 🚀 Features

- 📈 Fetches historical data for **Nifty50, Sensex, and Bank Nifty** using `yfinance`  
- 🧮 Runs **Monte Carlo simulations** to estimate Value at Risk (VaR)  
- 📊 Outputs:
  - Invested amount  
  - Portfolio weights  
  - Mean P&L  
  - Worst-case simulated loss  
  - VaR at chosen confidence level  
- 🎨 Modern and responsive UI (HTML + CSS with gradients and animations)  
- ✅ Input validation (ensures portfolio weights ≤ 100%)  

---

## 📝 Inputs & Formulas

### 🔢 User Inputs (via Web Form)
- **Invested Amount** – Total portfolio value (₹)
- **Portfolio Weights** – % allocation to:
  - Nifty50
  - Sensex
  - Bank Nifty
- **Start Date** – Historical data fetch start date
- **Time Horizon (days)** – Number of days to simulate risk over
- **Confidence Level (%)** – 

---

### 📐 Formulas & Methodology (Monte Carlo VaR)

1. **Log Returns**
   r_t = ln(P_t / P_(t-1))  
   where P_t = closing price at time t

2. **Mean & Covariance of Returns**
   - Mean vector: μ = mean(r_t)  
   - Covariance matrix: Σ = cov(r_t)

3. **Adjust for Time Horizon**
   - μ_h = μ × h  
   - Σ_h = Σ × h  
   where h = number of days in horizon

4. **Monte Carlo Simulations**
   Simulate N correlated returns (default N = 10,000):  
   R ~ Normal(μ_h, Σ_h)

5. **Portfolio Return**
   R_p = R · w  
   where w = vector of portfolio weights

6. **Portfolio P&L**
   P&L = V × R_p  
   where V = invested amount

7. **Value at Risk (VaR)**
   VaR_c = - Percentile(P&L, (1 - c) × 100)

---

### 📸 Screenshots

1. Inputs page
<img width="1919" height="980" alt="image" src="https://github.com/user-attachments/assets/f8a7f35c-7e44-4c0d-bf86-9af19a8783dc" />

2. Calculation results 
<img width="1919" height="979" alt="image" src="https://github.com/user-attachments/assets/410a11de-fc7c-49f0-8c51-367e19f61232" />



=======
# 📊 Monte Carlo VaR Calculator (Flask Web App)

A **fintech web application** built with **Flask** that calculates the **Value at Risk (VaR)** of a portfolio consisting of **Nifty50, Sensex, and Bank Nifty** indices using **Monte Carlo simulations**.  

The app allows users to input their portfolio weights, investment horizon, and confidence level, then simulates potential losses and calculates **VaR, Mean P&L, and Worst-case Loss**.

---

## 🚀 Features

- 📈 Fetches historical data for **Nifty50, Sensex, and Bank Nifty** using `yfinance`  
- 🧮 Runs **Monte Carlo simulations** to estimate Value at Risk (VaR)  
- 📊 Outputs:
  - Invested amount  
  - Portfolio weights  
  - Mean P&L  
  - Worst-case simulated loss  
  - VaR at chosen confidence level  
- 🎨 Modern and responsive UI (HTML + CSS with gradients and animations)  
- ✅ Input validation (ensures portfolio weights ≤ 100%)  

---

## 📂 Project Structure

.
├── app.py # Main Flask application
├── templates/
│ ├── inputs.html # Input form (portfolio details)
│ ├── result.html # Results page (VaR outputs)
├── static/ # (optional) for CSS/JS files if needed in future
├── requirements.txt # Python dependencies
└── README.md # Project documentation
>>>>>>> 48e9196 (Added Stock Value Predictor project)
