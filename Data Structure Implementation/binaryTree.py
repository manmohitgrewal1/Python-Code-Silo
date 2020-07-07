class BinaryTree:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None
        
    def add(self, data):
        # go right
        if data > self.data:
            # Check if the child exist 
            if self.right:
                self.right.add(data)
            # Create a BinaryTree Node if child does not exist
            else:
                tmp= BinaryTree(data)
                self.right= tmp
                
         # go left
        if data < self.data:
            # check if the child exist
            if self.left:
                self.left.add(data)
                
            # Create a BinaryTree Node if the child does not exist
            else:
                tmp= BinaryTree(data)
                self.left= tmp
    
    def showSorted(self):
        element=[]
        if self.left:
            element+=self.left.showSorted()
        element.append(self.data)
        if self.right:
            element+=self.right.showSorted()
            
        return element
    
    
if __name__ == "__main__":
    root= BinaryTree("Manmohit")
    arr= [15,12,17,4,48,56,11,2,90]
    for run in arr:
        root.add(run)
    sortedBTree=root.showSorted()
    print(len(arr), len(sortedBTree))
    print(sortedBTree)
