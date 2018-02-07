#!/usr/bin/python3
# written by: atholcomb
# balance.py
# prints out two balances, phone and bank

phone_balance = 7.62
bank_balance = 104.39
#phone_balance = 12.34
#bank_balance = 25

if phone_balance < 10:
	phone_increase = phone_balance + 10
	bank_decrease = bank_balance - 10
print("Phone Balance: ", phone_increase)
print("Bank Balance: ", bank_decrease)
