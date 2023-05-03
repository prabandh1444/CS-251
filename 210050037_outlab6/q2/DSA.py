################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------
"""
Defines node in a linked list
"""
class SinglyLinkedListNode:
    def __init__(self, data):
        """
        Constructor to SinglyLinkedListNode
            :param data: Initialises the data of the node
            :type data: Any type of data
            :ivar next: pointer pointing to address of the next node in the linkedlist
            :vartype next: pointer of SinglyLinkedList
        >>> from DSA import *
        >>> a = SinglyLinkedListNode(5)
        >>> print(a.data)
        5
        >>> print(a.next)
        None
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """
        Print the Info as a string
        >>> from DSA import *
        >>> a = SinglyLinkedListNode(5)
        >>> print(a.__str__())
        5
        """
        return str(self.data)
class SinglyLinkedList:
    """
    Implementation of SinglyLinkedlist
    The list of member Functions:
        #. insert
        #. find
        #. deleteVal
        #. printer
        #. reverse
    """
    def __init__(self):
        """
        Constructor of SinglyLinkedlist
            :ivar head: pointer pointing to address of the starting node in the linkedlist
            :vartype head: pointer of SinglyLinkedList
            :ivar tail: pointer pointing to address of the ending node in the linkedlist
            :vartype tail: pointer of SinglyLinkedList
        >>> from DSA import *
        >>> a = SinglyLinkedList()
        >>> print a.head
        None
        >>> print a.tail
        None
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """ 
        Inserts the element in LInkedList
            :param data: data of the node to be inserted
            :type data: anytype
            :return: returns Nothing
        >>> from DSA import *
        >>> a = SinglyLinkedList()
        >>> a.insert(5)
        >>> a.printer()
        [5]
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """ 
        searches the element in LInkedList
            :param data: data of the node to be searched
            :type data: anytype
            :return: returns the node
            :rtype: LinkedListNode
        >>> from DSA import *
        >>> a = SinglyLinkedList()
        >>> a.insert(5)
        >>> a.insert(4)
        >>> print(a.find(4).head)
        5 
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """ 
        deletes the element in LInkedList
            :param data: data of the node to be deleted
            :type data: anytype
            :return: returns true(if its present)
            :rtype: bool
        >>> from DSA import *
        >>> a = SinglyLinkedList()
        >>> a.insert(5)
        >>> a.deleteVal(5)
        >>> a.printer()
        []
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep = ', '):
        """ 
        prints the element in LInkedList
            :return: returs Nothing
        >>> from DSA import *
        >>> a = SinglyLinkedList()
        >>> a.insert(5)
        >>> a.printer()
        [5]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """ 
        Flips the LInkedList
            :return: returs Nothing
        >>> from DSA import *
        >>> a = SinglyLinkedList()
        >>> a.insert(5)
        >>> a.insert(4)
        >>> a.reverse()
        >>> a.printer()
        [4 , 5]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------
class DoublyLinkedListNode:
    """
    Defines node in a Doubly linked list

    """
    def __init__(self, data):
        """
        Defines node in a Doubly linked list
            :param data: Initialises the data of the node
            :type data: Any type of data
            :ivar next: pointer pointing to address of the next node in the Doublylinkedlist
            :vartype next: pointer of DoublyLinkedList
            :ivar prev: pointer pointing to address of the prev node in the Doublylinkedlist
            :vartype prev: pointer of DoublyLinkedList
        >>> from DSA import *>
        >> a = DoublyLinkedListNode(5)
        >>> print(a.data)
        5
        >>> print(a.next)
        None
        >>> print(a.prev)
        None
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """
        Print the Info as a string
        >>> from DSA import *
        >>> a = DoublyLinkedListNode(5)
        >>> print(a.__str__())
        5
        """
        return str(self.data)
class DoublyLinkedList:
    """
    Implementation of DoublyLinkedlist
    The list of member Functions:
        #. insert
        #. printer
        #. reverse
    """
    def __init__(self):
        """
        Constructor of DoublyLinkedlist
            :ivar head: pointer pointing to address of the starting node in the Doublylinkedlist
            :vartype head: pointer of DoubllyLinkedList
            :ivar tail: pointer pointing to address of the ending node in the Doublylinkedlist
            :vartype tail: pointer of DoublyLinkedList
        >>> from DSA import *
        >>> a = DoublyLinkedList()
        >>> print(a.next)
        None
        >>> print(a.prev)
        None
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """ 
        Inserts the element in LInkedList
            :param data: data of the node to be inserted
            :type data: anytype
            :return: returns Nothing
        >>> from DSA import *
        >>> a = DoublyLinkedList()
        >>> a.insert(5)
        >>> a.printer()
        [5]
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """ 
        prints the element in LInkedList
            :return: returs Nothing
        >>> from DSA import *
        >>> a = DoublyLinkedList()
        >>> a.insert(5)
        >>> a.printer()
        >>> [5]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """ 
        Flips the LInkedList
            :return: returs Nothing
        >>> from DSA import *
        >>> a = DoublyLinkedList()
        >>> a.insert(5)
        >>> a.insert(4)
        >>> a.reverse()
        >>> a.printer()
        [4 , 5]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------
class BSTNode:
    """
    Defines node in a BST
    """
    def __init__(self, info):
        """
        Defines node in a BST
            :param info: Info inside the Node
            :type info: Any type of data
            :ivar left: pointer pointing to address of the left of curr Node in BST 
            :vartype left: pointer of BSTNode
            :ivar prev: pointer pointing to address of the right of curr Node in BST
            :vartype prev: pointer of BSTNode
        >>> from DSA import *
        >>> a = BSTNode(5)
        >>> print(a.info)
        5
        >>> print(a.left)
        None
        >>> print(a.right)
        None
        >>> print(a.level)
        None
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """
        Print the Info as a string
        >>> from DSA import *
        >>> a = BSTNode(5)
        >>> print(a.__str__())
        5
        """
        return str(self.info)

class BinarySearchTree:
    """
    Defines  BST
    The list of member Functions:
        #. insert
        #. traverse
        #. height
    """
    
    def __init__(self):
        """
        Constructor to BST
            :ivar root: Root of the Tree
            :vartype root: BSTNode
        >>> from DSA import *
        >>> a = BinarySearchTree()
        >>> print(a.root)
        None
        """
        self.root = None
    
    def insert(self, val):
        """ 
        Inserts the element as a Node in BST
            :param val: data of the node to be inserted
            :type val: anytype
            :return: returns Nothing
        >>> from DSA import *
        >>> a = BinarySearchTree()
        >>> a.insert(5)
        >>> a.traverse()
        5
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """ 
        Traverses through the Tree to print Info in the Nodes
            :param order: Type of Order it follows
            :type order: string
            :return: returns Nothing
        >>> from DSA import *
        >>> a = BinarySearchTree()
        >>> a.insert(5)
        >>> a.traverse()
        5
        """
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """ 
        Returns Height of the Tree
            :param root: provide the node to get height
            :type root: BST Node
            :return: returns Nothing
        >>> from DSA import *
        >>> a = BinarySearchTree()
        >>> a.insert(4)
        >>> a.insert(5)
        >>> a.height(a.root)
        1
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------
class Trie:
    """
    Implementation of ADT Trie
    The list of member Functions:
        #. insert
        #. find
        #. checkprefix
        #. countprefix
    """
    def __init__(self):
        """
        Constructor of ADT Trie
            :ivar T: Stores all strings in a set
            :vartype T: set
        >>> a = Trie()
        >>> print(a.T)
        {}
        """
        self.T = {}
    
    def find(self, root, c):
        
        return (c in root)
    
    def insert(self, s):
        """ 
        Inserts the string as a Nodes in Trie
            :param s: data of the string to be inserted
            :type s: char*
            :return: returns Nothing
            
        >>> from DSA import *
        >>> a = Trie()
        >>> a.insert('Hello World')
        >>> a.checkPrefix('Hello')
        True
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """ 
        Searches the string as a Nodes in Trie
            :param s: data of the string Which can be a Prefix of a Word in Trie
            :type s: char*
            :return: returs True when prefix is present
            :rtype: bool
        >>> from DSA import *
        >>> a = Trie()
        >>> a.insert('Hello World')
        >>> a.checkPrefix('Hello')
        True
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """ 
        Searches the occurences the string as a Nodes in Trie
            :param s: data of the string which can be prefix of a word
            :type s: char*
            :return: returns frequency
            :rtype: int
        >>> from DSA import *
        >>> a = Trie()
        >>> a.insert('Hello World')
        >>> a.insert('HelloKitty')
        >>> a.checkPrefix('Hello')
        2
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0
class Heap:
    """
    Heap is a data structure depends on priorities
            #. left
            #. right
            #. insert
            #. min
            #. heapify
            #. deleteMin
    """
    def __init__(self, cap):
        """
        Heap is a data structure depends on priorities
            :param cap: Initialises the max capacity of a given array
            :type cap: str
            :ivar H: This is an array to store
            :vartype H: list
            :ivar n: No of elements in the given heap
            :vartype n: integer
            :ivar M: Maximum capacity of given array
            :vartype M: integer
        >>> a = Heap(5)
        >>> print(a.H)
        []
        >>> print(a.n)
        0
        >>> print(a.M)
        5
        """
        self.H = []
        self.n = 0
        self.M = cap
    def parent(self, i):
        """ 
        returns the Index of parent 
            :param i: This is the level of curr Node
            :type i: int
            :return: Index of element parent of Tree
            :rtype: int
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(5)
        >>> a.insert(6)
        >>> a.parent(5)
        2
        """
        if i == 0:
            return -1
        return (i - 1) // 2
    
    def left(self, i):
        """ 
        returns the Index of parent 
            :param i: This is the level of curr Node
            :type i: int
            :return: Index of element left of Tree
            :rtype: int
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(5)
        >>> a.insert(6)
        >>> a.left(1)
        3
        """
        if ((2*i) + 1) > self.n - 1:
            return -1
        return (2 * i) + 1
    
    def right(self, i):
        """
         returns the Index of parent 
            :param i: This is the level of curr Node
            :type i: int
            :return: Index of element right of Tree
            :rtype: int
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(7)
        >>> a.insert(1)
        >>> a.right(1)
        -1
        """
        if (2*(i + 1)) > self.n - 1:
            return -1
        return 2 * (i + 1)
    
    def insert(self, val):
        """This insert function adds the given element at the end of the array and rearranges the array so that the
        array satisfies the heap properties .

           :param val: Element which should be inserted .
           :type val: int
        
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(7)
        >>> a.insert(1)
        >>> print(a.H)
        [1, 3, 7, 9]
        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
            return
        return

    
    def min(self):
        """
        Inserts the least prior element in the Heap
            :return: returns Topelement in the Heap
            :rtype: int
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(7)
        >>> a.insert(1)
        >>> print(a.min())
        1
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """ 
        Heapify the Tree at a certain Node
            :param root: Node to be Heapified
            :type root: Node
            :return: returns Nothing
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(7)
        >>> a.insert(1)
        >>> a.insert(5)
        >>> a.H[0] = 4
        >>> a.H[1] = 2
        >>> a.Heapify(0)
        >>> print(a.H)
        [2, 4, 7, 9, 5]
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """ 
        Deletes the root of the Heap
            :return: returns Nothing
        >>> from DSA import *
        >>> a = Heap(20)
        >>> a.insert(3)
        >>> a.insert(9)
        >>> a.insert(7)
        >>> a.insert(1)
        >>> a.insert(5)
        >>> a.deleteMin()
        >>> print(a.H)
        [3, 7, 9]

        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.H.pop()
                self.Heapify(0)
        return   
   