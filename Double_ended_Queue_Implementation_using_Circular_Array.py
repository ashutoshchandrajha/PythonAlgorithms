class Empty(Exception):
    pass

class ArrayDeque():
    #Queue Implementation with adding and removing avilable at both front and back
    DEFAULT_CAPACITY = 10                       #moderate capacity for all new queues

    def __int__(self):
        self._data = [None]* ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0                         #stores index of the first element

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return (self._front+self._size-1)%len(self._data)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front]==None           #garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0<self._size<len(self._data)//4:
            self.resize(len(self._data)//2)
        return answer

    def add_last(self,e):
        #add element to the back of the queue
        if self._size == len(self._data):
            self.resize(2*len(self._data))      #double the array size
        a = (self._front + self._size) % len(self._data)
        self._data[a] = e
        self._size += 1

    def add_first(self,e):
        #add element to the front of the queue
        if self._size == len(self._data):
            self.resize(2*len(self._data))      #double the array size
        self._front = (self._front-1)%len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_last(self):
        #delete element from the end of the queue
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front+self._size-1)%len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -=1
        if 0<self._size<len(self._data)//4:
            self.resize(len(self._data))//2
        return answer

    def resize(self,capacity):
        #Resize to new list of capcacity >= len(self)
        old = self._data
        self._data = [None]*capacity
        walk = self._front
        for k in range(self._size):             #only consider existing elements
            self._data[k] = old[walk]           #intentionally shift indices
            walk = (1+walk)%len(old)            #use old size as modulus
        self._front = 0
