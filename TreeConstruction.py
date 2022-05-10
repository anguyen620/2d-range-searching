def insert(rootNode, interval):	
    # Base case
    if rootNode == NULL:
        return Node()

    low = rootNode.getInterval().getLow()

    # If low value is smaller, new interval goes to the left
    if interval.getLow() < low:
        rootNode.setLeft(insert(rootNode.getLeft(), interval))

    # Else, goes to the right
    else:
        rootNode.setRight(insert(rootNode.getRight(), interval))


