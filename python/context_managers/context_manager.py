'''
Context Managers & "with" statement.
Example: Simple File reading
'''

import io

# file resource management without using context managers
file = open('sample.txt', 'w')
try:
	file.write('Python is super awesome!')
finally:
	file.close()

# file resource management without using context managers

with open('sample.txt', 'w') as file:
	file.write('Python is super awesome!')

class open(object):

	def __init__(self, file_name, mode='r'):
		print('__init__ called')
		self.file_name = file_name
		self.mode = mode

	def __enter__(self):
		print('__enter__ called')
		self.file = io.open(self.file_name, self.mode)
		return self.file

	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__ called')
		self.file.close()
