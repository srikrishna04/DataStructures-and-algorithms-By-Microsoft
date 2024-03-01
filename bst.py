class TreeNode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None 
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
def remove_none(numbers):
    return [i for i in numbers if i is not None]
def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bin_r, min_r, max_r = is_bst(node.right)
    is_bst_node = (is_bst_l and is_bin_r and (max_l is None or max_l < node.key) and (max_r is None or min_r > node.key))
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    return is_bst_node, min_key, max_key
# insertion
class BstNode:
    def __init__(self, key, value=None):
        self.key= key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
def insert(node, key, value):
    if node is None:
        node = BstNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node
def find(node, key):
    if node is None:
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return find(node.left, key)
    elif key > node.key:
        return find(node.right, key)
def update(node, key, value):
    success = find(node, key)
    if success is not None:
        success.value = value
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
def is_balanced(node):
    if node is None:
        return True, 0
    bal_l, height_l = is_balanced(node.left)
    bal_r, height_r = is_balanced(node.right)
    bal = bal_l and bal_r and abs(height_l - height_r)<=1
    height = 1 + max(height_l + height_r)
    return bal, height

def make_balan_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) -1
    if lo > hi:
        return None
    mid = (lo+hi) // 2
    key, value = data[mid]
    node = BstNode(key, value)
    node.parent = parent
    node.left = make_balan_bst(data, lo, mid-1, node)
    node.right = make_balan_bst(data, mid+1, hi, node)
    return node
def balan_bst(num):
    return make_balan_bst(list_all(num))
# check bst
tree1 = TreeNode.toTree(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(is_bst(tree1))

tree = insert(None, 'royal', 1)
insert(tree, 'handsome', 2)
insert(tree, 'happy', 3)
insert(tree, 'tour', 4)
insert(tree, 'peace', 5)
# TreeNode.display(tree)

# original = find(tree, 'happy')
# print(original.key, original.value)

# update(tree, 'tour', 10)
# new = find(tree, 'tour')
# print(new.key, new.value)

# print(list_all(tree))

# print(is_balanced(tree))

# x = list_all(tree)
# tr1 = make_balan_bst(x)
# TreeNode.display(tr1)

# TreeNode.display(balan_bst(tree))