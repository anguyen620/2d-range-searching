from TreeConstruction import *
from Query import *
from getRange import *

points = [(1,1), (1,4), (2,0), (2,2), (4,3)]
tree = createTree(points)
query = Query(1,2,1,3) # x = [1,2], y = [1,3]

print(range2D(tree, query))
