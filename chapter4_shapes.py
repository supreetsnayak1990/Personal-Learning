from swampy.TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polyline(t, n, length, angle):
	"""Draws n line segments with the given length and angle in degrees between them. t is a turtle instance from swampy package"""
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def polygon(t, length, n):
	"""Draws a polygon with specified length and number of sides"""
	angle = 360.0 / n
	polyline(t, n, length, angle)
	
def triangle(t, length, angle):
	fd(t, length)
	lt(t, (180 -((180.0-angle)/2.0)))
	fd(t, 2*length*(math.sin(math.pi*angle/360.0)))
	lt(t, (180 -((180.0-angle)/2.0)))
	fd(t, length)
	lt(t, 180-angle)
	
def shape(t, length, n):
	lt(t, 180.0/n)
	angle = 360.0/n
	for i in range(n):
		triangle(t, length, angle)
		lt(t, 360.0/n)
	rt(t, 180.0/n)

def move(t, steps):
	"""Helps Turtle to move in the space for this exercise"""
	pu(t)
	fd(t, steps)
	pd(t)
	
##Solution to Chapter 4 question

##Shape1
move(bob,-120)		
shape(bob, 60.0, 5)

##Shape2
move(bob,120)		
shape(bob, 60.0, 6)

##Shape3
move(bob,120)		
shape(bob, 60.0, 7)
	
	
wait_for_user()