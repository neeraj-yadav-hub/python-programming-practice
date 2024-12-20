"""
Given an array. Print the sum of all the subarray using prefix sum.
"""
def prefixsum(full_array):
    pfsum=[None]*len(full_array)
    for i in range(len(full_array)):
        if i == 0:
            pfsum[i] = full_array[i]
        else:
            pfsum[i] = pfsum[i-1] + full_array[i]
    return pfsum

array_list = list(map(int, input("Enter the elements:").split()))
pfsum = prefixsum(array_list)
for start in range(len(array_list)):
    for end in range(start, len(array_list)):
        if start == 0:
            print(pfsum[end])
        else:
            print(pfsum[end] - pfsum[start-1])