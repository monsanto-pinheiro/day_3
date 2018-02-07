'''
Created on Feb 7, 2018

@author: mmp
'''
import unittest
import utils

class Test(unittest.TestCase):

	def test_is_float(self):
		self.assertIsNone(utils.is_float('valor'))
		self.assertEqual(10.0, utils.is_float('10'))
		self.assertEqual(10.0, utils.is_float(10))
		self.assertIsNone(utils.is_number('valor'))
		self.assertEqual(10, utils.is_number('10'))
		self.assertEqual(10, utils.is_number(10))

	def runTest(self):
		self.test_is_float()

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_is_float']
	unittest.main()