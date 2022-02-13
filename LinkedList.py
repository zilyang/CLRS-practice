# Chapter 10.2
# Implement a double linked list with sentinel with search, insert, and delete functions.

# Node class
class Node:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.prev = self.nil
        self.nil.next = self.nil
    
    def __str__(self):
        x = self.nil.next
        string = ""
        while x != self.nil:
            #print(x.key)
            string += " -> "+str(x.key)
            x = x.next
        return string

    # Find node with key x in linked list and return it
    def search(self,k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        if x == self.nil:
            print("List does not contain node with key ", k)
            return None
        return x

    # Insert node with key k into the head of the list
    def insert(self,k):
        print("insert ", k)
        # initialize new node with key k
        new = Node(k)
        # insert new to head
        new.next = self.nil.next
        new.prev = self.nil
        # break old links
        self.nil.next = new
        new.next.prev = new

    # Delete node with key k from list
    def delete(self,k):
        print("delete ", k)
        # Find node with key k
        x = self.search(k)
        if x == None:
            return
        #  Break links
        x.prev.next = x.next
        x.next.prev = x.prev

def main():
    List = LinkedList()
    List.insert(1)
    List.insert(2)
    List.insert(3)
    print("After inserting 1, 2, 3 list is: ")
    print(List)
    List.delete(2)
    print("After deleting 2 list is: ")
    print(List)
    List.delete(4)
    print("After deleting non existing key, list is: ")
    print(List)
    List.delete(1)
    print(List)
    List.delete(3)
    print(List)

if __name__=="__main__":
    main()

