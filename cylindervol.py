#!/usr/bin/python
# written by: atholcomb
# cylindervol.py
# computes the volume of a cylinder

def cylinder_volume(height, radius):
	pi = 3.14
	return height * pi * (radius ** 2)

print cylinder_volume(10, 3)
