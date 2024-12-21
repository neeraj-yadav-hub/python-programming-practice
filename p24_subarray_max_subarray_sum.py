"""
Given an array. Find the maximum subarray sum.
"""
array_list = list(map(int, input("Enter the elements:").split()))
maximum = array_list[0]
for start in range(len(array_list)):
    sum = 0
    for end in range(start,len(array_list)):
        sum = sum + array_list[end]
        maximum = max(maximum, sum)
print(maximum)