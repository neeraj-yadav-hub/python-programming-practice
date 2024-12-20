"""
Given an array. Print the sum of all the subarray that can be formed using the given array.
"""
array = list(map(int, input("Enter the array elements:").split()))
for start in range(0, len(array)):
    for end in range(start,len(array)):
        sum = 0
        for k in range(start, end+1):
            sum = sum + array[k]
        print(sum)