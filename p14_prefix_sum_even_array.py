"""
Given N array elements. Create a prefix even odd array. A prefix even odd array is an array of
sum of even indexes of an array.
"""

def create_even_prefix_sum(given_array):
    prefix_sum = [None]*len(given_array)
    for i in range(0,len(given_array)):
        if i == 0:
            prefix_sum[i] = given_array[i]
        elif i%2 == 0:
            prefix_sum[i] = prefix_sum[i - 1] + given_array[i]
        else:
            prefix_sum[i] = prefix_sum[i-1]
    return prefix_sum

if __name__ == "__main__":
    l = list(map(int, input("Enter list of numbers:").split()))
    sum = create_even_prefix_sum(l)
    print(sum)
        