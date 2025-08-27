from flask import Flask, render_template, request, make_response
import db_helper
import csv
import io



# -- Helper methods --

def calc_interest_income(total_loan_amount, loan_interest_rate, non_performing_assets):
    interest_income = total_loan_amount * loan_interest_rate * (1 - non_performing_assets)
    return interest_income

def calc_interest_expense(deposits, deposit_interest_rate):
    interest_expense = deposits * deposit_interest_rate
    return interest_expense

def calc_earning_asset(total_loan_amount, non_performing_assets):
    earning_asset = total_loan_amount * (1 - non_performing_assets)
    return earning_asset

def calc_net_interest_margin(interest_income, interest_expense, earning_asset):
    net_interest_margin = (interest_income - interest_expense) / earning_asset
    return round(net_interest_margin, 4)

def calc_operating_expense(deposits, opex_value):
    operating_expense = deposits * opex_value
    return operating_expense

def calc_net_profit(interest_income, interest_expense, operating_expense, non_performing_assets, total_loan_amount):
    npa_loss_amount = total_loan_amount * (non_performing_assets / 100)
    net_profit = interest_income - interest_expense - operating_expense - npa_loss_amount
    return round(net_profit, 2)



# -- Python Flask App --

app = Flask(__name__)

@app.route('/')
def inputs():
    return render_template('inputs.html')


@app.route('/calculate', methods=['POST'])
def results():

    data = request.form.to_dict()

    total_loan_amount = int(data['loan_amount'])
    loan_interest_rate = float(data['loan_interest_rate']) / 100
    non_performing_assets = float(data['non_performing_assets']) / 100
    deposits = int(data['deposits'])
    deposit_interest_rate = float(data['deposit_interest_rate']) / 100
    opex_value = float(data['opex_ratio']) / 100

    interest_income = calc_interest_income(total_loan_amount, loan_interest_rate, non_performing_assets)
    interest_expense = calc_interest_expense(deposits, deposit_interest_rate)
    earning_assets = calc_earning_asset(total_loan_amount, non_performing_assets)
    net_interest_margin = calc_net_interest_margin(interest_income, interest_expense, earning_assets)
    operating_expense = calc_operating_expense(deposits, opex_value)
    net_profit = calc_net_profit(interest_income, interest_expense, operating_expense, non_performing_assets, total_loan_amount)

    calculated_data = {
        'loan_amount': total_loan_amount,
        'loan_interest_rate': loan_interest_rate,
        'deposits': deposits,
        'deposit_interest_rate': deposit_interest_rate,
        'non_performing_assets': non_performing_assets,
        'opex_ratio': opex_value,
        'interest_income': interest_income,
        'interest_expense': interest_expense,
        'earning_assets': earning_assets,
        'net_interest_margin': net_interest_margin,
        'operating_expense': operating_expense,
        'net_profit': net_profit
    }


    # -- Insert calculated data to database -- 
    db_helper.insert_data(calculated_data)

    return render_template('results.html', 
                        interest_income=interest_income,
                        interest_expense=interest_expense,
                        earning_assets=earning_assets,
                        net_interest_margin=net_interest_margin,
                        operating_expense=operating_expense,
                        net_profit=net_profit)


# -- Download a .CSV report of the calculated data
@app.route('/download_csv', methods=['POST'])
def download_csv():
    data = request.form.to_dict()

    results = {
        "Interest Income": data['interest_income'],
        "Interest Expense": data['interest_expense'],
        "Earning Assets": data['earning_assets'],
        "Net Interest Margin": data['net_interest_margin'],
        "Operating Expense": data['operating_expense'],
        "Net Profit": data['net_profit']
    }

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Metric", "Value"])
    for key, value in results.items():
        writer.writerow([key, value])

    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=balance_sheet_report.csv"
    response.headers["Content-type"] = "text/csv"
    return response

@app.route('/history', methods=['POST'])
def history():
    rows = db_helper.fetch_data()
    return render_template('history.html', rows=rows)

if __name__ == "__main__":
    db_helper.create_db()
    app.run(debug=True)