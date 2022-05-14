from Node import *
from Query import *

def range1D(node, query, y0=-1000, y1=1000):
	if node == None:
		return []

	val = node.getValue()

	# If node is a leaf
	if node.isLeaf():
		# Check if node in range
                if val[1] >= query.getLowY() and val[1] <= query.getHighY():
                        return [val]
                else:
                        return []	

	# If query contains [y0,y1]
	elif y0 >= query.getLowY() and y1 <= query.getHighY():
		return node.getLeaves()

	# If query is disjoint with [y0, y1]
	elif query.getHighY() < y0 or query.getLowY() > y1:
                return []

	else:
		return range1D(node.getLeft(), query, y0, val[1]) + range1D(node.getRight(), query, val[1], y1)

def range2D(node, query, x0=-1000, x1=1000):
	if node == None:
		return []

	val = node.getValue()

	# If node is a leaf
	if node.isLeaf():
		# Check if node in range
		if val[0] >= query.getLowX() and val[0] <= query.getHighX():
			return [val]
		else:
			return []

	# If query contains [x0,x1]
	elif x0 >= query.getLowX() and x1 <= query.getHighX():
		return range1D(node.getAuxTree(), query) 

	# If query is disjoint with [x0, x1]
	elif query.getHighX() < x0 or query.getLowX() > x1:
		return []

	else:
		return range2D(node.getLeft(), query, x0, val[0]) + range2D(node.getRight(), query, val[0], x1)
