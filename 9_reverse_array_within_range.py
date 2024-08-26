"""
Given an array. Given a range Start and End. Reverse the array within that range.
"""

def reverse_array_within_range(start, end, arr):
    while start<end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start+=1
            end-=1
    print(arr)
arr = [1,2,3,4,5,6,7,8,9,10]
reverse_array_within_range(5,0,arr)