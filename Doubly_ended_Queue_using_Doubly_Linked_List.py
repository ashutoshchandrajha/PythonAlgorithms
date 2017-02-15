class Empty(Exception):
    pass

class _DoublyLinkedBase():
    #Base class providing doubly linked list representation
    class _Node():
        #non public class for storing a doubly linked node
        __slots__ = '_element','_prev','_next'
        def __init__(self,element,prev,next):
            self._element=element
            self._prev=prev
            self._next=next

    def __init__(self):
        #Create an empty list
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next=self._trailer            #trailer is after header
        self._trailer._prev=self._header            #header is before trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0
        

    def _insert_between(self,e,predecessor,successor):
        #add element between two existing node and return new node
        newest = self._Node(e,predecessor,successor)    #linked to neighbors
        predecessor._next=newest
        successor._prev=newest
        self._size+=1
        return newest

    def _delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next=successor
        successor._prev=predecessor
        self._size-=1
        element = node._element                         #record deleted element
        node._prev = node._next = node._element = None  #deprecate node
        return element                                  #return deleted element

class LinkedDeque(_DoublyLinkedBase):       #Inheritance is used
    #Double ended queue implementation based on doubly linked list
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element              #real item just after header

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element             #real item before trailer

    def insert_first(self,e):
        self._insert_between(e,self._header,self._header._next)

    def insert_last(self,e):
        self._insert_between(e,self._trailer._prev,self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        self._delete_node(self._trailer._prev)
        
