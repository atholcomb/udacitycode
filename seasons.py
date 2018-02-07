#!/usr/bin/python3
# written by: atholcomb
# season.py
# outputs what to do with a given season

def garden_cal():
	""" Print out what to do for a given season"""
	season = input("Enter a season: ")
	if season == "spring":
		print("Time to plant the garden!")
	elif season == "summer":
		print("Time to water the garden!")
	elif season == "autumn" or season == "fall":
		print("Time to harvest the garden!")
	elif season == "winter":
		print("Time to head inside!")
	else:
		print("I don't recognize the season")

garden_cal()
