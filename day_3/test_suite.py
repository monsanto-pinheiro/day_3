'''
Created on Feb 7, 2018

@author: mmp
'''
import unittest
import tests_utils
import test_clean_fasta

def suite():
	suite = unittest.TestSuite()
	suite.addTest(tests_utils.Test()) 
	suite.addTest(test_clean_fasta.Test()) 
	return suite


if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	test_suite = suite()
	runner.run(test_suite) 