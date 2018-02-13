'''
Created on Feb 7, 2018

@author: mmp
'''
import unittest
from module_3 import Codons

class Test(unittest.TestCase):


	def test_count_codons_by_sequence(self):
		codons = Codons()
		codons.count_codons_by_sequence('AAA')
		self.assertEqual(1, codons.dict_codon['AAA'])
		self.assertFalse('CCC' in codons.dict_codon)
		codons.count_codons_by_sequence('CCC')
		self.assertEqual(1, codons.dict_codon['AAA'])
		self.assertEqual(1, codons.dict_codon['CCC'])
		codons.count_codons_by_sequence('CCC')
		codons.count_codons_by_sequence('CCC')
		self.assertEqual(3, codons.dict_codon['CCC'])
	
	def test_count_codons(self):
		codons = Codons()
		try:
			codons.count_codons('sddsdsfdsdsdfs')
			self.fail('must fail')
		except IOError as e:
			pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()