import sqlite3



def create_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    loan_amount REAL,
                    loan_interest_rate REAL,
                    deposits REAL,
                    deposit_interest_rate REAL,
                    non_performing_assets REAL,
                    opex_ratio REAL,
                    interest_income REAL,
                    interest_expense REAL,
                    earning_assets REAL,
                    net_interest_margin REAL,
                    operating_expense REAL,
                    net_profit REAL
                )''')
    conn.commit()
    conn.close()


def insert_data(data):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO calculations 
        (loan_amount, loan_interest_rate, deposits, deposit_interest_rate, non_performing_assets, 
        opex_ratio, interest_income, interest_expense, earning_assets, net_interest_margin, 
        operating_expense, net_profit) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (
        data['loan_amount'], data['loan_interest_rate'], data['deposits'], data['deposit_interest_rate'],
        data['non_performing_assets'], data['opex_ratio'], data['interest_income'], data['interest_expense'],
        data['earning_assets'], data['net_interest_margin'], data['operating_expense'], data['net_profit']
    ))
    conn.commit()
    conn.close()


def fetch_data():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calculations ORDER BY id DESC LIMIT 10')
    rows = cursor.fetchall()
    return rows
    

