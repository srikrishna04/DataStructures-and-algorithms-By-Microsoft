class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None 
    def treeHeight(self):
        if self is None:
            return 0
        else:
            return 1 + max(TreeNode.treeHeight(self.left) ,TreeNode.treeHeight(self.right))
    def treeSize(self):
        if self is None:
            return 0
        else:
            return 1 + TreeNode.treeSize(self.left) + TreeNode.treeSize(self.right)
    def inOrder(self):
        if self is None: 
            return []
        return (TreeNode.inOrder(self.left) + [self.key] + TreeNode.inOrder(self.right))
       
    def display(self, space="\t", level=0):
        if self is None:
            print(space*level + "⌀")
            return
        elif self.left is None and self.right  is None:
            print(space*level + str(self.key))
            return
        TreeNode.display(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display(self.left, space, level+1)
    def treeToTuple(self):
        if self is None:
            return None
        elif self.left is None and self.right is None:
            return self.key
        else:
            return TreeNode.treeToTuple(self.left), self.key, TreeNode.treeToTuple(self.right)
    def __str__(self):
        return "BinaryTree <{}>".format(self.treeToTuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.treeToTuple())
    @staticmethod    
    def toTree(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.toTree(data[0])
            node.right = TreeNode.toTree(data[2])
        else:
            node = TreeNode(data)
        return node
x = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.toTree(x)
print(tree)
print(tree.inOrder())
print(tree.treeHeight())
print(tree.treeSize())
print(tree.treeToTuple())
tree.display('  ')
