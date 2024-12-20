"""
Given an array. Print all the subarrays that can be formed from the given array.
"""
array = list(map(int, input("Enter the array elements:").split()))
for start in range(0, len(array)):
    for end in range(start,len(array)):
        for k in range(start, end+1):
            print(array[k],end="")
        print()