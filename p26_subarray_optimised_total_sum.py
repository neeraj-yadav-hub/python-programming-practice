"""
Given an array. Find the total sum of subarrays in O(N).
"""
array_list = list(map(int, input("Enter the numbers:").split()))
total_sum = 0
for i in range(len(array_list)):
    left = i + 1
    right = len(array_list) - i
    count = left * right
    total_sum = total_sum + count * array_list[i]
print(total_sum)
