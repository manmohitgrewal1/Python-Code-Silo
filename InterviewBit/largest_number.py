# Merge Sort Algorithm 
def LargestNum(array):
    string=""
    if len(array) <2:
        return str(array[0])
    if len(array)==0:
        return string
           
    result= MergeSort(array)
    for run in result:
        string+=str(run)
    return string
    
def MergeSort(array):
    """
    Para: List on which Merge sort will be done
    return: This function will return sorted list
    The function will split the list and call itself 
    until length of the list is 1.
    """
    if len(array)< 2:
        return array
    median= len(array)//2
    left=MergeSort(array[:median])
    right=MergeSort(array[median:])
    result= Merge(left, right)
    return result
    
def Merge(left, right):
    """ 
    Para: Two lists
    Return: Sorted array in which element are arranged in a way that 
    they  form the largest number.
    """
    left_pointer=0
    right_pointer=0
    current=0
    result=[]
    while left_pointer < len(left) and right_pointer< len(right):
        num_l= str(left[left_pointer]) + str(right[right_pointer]) 
        num_r= str(right[right_pointer]) + str(left[left_pointer])
        if num_r > num_l:
            result.append(right[right_pointer])
            right_pointer+=1
        else:
            result.append(left[left_pointer])
            left_pointer+=1
        current+=1
    while left_pointer < len(left):
        result.append(left[left_pointer])
        left_pointer+=1
        current+=1
    while right_pointer< len(right):
        result.append(right[right_pointer])
        right_pointer+=1
        current+=1
    return result



# Simple Sort Algotithm 
def GetLargest(array):
    if len(array)== 0:
        return ""
    if len(array)==1:
        return toString(array)
    for i in range(0, len(array)):
        j=i+1
        while j!= len(array):
            ab= str(array[i]) + str(array[j])
            ba= str(array[j]) +str(array[i])
            if ba> ab:
                val= array[i]
                array[i]= array[j]
                array[j]= val
            j+=1 
    string=toString(array)
    if int(string)== 0:
        return "0"
    return string

def toString(array):
    string= ""
    for run in array:
        string+=str(run)
    return string




if __name__ == "__main__":
    arr= [ 82,5,68,37,2,9,98,1 ]
    # Get largest number with simple sorting
    print(GetLargest(arr))
    
    # Get largest number with Merge sort algorithm
    print(LargestNum(arr))