#!/usr/bin/python3
# written by: atholcomb
# busride.py
# outputs the price of a bus ticket per person's age

age = int(input("Enter your age: "))

# bus fares for per age limit
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

# ticket price logic
if age <= free_up_to_age:
	ticket_price = 0
elif age <= child_up_to_age:
	ticket_price = concession_ticket
elif age >= senior_from_age:
	ticket_price = concession_ticket
else:
	ticket_price = adult_ticket

message = "A person who is {} years old, will pay ${:.2f} to ride the bus.".format(age, ticket_price)

print(message)
