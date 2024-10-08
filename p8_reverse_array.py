"""
Reverse a given array. Space complexity(1). Hence change the original array.
"""

def reverse_array(arr):
    j = len(arr) - 1
    for i in range(len(arr)):
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1
    return arr

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    reverse = reverse_array(arr)
    print(reverse)