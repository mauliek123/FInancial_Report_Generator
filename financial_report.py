import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import schedule
import time
from datetime import datetime

# DB Connection
db_config = {
    'user': 'root',
    'password': 'Maulie15k#',
    'host': 'localhost',
    'database': 'financial_reporting'
}

def generate_report():
    print(f"[{datetime.now()}] Starting report generation...")

    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    
    # Read Data
    transactions_df = pd.read_sql("SELECT * FROM transactions", conn)
    taxes_df = pd.read_sql("SELECT * FROM taxes", conn)
    conn.close()

    # Calculate KPIs
    total_income = transactions_df[transactions_df['type'] == 'income']['amount'].sum()
    total_expense = transactions_df[transactions_df['type'] == 'expense']['amount'].sum()
    total_tax = taxes_df['amount'].sum()
    profit = total_income - total_expense - total_tax
    profit_margin = (profit / total_income) * 100 if total_income > 0 else 0

    # Create Summary DataFrame
    summary_df = pd.DataFrame({
        'Total Income': [total_income],
        'Total Expense': [total_expense],
        'Total Tax': [total_tax],
        'Profit': [profit],
        'Profit Margin (%)': [profit_margin]
    })

    # Save Report
    file_name = f"financial_report_{datetime.now().strftime('%Y%m%d')}.csv"
    summary_df.to_csv(file_name, index=False)

    print(f"[{datetime.now()}] Report saved as {file_name}")

# Schedule report daily at 9 AM
schedule.every().day.at("09:00").do(generate_report)

# Run once immediately for testing
generate_report()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
