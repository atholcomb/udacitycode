#!/usr/bin/python3
# written by: atholcomb
# even_or_odd.py
# reads a integer and prints out whether it is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
	print("The number " + str(number) + " is even.")
else:
	print("The number " + str(number) + " is odd.")