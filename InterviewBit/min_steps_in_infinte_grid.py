class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        dist= 0
        temp=[]
        if len(A)<=1 or len(B)<=1:
            return 0
        for run in range(len(A)-1):
            # print(run)
            cord1= MinSteps(A[run], B[run]) 
            cord2=MinSteps(A[run+1] ,B[run+1])
            dist= dist+ cord2.find(cord1) 
        return dist
class MinSteps:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def find(self, coords):
        return max(abs(self.x - coords.x), abs(self.y- coords.y))