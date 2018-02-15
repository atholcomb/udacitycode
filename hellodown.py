#!/usr/bin/python3
# written by: atholcomb
# hellodown.py
# prints out the string vertically

def main():
	string = input("Enter string: ")
	hello(string)	

def hello(string):
	for n in string:
		print(n)

main()
