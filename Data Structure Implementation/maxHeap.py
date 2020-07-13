import sys
class MaxHeap:
    def __init__(self, heapsize):
        self.heapsize= heapsize
        self.heap=[0] * (heapsize +1) 
        self.heap[0]= sys.maxsize
        self.size= 0
        self.front= 1
        # self.trans= self.front
        
    def _parent(self, index):
        return index//2 
        
    def _right(self, index):
        return (2 * index) + 1
    
    def _left(self, index):
        return (2 * index) 
        
    def _swap(self, childPos, parentPos):
        self.heap[childPos], self.heap[parentPos]= self.heap[parentPos], self.heap[childPos]
        
    def push(self, data):
        self.size+= 1
        self.heap[self.size]= data
        current= self.size
        # print("current value= {} value of parent= {}".format( self.heap[current], self.heap[self._parent(current)]))
        while self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current= self._parent(current)
    
    def pop(self):
        print("!!!!!!!!!!!! POPED {} from the max heap !!!!!!!!!!!!".format(self.heap[self.front]))
        print("New Max Heap:-")
        self.heap[self.front]= self.heap[-1]
        del self.heap[-1]
        self._restoreHeap(self.front)
        
        
    def _restoreHeap(self, frontIndex):
        if not self._isLeaf(frontIndex):
            if (self.heap[self._left(frontIndex)] > self.heap[self._right(frontIndex)]) and self.heap[frontIndex] < self.heap[self._left(frontIndex)]:
                self._swap(frontIndex, self._left(frontIndex))
                frontIndex= self._left(frontIndex)
                self._restoreHeap(frontIndex)
            elif self.heap[self._left(frontIndex)] < self.heap[self._right(frontIndex)] and self.heap[frontIndex] < self.heap[self._right(frontIndex)]:
                self._swap(frontIndex, self._right(frontIndex))
                frontIndex= self._right(frontIndex)
                self._restoreHeap(frontIndex)
    
    def _isLeaf(self, index):
        if self._right(index) <= len(self.heap) or self._left(index) <= len(self.heap):
            return False
        return True
        
    def show(self):
        # print(self.heap)
        for run in range(1, len(self.heap)//2):
            print("Parent: {} has Left child: {} and Right child= {}".format(self.heap[run], self.heap[self._left(run)], self.heap[self._right(run)]))
        print("--------------------------------- END OF SHOW METHOD --------------------------------- ")

class Helper:
    def __init__(self, array):
        self.array= array
        self.root= MaxHeap(len(array))
    
    def createHeap(self):
        for run in self.array:
            self.root.push(run)
            
    def remove(self):
        self.root.pop()
    
    def Print(self):
        self.root.show()
        
if __name__== "__main__":
    arr= [15,5,3,17,10,84,19,6,22,9]
    loader= Helper(arr)
    loader.createHeap()
    loader.Print()
    loader.remove()
    loader.Print()