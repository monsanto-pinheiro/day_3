'''
Created on Feb 5, 2018

@author: mmp
'''
DNA_BASES = ['A', 'C', 'T', 'G', 'U']

def reverse(sequence):
	return sequence[::-1]
	
def complement(sequence):
	sz_return = ''
	for base in sequence:
		if (base == 'A' or base == 'a'): sz_return += 'T'
		elif (base == 'C' or base == 'c'): sz_return += 'G'
		elif (base == 'G' or base == 'g'): sz_return += 'C'
		elif (base == 'T' or base == 't' or base == 'U' or base == 'u'): sz_return += 'A'
		else: sz_return += base
	return sz_return
	
def clean_fasta(sequence):
	"""
	clean fasta, remove all letters unless ACTG
	"""
	seq_return = ""
	for i in sequence:
		if i.upper() in DNA_BASES:
			seq_return += i.upper()
	return seq_return

if __name__ == "__main__":
	seq = 'accatatatagasfwefwgaggagattgq'
	seq_cleaned = clean_fasta(seq)
	print(seq_cleaned)

	print('reverse:', reverse(seq_cleaned))	
	print('reverse complement:', complement(reverse(seq_cleaned)))
	print('original reverse complement:', complement(reverse(seq)))
	
	### count dna bases
	print('Count bases')
	for base in DNA_BASES:
		print('{} -> {}'.format(base, seq_cleaned.count(base)))

