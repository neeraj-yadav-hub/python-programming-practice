"""
Given an array. Find the total sum of all the subarray.
"""
array_list = list(map(int, input("Enter the elements:").split()))
total_sum = 0
for start in range(len(array_list)):
    sum = 0
    for end in range(start, len(array_list)):
        sum = sum + array_list[end]
        total_sum = total_sum + sum
print(total_sum)