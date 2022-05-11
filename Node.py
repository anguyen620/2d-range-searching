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

	def isLeaf(self):
		if self._left == NULL and self._right == NULL:
			return True
		else:
			return False

	def getLeaves(self):
		leaves = []

		# Leaf
		if self.isLeaf():
			return [self._value]

		# Get left side		
		if self._left != NULL:
			leaves + self._getLeaves(self._left)

		# Get right side
		if self._right != NULL:
			leaves + self._getLeaves(self.right)

		return leaves


