class Node:
	def __init__(self, val, left = NULL, right = NULL, auxTree = NULL):
		self._value = val
		self._left = left
		self._right = right
		self._auxTree = auxTree

	def getValue(self):
		return self._value

	def getRight(self):
		return self._right
	
	def getLeft(self):
		return self._left

	def getAuxTree(self):
		return self._auxTree

	def setAuxTree(self, auxTree):
		self._auxTree = auxTree
