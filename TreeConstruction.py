import Node

# takes a x-sorted list of (x,y) tuples
createTree(points, flag=True):
	if len(points) == 1:
		node = Node(points[0])
	else:
		middle = len(points)//2
		node = Node(points[middle])
		node.setLeft(createTree(points[:middle], flag)
		node.setRight(createTree(points[middle+1:], flag)

	if flag:
		node.setAuxTree(createTree(sorted(points, key=lambda x: x[1]), flag=False))

	return node
