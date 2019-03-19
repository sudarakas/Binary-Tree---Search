class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def searchNode(node, key):
    if (node == None):
        return False
    
    if (node.value == key):
        return True
    
    searchLeft = searchNode(node.left, key)
    searchRight = searchNode(node.right, key)

    return searchLeft or searchRight


#build the tree
root = Node(55)

root.left = Node(29)
root.right = Node(87)

root.left.left = Node(42)
root.left.right = Node(20)

root.right.left = Node(60)
root.right.right = Node(91)

#search keys
print(searchNode(root, 91))
print(searchNode(root, 46565))
