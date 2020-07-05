class TreeNode:
    def __init__(self, data):
        self.data= data
        self.children=[]
        self.parent=None
     
    def addchild(self, child):
        child.parent= self
        self.children.append(child)
        
    def showTree(self):
        prefix= " " * self.get_level() *3 + "|--"
        print(prefix + self.data )
        if self.children:
            for child in self.children:
                child.showTree()
    
    def get_level(self):
        if self.parent:
            p=self.parent
            length=0
            while p:
                length+=1
                p= p.parent
            return length
        return 0
        
    
def CreateTree():
    root= TreeNode("Cars")
    
    hyundia= TreeNode("Hyundai")
    hyundia.addchild(TreeNode("Grand I10"))
    hyundia.addchild(TreeNode("Elite I20"))
    hyundia.addchild(TreeNode("Verna"))
    hyundia.addchild(TreeNode("Creta"))
    hyundia.addchild(TreeNode("Venue"))
    
    nexa= TreeNode("Nexa")
    nexa.addchild(TreeNode("Ciaz"))
    nexa.addchild(TreeNode("Balano"))
    nexa.addchild(TreeNode("Ignis"))
    
    ford= TreeNode("Ford")
    ford.addchild(TreeNode("Aspire"))
    ford.addchild(TreeNode("Figo"))
    ford.addchild(TreeNode("Endevour"))
    
    tata= TreeNode("Tata")
    tata.addchild(TreeNode("Tiago"))
    tata.addchild(TreeNode("Altrus"))
    tata.addchild(TreeNode("Safari"))
    
    root.addchild(hyundia)
    root.addchild(nexa)
    root.addchild(ford)
    root.addchild(tata)
    
    root.showTree()
    print(root)
    return root
        
if __name__ == "__main__":
    print("---------------- Automotive Tree -------------")    
    root1= CreateTree()