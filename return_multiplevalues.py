import pytest

# A Python program to to return multiple 
# values from a method using class

def test_multiplevalues():
	class Test:
		def __init__(self):
			self.str = "geeksforgeeks"
			self.x = 20  
	 
	# This function returns an object of Test
	def fun():
		return Test()
		 
	# Driver code to test above method
	t = fun() 
	print "\t"
	print(t.str)
	print(t.x)