'''
Created on Feb 7, 2018

@author: mmp
'''
import math

class Shape(object):
	'''
	classdocs
	'''

	def __init__(self, color, material, max_temperature = 20):
		'''
		Constructor
		'''
		self.color = color
		self.material = material
		self.max_temperature = max_temperature
		
	def __str__(self):
		return 'Color: {}   Material : {}  Max_Temp: {}'.format\
			(self.color, self.material, self.max_temperature)
	
	def __eq__(self, other):
		return self.color == other.color and \
			self.material == other.material and\
			self.max_temperature == other.max_temperature

class Rectangle(Shape):
	
	def __init__(self, comp, larg, color, material):
		Shape.__init__(self, color, material)
		self.comp = comp
		self.larg = larg
		
	def get_area(self):
		return self.comp * self.larg
	
	def __str__(self):
		return 'Rectangle -> Comp. {}  lag. {}  {}'.format(\
			self.comp, self.larg, super(Rectangle, self).__str__())
	
	def __eq__(self, other):
		return isinstance(other, Rectangle) and self.comp == other.comp and self.larg == other.larg\
			and super(Rectangle, self).__eq__(other)

class Circle(Shape):

	def __init__(self, radious, color, material):
		Shape.__init__(self, color, material)
		self.radious = radious
		
	def get_area(self):
		return 2 * math.pi * (self.radious ** 2)
	
	def __str__(self):
		return 'Circle -> Radious. {}   {}'.format(\
			self.radious, super(Circle, self).__str__())
	
	def __eq__(self, other):
		return isinstance(other, Circle) and self.radious == other.radious\
			and super(Circle, self).__eq__(other)
	
class Triangle(Shape):
	
	def __init__(self, cat1, cat2, color, material):
		Shape.__init__(self, color, material)
		self.cat1 = cat1
		self.cat2 = cat2
		
	def get_area(self):
		return (self.cat1 * self.cat2) / 2
	
	def __str__(self):
		return 'Triangle -> Cat1. {}  Cat2. {}  {}'.format(\
			self.cat1, self.cat2, super(Triangle, self).__str__())
	
	def __eq__(self, other):
		return isinstance(other, Triangle) and self.cat2 == other.cat2\
			and self.cat1 == other.cat1\
			and super(Triangle, self).__eq__(other)

class Shapes():
	
	def __init__(self):
		self.lst_shapes = []	
	
	def add_shape(self, shape):
		if (shape not in self.lst_shapes):
			self.lst_shapes.append(shape)
	
	def print_areas(self):
		for shape_temp in self.lst_shapes:
			print(shape_temp)
			print(shape_temp.get_area())
	
## start processing
if __name__ == '__main__':
	
	shapes = Shapes()
	shapes.add_shape(Rectangle(10, 20, (0,0,0), 'wood'))
	shapes.add_shape(Rectangle(10, 20, (0,0,0), 'wood'))
	shapes.add_shape(Triangle(10, 20, (0,0,0), 'metal'))
	shapes.add_shape(Circle(10, (0,0,0), 'glass'))
	shapes.add_shape(Circle(10, (255,0,0), 'glass'))
	shapes.print_areas()
	
# 	shape1 = Shape((0,0,0), 'wood') 
# 	shape3 = Shape((0,0,0), 'wood', 30)
# 	shape2 = Shape((255,255,255), 'glass')
# 	print(shape1)
# 	print(shape2) 
# 	print(shape1 == shape2)
# 	lst_shape = [shape1, shape2]
# 	if (shape3 not in lst_shape):
# 		lst_shape.append(shape3)
# 	print(lst_shape)
