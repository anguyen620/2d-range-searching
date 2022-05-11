def range1D(node, query, y0, y1):
	val = node.getValue()

	# If node is a leaf
	if node.getleft() == NULL and node.getRight() == NULL:
		# Check if node in range
                if val >= query.getLowY() and val <= query.getHighY():
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
		return range1D(node.getLeft(), query, y0, val) + range1D(node.getRight(), query, val, y1)

def range2D(node, query, x0, x1):
	val = node.getValue()

	# If node is a leaf
	if node.getleft() == NULL and node.getRight() == NULL:
		# Check if node in range
		if val >= query.getLowX() and val <= query.getHighX():
			return [val]
		else:
			return []

	# If query contains [x0,x1]
	elif x0 >= query.getLowX() and x1 <= query.getHighX():
		return range1D(node.getAuxTree(), query, -1000, 1000) # Ideally, would do -infinity and infinity

	# If query is disjoint with [x0, x1]
	elif query.getHighX() < x0 or query.getLowX() > x1:
		return []

	else:
		return range2D(node.getLeft(), query, x0, val) + range2D(node.getRight(), query, val, x1)
