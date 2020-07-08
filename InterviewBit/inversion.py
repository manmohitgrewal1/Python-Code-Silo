def findInversions(array):
    if len(array)< 2:
        return 0
    print(mergeSort(array))

def mergeSort(array):
    if len(array)<2:
        return 0
    result=0
    median= len(array)//2
    left= array[:median] 
    right= array[median:]
    result+=mergeSort(left)
    result+=mergeSort(right)
    result+= merge(left, right, array)
    return result
    
def merge(left, right, main):
    left_pointer=0
    right_pointer=0
    num_of_inversions=0
    current=0
   
    while left_pointer< len(left) and right_pointer< len(right):
        if left[left_pointer]> right[right_pointer]:
            main[current]=right[right_pointer]
            if left_pointer < len(left):
                x= len(left)- left_pointer
                num_of_inversions+=x
            else:
                num_of_inversions+=1
            
            right_pointer+=1
        else:
            main[current]=left[left_pointer]
            left_pointer+=1
        current+=1
    while left_pointer< len(left):
        main[current]=left[left_pointer]
        left_pointer+=1
        current+=1

    while right_pointer < len(right):
        main[current]=right[right_pointer]
        right_pointer+=1
        current+=1
    return num_of_inversions
    
if __name__ == "__main__":
    arr= [2, 3, 4]
    findInversions(arr)