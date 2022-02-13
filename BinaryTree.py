# Chapter 12
# Binary search tree that has traverse, insert, delete, get minimum / maximum, get predecessor / successor functions

# Node class
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Binary tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # insert Node with integer v 
    def insert(self, v):
        node = Node(v)
        y = None
        x = self.root
        while x != None:
            y = x
            # if v is smaller than x.value, then we want to insert it in the left sub tree
            if v < x.value:
                x = x.left
            # otherwise in the right subtree
            else:
                x=x.right
        node.parent = y
        # Tree is empty, set node as root
        if y == None:
            self.root = node
        elif v < y.value:
            y.left = node
        else:
            y.right = node
    
    # find minimum value in tree
    # output: node with smallest value in tree
    def find_min(root):
        x = root
        # keep going left until we hit the left most node
        while x.left != None:
            x = x.left
        return x


    # find the smallest node whose value is bigger than a given node's value
    # input: node
    # output: node's successor node
    def find_successor(self,node):
        # if node's right subtree exists, return min node in the right subtree
        if node.right:
            return self.find_min(node.right)
        y = node.parent
        x = node
        # otherwise we go up the tree until we found the node whose left child is an ancestor of node
        while y!=None and y.right == x:
            x = y
            y = y.parent
        return y

    # inorder traverses the tree 
    # input: root of tree, empty array to store sorted nodes
    # returns: list of nodes 
    def inorder_traverse(root,result):
        if root == None:
            return result
        # append all nodes left of root
        BinaryTree.inorder_traverse(root.left, result)
        # append root
        result.append(root.value)
        # append all nodes right of root
        BinaryTree.inorder_traverse(root.right, result)
        return result

    # searched tree for a value
    # input: value to search for
    # output: True / False if tree contains the value
    def search(self,v):
        x = self.root
        while x != None:
            if x.value == v:
                return x
            if v < x.value:
                x = x.left
            else:
                x = x.right
        print("tree does not contain ", v)
        return None
    
    # deletes Note with value from tree
    # input: value v
    def delete(self,v):
        # first find the node containing v
        node = self.search(v)
        if node == None:
            return
        # if node has no left child, its right node takes its place
        if node.left == None:
            self.transplant(node,node.right)
        # if node has no right child, its left child takes its place
        elif node.right == None:
            self.transplant(node,node.left)
        # if node has a right and a left child
        else:
            y = self.find_successor(node)
            # if y is not node's right child but lies in node's right sub tree
            if y.parent != node:
                # replace y with y's right child and then replace node with y
                self.transplant(y,y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            # y's left child is always empty so we can safely set y's left subtree as node's left tree
            y.left = node.left
            y.left.parent = y


    
    # delete helper. replaceses subtree at node 1 with subtree at node 2
    # input: node 1, node 2
    def transplant(self,node1, node2):
        # if node 1 is the root
        if node1.parent == None:
            self.root = node2
        # if node 1 is a left node
        elif node1.parent.left == node1:
            node1.parent.left = node2
        # if node 1 is a right node
        else:
            node1.parent.right=node2
        if node2 != None:
            # update parent
            node2.parent = node1.parent

            
def  main():
    tree = BinaryTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(5)
    tree.insert(1)
    tree.insert(7)
    tree.insert(8)
    tree.insert(3)
    tree.insert(6)
    print(BinaryTree.inorder_traverse(tree.root,[]))
    print(BinaryTree.find_min(tree.root).value)
    node = tree.search(1)
    print(tree.find_successor(node).value)
    tree.delete(5)
    print(BinaryTree.inorder_traverse(tree.root,[]))
if __name__ == "__main__":
    main()


