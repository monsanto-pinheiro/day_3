'''
Created on Feb 7, 2018

@author: mmp
'''
import unittest
import second_module

class Test(unittest.TestCase):


	def test_clean_fasta(self):
		self.assertEqual('AAACCTTT', second_module.clean_fasta('aaaccttt'))
		self.assertEqual('AAACCTTT', second_module.clean_fasta('AAACCTTT'))
		self.assertEqual('AAACCTTT', second_module.clean_fasta('asdsaaccttt'))
		self.assertEqual('', second_module.clean_fasta(''))
		self.assertEqual('AATTTUUUCCTT', second_module.clean_fasta('aatttuuucctt'))
		self.assertTrue(second_module.clean_fasta('') == '')

	def test_complement(self):
		self.assertEqual('AATT', second_module.complement('TTAA'))
		self.assertEqual('AATTGGCCDAA', second_module.complement('TTAACCGGDUu'))

	def test_reserve(self):
		self.assertEqual('AATT', second_module.reverse('TTAA'))
	
	def runTest(self):
		self.test_clean_fasta()
		self.test_complement()
		self.test_reserve()
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()