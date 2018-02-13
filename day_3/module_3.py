'''
Created on Feb 7, 2018

@author: mmp
'''
import os

class Codons:
	
	def __init__(self):
		self.dict_codon = {}

	def count_codons(self, file_name):
		"""
		count codons and put the result in a list
		"""
		self.file_name = file_name
		if not os.path.exists(file_name):
			raise IOError('File does not exist ' + self.file_name)
		
		with open(self.file_name) as handle_in:
			for line in handle_in:
				temp_line = line.strip()
				if (len(temp_line) == 0): continue
				if (temp_line[0] == '>'): continue
				self.count_codons_by_sequence(line)
		
	def count_codons_by_sequence(self, sequence):
		"""
		"""
		for i in range(0, len(sequence), 3):
			if ((i + 2) >= len(sequence)): continue
			codon = '{}{}{}'.format(sequence[i], sequence[i+1], sequence[i+2])
			if (codon in self.dict_codon): self.dict_codon[codon] += 1
			else: self.dict_codon[codon] = 1
	
	def print_codons(self):
		print(self.file_name)
		for key in sorted(self.dict_codon.keys()):
			print(key, self.dict_codon[key])
	
	def save_file(self, file_name_out):
		
		with open(file_name_out, 'w') as handle_out:
			for key in sorted(self.dict_codon.keys()):
				handle_out.write('{} {}\n'.format(key, self.dict_codon[key]))
		print('file saved: ' + file_name_out)

if __name__ == '__main__':
	
	codons = Codons()
	codons.count_codons('ref_H3.fasta')
	codons.print_codons()
	codons.save_file('result_codons.txt')
	
