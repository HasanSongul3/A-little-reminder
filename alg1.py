import time
import datetime

date_str = input("Please enter a date in dd-mm-yy format: ")
date = datetime.datetime.strptime(date_str, '%d-%m-%y').date()

while True:
    now = datetime.datetime.today()
    if date == now:
        print("Your date has come!")
        break
    else:
        time.sleep(10000)

