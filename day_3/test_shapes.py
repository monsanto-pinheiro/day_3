'''
Created on Feb 7, 2018

@author: mmp
'''
import unittest
from shapes import Shape, Rectangle

class Test(unittest.TestCase):

	def test_shape(self):
		shape = Shape((0,0,0), 'wood')
		self.assertEqual('Color: (0, 0, 0)   Material : wood  Max_Temp: 20', str(shape))
		shape2 = Shape((0,0,0), 'wood')
		self.assertEqual(shape, shape2)
		shape3 = Shape((0,23,0), 'woodds')
		self.assertNotEqual(shape, shape3)
	
	def test_rectangle(self):
		rectangle = Rectangle(10, 20, (0,0,0), 'wood')
		self.assertEqual('Rectangle -> Comp. 10  lag. 20  Color: (0, 0, 0)'+\
						'   Material : wood  Max_Temp: 20', str(rectangle))
		self.assertEqual(200, rectangle.get_area())
		rectangle2 = Rectangle(10, 30, (0,0,0), 'wood')
		self.assertEqual(300, rectangle2.get_area())
		self.assertNotEqual(rectangle2, rectangle)
		rectangle3 = Rectangle(10, 20, (0,0,0), 'wood')
		self.assertEqual(rectangle3, rectangle)
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_shape']
	unittest.main()