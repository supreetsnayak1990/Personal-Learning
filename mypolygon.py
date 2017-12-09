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
	
def circle(t, r):
	"""Draws a circle with radius r"""
	arc(t, r, 360)

def sqaure(t, length):
	"""Draws a square with specified length"""
	polygon(t, length, 4)
	
circle(bob, 50)
sqaure(bob, 100)

wait_for_user()