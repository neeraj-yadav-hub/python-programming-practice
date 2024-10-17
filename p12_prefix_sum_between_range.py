"""
Given N array elements and  Q queries for the same array. For each query
calculate sum of elements in the given range [L-R] & [L<=R]
"""

def create_prefix_sum(given_array):
    prefix_sum = [None]*len(given_array)
    for i in range(0,len(given_array)):
        if i == 0:
            prefix_sum[i] = given_array[i]
        else:
            prefix_sum[i] = prefix_sum[i - 1] + given_array[i]
    return prefix_sum

def calculate_sum_between_range(list_of_elements, left_range, right_range):
    pf_sum = create_prefix_sum(list_of_elements)
    if left_range == 0:
        return pf_sum[right]
    else:
        return pf_sum[right_range] - pf_sum[left_range - 1]
        
if __name__ == "__main__":
    l = list(map(int, input("Enter list of numbers:").split()))
    q = int(input("Enter the no. of queries:"))
    for i in range(q):
        left ,right = map(int ,(input("Enter left & right range:").split()))
        if left <= right:
            sum = calculate_sum_between_range(l ,left ,right)
            print(sum)
        else:
            print("left range should be smaller than right")