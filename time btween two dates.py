from datetime import date

first_date = input("Enter the first date")
second_date = input("Enter the second date")

delta = first_date - second_date

print(delta.days)
