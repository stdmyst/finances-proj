from pprint import pprint
from datetime import datetime

import pandas as pd


def get_transactions(url):
    transactions = []

    df = pd.read_excel(url)
    print(df.columns)

    for _, el in df.iterrows():
        (
            op_datetime, pay_datetime, card, status,
            op_sum, op_currency, pay_sum, pay_currency,
            cashback, category, mcc, description, bonus, rounding, sum_with_rounding
        ) = el
        pay_sum = float(pay_sum)
        op_sum = float(op_sum)

        transaction = {
            "bank": "Tinkoff",
            "op_datetime": datetime.strptime(op_datetime, "%d.%m.%Y %H:%M:%S"),
            "pay_datetime": None if pd.isna(pay_datetime) else datetime.strptime(pay_datetime, "%d.%m.%Y"),
            "card": card,
            "status": status,
            "op_sum": op_sum,
            "op_currency": op_currency,
            "pay_sum": pay_sum,
            "pay_currency": pay_currency,
            "cashback": float(cashback),
            "category": category,
            "mcc": mcc,
            "description": description,
            "bonus": float(bonus),
            "rounding": rounding,
            "sum_with_rounding": sum_with_rounding,
            "debit": pay_sum if pay_sum > 0 else 0, 
            "credit": -pay_sum if pay_sum < 0 else 0,
            }
        transactions.append(transaction)
        
    return transactions


if __name__ == "__main__":
    print(get_transactions("_filepath_"))