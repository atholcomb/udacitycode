#!/usr/bin/python3
# written by: atholcomb
# how_many_days.py
# outputs the number of weeks and days in the given number of days inputted

def how_many_days(num):
	"""Print the number of weeks and days from the number of days entered"""
	# use integer division to output weeks
	weeks = num // 7
	# to get number of days, use the modulus operator
	days = num % 7
	print("{} week(s) and {} day(s)".format(weeks, days))

# test cases
how_many_days(1)
how_many_days(6)
how_many_days(7)
how_many_days(9)
how_many_days(9195)
