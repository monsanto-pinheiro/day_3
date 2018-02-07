'''
Created on Feb 6, 2018

@author: mmp
'''

def is_number(valor):
	"""
	param: any value
	return: int if valor is integer
	"""
	try:
		return int(valor)
	except:
		return None
	
def is_float(valor):
	"""
	param: any value
	return: float if valor is real
	"""
	try:
		return float(valor)
	except:
		return None

