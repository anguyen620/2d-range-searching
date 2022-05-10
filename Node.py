class Node:
	def __init__(self, val, left = NULL, right = NULL):
		self._value = val
		self._left = left
		self._right = right

	def getValue(self):
		return self._value

	def getRight(self):
		return self._right
	
	def getLeft(self):
		return self._left
