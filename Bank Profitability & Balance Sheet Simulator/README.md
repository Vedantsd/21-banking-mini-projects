# 🏦 Bank Profitability & Balance Sheet Simulator 

A mini banking web app built with **Flask** that simulates core profitability metrics:
**Interest Income, Interest Expense, Earning Assets, NIM, Operating Expense, Net Profit**.
It includes **CSV export** and a **SQLite-backed history** of previous runs.

---

## ✨ Features

- Clean 2-page flow: **Inputs → Results**
- Calculates:
  - Interest Income
  - Interest Expense
  - Earning Assets
  - Net Interest Margin (NIM)
  - Operating Expense
  - Net Profit (includes NPA loss)
- **Download CSV** report of results
- **SQLite** database to store and view history of calculations
- Minimal, responsive UI (HTML/CSS, Jinja2)

---

## 📥 Inputs (with units)

| Field                     | Unit     | Meaning |
|--------------------------|----------|---------|
| Loan Amount              | Currency | Total outstanding loans |
| Loan Interest Rate       | %        | Average annual loan rate |
| Deposits                 | Currency | Total customer deposits |
| Deposit Interest Rate    | %        | Average annual deposit rate the bank pays |
| Non-Performing Assets    | %        | Share of loans that are non-performing (NPA) |
| Operating Expense Ratio  | %        | OPEX as a % of deposits |

---

## 🧮 Formulas Used

- **Non-Performing Loans (NPL)**  
  `NPL = Total Loans × (NPA%/100)`

- **Performing Loans (Earning Loans)**  
  `Performing Loans = Total Loans − NPL = Total Loans × (1 − NPA%/100)`

- **Interest Income**  
  `Interest Income = Performing Loans × Loan Interest Rate`

- **Interest Expense**  
  `Interest Expense = Deposits × Deposit Interest Rate`

- **Earning Assets** *(simplified)*  
  `Earning Assets = Performing Loans`

- **Net Interest Margin (NIM)**  
  `NIM = (Interest Income − Interest Expense) / Earning Assets`

- **Operating Expense (if using ratio)**  
  `OPEX = Deposits × (OPEX Ratio/100)`

- **Net Profit**  
  `Net Profit = Interest Income − Interest Expense − OPEX − NPL`

---

## 📸 Screenshots

1. Data inputs page
<img width="1919" height="980" alt="image" src="https://github.com/user-attachments/assets/92bef8ab-20a9-463e-bfbb-6500d29a9aa4" />

2. Results page
<img width="1919" height="980" alt="image" src="https://github.com/user-attachments/assets/13a08918-a3b0-42ab-8716-6a9d7e69f0de" />

3. Previous calculations page
<img width="1919" height="982" alt="image" src="https://github.com/user-attachments/assets/d6f05470-6028-460f-b33c-2bc59587743e" />

4. CSV report data
<img width="308" height="238" alt="image" src="https://github.com/user-attachments/assets/781aafdd-3a23-4e64-9adf-acb9b8f17010" />
