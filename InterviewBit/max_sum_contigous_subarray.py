class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==1:
            return A[0]
        return FindMaxSum(A)
        

    
def FindMaxSum(arr):
    Sum= arr[0]
    total=0
    for run in arr:
        total+=run
        if total>Sum:
            Sum= total
        if total<0:
            total=0
    return Sum
        