# A tree is almost similar to a linked list but the only difference is 
# that in a linked list a node can only link to one other node while 
# in a tree each node can link to multiple other nodes

# binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_sum(root):
    if root == None:
        return 0
    
    return root.data + find_sum(root.left) + find_sum(root.right)


# node2 is the root node
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("The sum of values in the tree is: {}".format(find_sum(node2)))

