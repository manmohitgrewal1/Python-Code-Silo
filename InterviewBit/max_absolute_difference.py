class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        """following code has time complexity of O(n)"""
        a=[]
        b=[]
        for i in range(len(A)):
            a.append(A[i]+i)
            b.append(A[i]-i)
        minA, maxA= min(a), max(a)
        minB, maxB= min(b), max(b)
        return max(abs(maxA - minA), abs(maxB- minB))
        
        """Following code has time complexity of O(n^2)"""
        # Sum=0
        # Max=0
        # for i in range(len(A)):
        #     for j in range(len(A)):
        #         Sum= abs(A[i]- A[j])+ abs(i-(j))
        #         if Sum> Max:
        #             Max= Sum
        # return Max