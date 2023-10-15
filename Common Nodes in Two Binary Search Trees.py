# Python program of iterative traversal based method to
# find common elements in two BSTs.


# A BST node
class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


# A utility function to create a new node
def newNode(ele):
    temp = Node()
    temp.key = ele
    temp.left = temp.right = None
    return temp


# A utility function to do inorder traversal
def inorder(root, traversal):
    if root != None:
        inorder(root.left, traversal)
        traversal.append(root.key)
        inorder(root.right, traversal)


# Function two print common elements in given two trees
def printCommon(root1, root2):
    inorder1 = []
    inorder2 = []

    # Storing inorder traversal of both the trees
    inorder(root1, inorder1)
    inorder(root2, inorder2)

    print("Tree 1 : ")
    for i in range(len(inorder1)):
        print(inorder1[i], end=" ")

    print()

    print("Tree 2 : ")
    for i in range(len(inorder2)):
        print(inorder2[i], end=" ")

    print()

    print("Common Nodes: ")

    # Using two pointers calculating common nodes in both the traversals
    i = 0
    j = 0
    while i < len(inorder1) and j < len(inorder2):
        if inorder1[i] == inorder2[j]:
            print(inorder1[i], end=" ")
            i = i + 1
            j = j + 1

        elif inorder1[i] < inorder2[j]:
            i = i + 1
        else:
            j = j + 1

    print()


# A utility function to insert a new Node
# with given key in BST
def insert(node, key):
    # If the tree is empty, return a new Node
    if node == None:
        return newNode(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the (unchanged) Node pointer
    return node


# Driver program
# Create first tree as shown in example
root1 = None
root1 = insert(root1, 5)
root1 = insert(root1, 1)
root1 = insert(root1, 10)
root1 = insert(root1, 0)
root1 = insert(root1, 4)
root1 = insert(root1, 7)
root1 = insert(root1, 9)

# Create second tree as shown in example
root2 = None
root2 = insert(root2, 10)
root2 = insert(root2, 7)
root2 = insert(root2, 20)
root2 = insert(root2, 4)
root2 = insert(root2, 9)

printCommon(root1, root2)
