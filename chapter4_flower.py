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

def arc(t, r, angle):
	"""Draws an arc with radius r and specified angle"""
	arc_length = 2 * math.pi * r * (angle/360.0)
	n = int(arc_length/3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)
	
def petal(t, r, angle):
	"""Draws a petal with radius r and specified angle"""
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)
	
	
def flower(t, r, angle, n):
	"""Draws a flower with radius r, specified angle and number of petals specified"""
	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)

def move(t, steps):
	"""Helps Turtle to move in the space for this exercise"""
	pu(t)
	fd(t, steps)
	pd(t)
	
"""Solution to Exercise chapter 4"""

##Flower 1
move(bob, -100)
flower (bob, 60.0, 60.0, 7)

##Flower 2
move(bob, 100)
flower(bob, 40.0, 80.0, 10)

##Flower 3
move(bob, 100)
flower(bob, 140.0, 20.0, 20)

wait_for_user()