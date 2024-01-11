import datetime as dt

date_of_transaction = dt.datetime.now()
formatted_datetime = date_of_transaction.strftime("%Y-%m-%d %H:%M:%S:2d")

print(date_of_transaction)
