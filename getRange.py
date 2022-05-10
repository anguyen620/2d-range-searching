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
