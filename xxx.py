# Good morning, Dr. Chandra. This is Hal. I am ready for my first lesson.

import re
WORD_RE = re.compile(r'\W*(\w*)\W*')

class Heap(object):
    ''' This is an unordered array representation in that while the top item 
        is always the min or max value (as determined by the constructor), the
        subsequent entries are NOT guarenteed to be in that order. As each item
        is removed from the top, the tree is reordered just enough to place the
        next entry on top.
    '''
    def __init__(self, max=False, comparator=None):
        self.__heap = []
        self.__maxQ = max
        self.__comparator = comparator if comparator else None
        
    def copy(self):
        copy = Heap()
        copy.__heap = self.__heap.copy()
        copy.__maxQ = self.__maxQ
        copy.__comparator = self.__comparator
        return copy

    def size(self):
        ''' the number of items in the heap '''
        return len(self.__heap)

    def __pop(self):
        ''' removes an item from the end of heap storage; frees space '''
        return self.__heap.pop()
    
    def __push(self, val):
        ''' appends an item to the end of heap storage; allocates space '''
        self.__heap.append(val)
    
    def __get(self, i):
        ''' provide 1 based array access '''
        return self.__heap[i-1]

    def __put(self, i, val):
        ''' provide 1 based array storage '''
        self.__heap[i-1] = val
        
    def __less(self, i, j):
        a = self.__get(i)
        b = self.__get(j)
        if self.__comparator:
            return self.__comparator(a, b)
        else:
            return a > b if self.__maxQ else a < b
        
    def __swap(self, i, j):
        a = self.__get(i)
        b = self.__get(j)
        self.__put(i, b)
        self.__put(j, a)
        
    def __swim(self, k):
        ''' swap the item up the heap to its natural location '''
        while k > 1 and self.__less(k, k // 2):
            self.__swap(k, k // 2);
            k = k // 2;

    def __sink(self, j):
        ''' swap the item down into the heap '''
        N = self.size()
        while 2*j <= N:
            k = 2*j
            # Compare to the right node if it's smaller and present.
            if k < N and self.__less(k+1, k): k += 1
            if self.__less(j, k): break
            self.__swap(j, k)
            j = k
            
    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.__get(1)
    
    def remove(self):
        ''' Return the top item from the heap '''
        result = self.peek()
        endval = self.__pop()
        N =  N = self.size()
        if N > 0:
            self.__put(1, endval)
            if N > 1: self.__sink(1)
        return result

    def insert(self, val):
        ''' Insert a value into heap '''
        self.__push(val)
        N =  N = self.size()
        self.__swim(N)
        return self # chaining support.
    
    def load(self, alist):
        for x in alist: self.insert(x)
        return self # chaining support.

    def load_word(self, raw_word):
        lword = raw_word.lower()
        m = WORD_RE.match(lword)
        #log('- Match "{0}" for {1}', lword, m)
        word = m.group(1)       
        if len(word):
            #log('- Insert "{0}"', word)
            self.insert(word)
        return self # chaining support.
    
    def load_words(self, *sentences):        
        for sentence in sentences:
            for word in sentence.split():
                self.load_word(word)
        return self # chaining support.
    
    def consume(self, preserve=False):
        ''' Iterate and consume all the items in order '''
        if preserve: self = self.copy()
        while not self.is_empty(): yield self.pop()

    def __iter__(self):
        ''' Iterate all the items, but not necessarily in order '''
        return iter(self.__heap)
        
    def __repr__(self):
        return str([x for x in self])

    __str__ = __repr__
    pop = remove # Convenient and often expected.
    
#-----------------------------------------------------------------------------
