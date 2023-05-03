
/**
 * @file DSA.h
 * @author BVSS Prabandh
 * @brief Implementation of  Different types of Abstract Data Types
 * @version 0.1
 * @date 2022-09-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include <bits/stdc++.h>
#define ll long long int
#define vi vector<int>
#define vll vector<ll>
using namespace std;

/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------
/**
 * @brief This Class implements ADT (SinglyLinkedListNode) where everynode contains pointer to next Node and data in them.
 * 
 */

class SinglyLinkedListNode {

    public:

        ll data;
        SinglyLinkedListNode* next;
        /**
         * @brief Construct a new Singly Linked List Node object
         *  
         * @param[out] data Sets data value as -1
         * @param[out] next Sets next point to NULL
         */
        SinglyLinkedListNode();
        /**
         * @brief Construct a new Singly Linked List Node object
         * 
         * @param[in] val Input given to set data
         * @param[out] data Sets value of data as val
         * @param[out] next Sets next point to NULL
         */
        SinglyLinkedListNode(ll val);

};

ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}
/**
 * @brief This Class implements ADT (SinglyLinkedList) which is chain of SinglyLinkedListNodes which is specified by head and Last Node's pointer
 *  is pointed to NULL
 * 
 *  The list of member Functions:
 *      -# insert
 *      -# find
 *      -# deleteVal
 *      -# printer
 *      -# reverse
 */
class SinglyLinkedList {

    public:
        
        SinglyLinkedListNode *head, *tail;
        /**
         * @brief Construct a new Singly Linked List object
         * @param[out] head Sets head to Nullptr
         * @param[out] tail Sets tail to Nullptr
         */
        SinglyLinkedList();
        /**
         * @brief Inserting a Node into the Chain by Adding after the Tail
         * 
         * @param[in] data Information of the new Node
         * @return Returns Nothing
         */
        void insert(ll data);
        /**
         * @brief Searches for a Node with data in the Chain
         * 
         * @param[in] data Information of Node to be Searched
         * @param[out] prev Node containg data as Information
         * @return returns adress of the node contains the given information
         */
        SinglyLinkedListNode* find(ll data);
        /**
         * @brief Searches For Node with data and Deletes it from chain
         * 
         * @param[in] data Information of Node to be Deleted
         * @return true(if the Node is present in the Chain)
         * @return false (If the Node isnt Present in the Chain)
         */
        bool deleteVal(ll data);
        /**
         * @brief Function to Print SinglyLinked lists
         * 
         * @param[out] sep Prints the SinglyLinked list (as list in Python)
         * @return Returns Nothing
         */
        void printer(string sep);
        /**
         * @brief Revers The Singlylinked List
         *
         *@return Returns Nothing 
         */
        void printer();
        void reverse();
        };
SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2);

// ------------------------------- Doubly Linked List -----------------------------
/**
 * @brief This Class implements ADT (DoublyLinkedListNode) where everynode contains pointers to next Node and previous data, Info in them.
 * 
 * The list of member Functions:
 *      -# insert
 *      -# printer
 *      -# reverse
 */
class DoublyLinkedListNode {

    public:
        
        ll data;
        DoublyLinkedListNode *next, *prev;
        /**
         * @brief Construct a new Doubly Linked List Node object
         * @param[out] data Data is set as -1
         * @param[out] next Next is set as NULL
         * @param[out] prev Previous is set as NUll
         */
        DoublyLinkedListNode();
        /**
         * @brief Construct a new Doubly Linked List Node object
         * 
         * @param[in] val Sets value of head as Val
         * @param[out] next Next is set as NULL
         * @param[out] prev Previous is set as NUll
         */
        DoublyLinkedListNode(ll val);

};

ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}
/**
 * @brief This Class implements ADT (DoublyLinkedList) which is chain of DoublyLinkedListNodes which is specified by head and Last Node's next pointer
 *  is pointed to NULL and Head Node's previous pointer is pointed to NULL
 * 
 */
class DoublyLinkedList {

    public:
        
        DoublyLinkedListNode *head, *tail;
        /**
         * @brief Construct a new Doubly Linked List object
         * @param[out] head Sets head to nullptr
         * @param[out] tail Sets tail to nullptr
         */
        DoublyLinkedList();
        /**
         * @brief Inserting a Node into the Chain by Adding after the Tail
         * 
         * @param[in] data Information of the new Node
         * @return Returns Nothing
         */
        void insert(ll data);
        /**
         * @brief Function to Print DoublyLinked lists
         * 
         * @param[out] sep Prints the DoublyLinked list (as list in Python)
         * @return Returns Nothing
         */
        void printer(string sep);
        void printer();
        /**
         * @brief Revers The linked List
         *
         *@return Returns Nothing 
         */
        void reverse ();

};

// ------------------------------- Binary Search Tree -----------------------------
/**
 * @brief BSTNode contain data,height and threepoints containing parent,leftchild and rightchild.
 * 
 */
class BSTNode {

    public:

        ll info, level;
        BSTNode *left, *right;
    /**
     * @brief Construct a new BSTNode object
     * 
     * @param val Info in Head
     * @param[out] level Sets level as zero
     * @param[out] info  Sets info as val
     * @param[out] left  Sets left as nullptr
     * @param[out] right Sets right as nullptr
     */
        BSTNode(ll val);

};

ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}
/**
 * @brief BinarySearchTree is an ADT (A map of BSTnodes) where every BSTNode has atmost Two children.
 * 
 * The list of memeber functions are:
 *   -# insert
 *   -# traverse
 *   -# height
 */
class BinarySearchTree {

    public:
        
        BSTNode *root;
        
        enum order {PRE, IN, POST};
        /**
         * @brief Construct a new Binary Search Tree object
         * @param[out] root Set root as nullptr
         */
        BinarySearchTree();
        /**
         * @brief Insert new Node in the Tree
         * 
         * @param val Info of the New Leaf
         * @return Returns Nothing
         */
        void insert(ll val);
        /**
         * @brief Traverse The Tree in desired maner
         * 
         * @param T Tree
         * @param tt Choice of Traverse
         * @return Returns Nothing
         */
        void traverse (BSTNode* T, order tt);
        /**
         * @brief Returns the Height of BST
         * 
         * @param T Tree
         * @return ll(Height of Tree)
         */
        ll height(BSTNode *T);
};

// ------------------------------- Suffix Trie -----------------------------
/**
 * @brief A Trie is a DataType which stores a collection of Strings in Lexographic order,i.e, all paths from root to leaves(from left to right) gives strings in
 * lexographic order
 *  
 * member functions are :
 *    -# find
 *    -# insert
 *    -# checkprefix
 *    -# countprefix
 */
class Trie {

    public:
        
        ll count;
        map<char,Trie*> nodes;
        /**
         * @brief Construct a new Trie object
         * @param[out] count Set count as zero
         * @param[out] nodes New paths created 
         */
        Trie ();
        /**
         * @brief Find a specified string in Tree
         * 
         * @param T TREE
         * @param c string required to find
         * @return true (if string is found)
         * @return false (if string isnt found)
         */
        bool find(Trie* T, char c);
        /**
         * @brief Insert string in a Trie
         * 
         * @param s string to be inserted
         * @return Returns Nothing
         */
        void insert(string s);
        /**
         * @brief Check all prefixs of string in the Trie
         * 
         * @param s String whose prefixs to be searched
         * @return true(If such a prefix is found) 
         * @return false (If no such Prefix is found)
         */
        bool checkPrefix(string s);
        /**
         * @brief Count number of Prefixes of s in Trie
         * 
         * @param s String whose prefixes to be Searched
         * @return ll(Number of prefixes present)
         */
        ll countPrefix(string s);

};