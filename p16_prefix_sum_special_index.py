"""
Given an N array elements. Find the count of special index. A index
is said to be special index if after deleting it the sum of even indexes
is equal to sum of odd indexes.
"""
from p14_prefix_sum_even_array import create_even_prefix_sum
from p15_prefix_sum_odd_array import create_odd_prefix_sum

def special_index(pfeven, pfodd):
    n = len(pfeven)
    special_index_count = 0
    for i in range(n):
        if i == 0:
            sum_even = pfodd[n-1] - pfodd[i]
            sum_odd = pfeven[n-1] - pfeven[i]
        else:
            sum_even = pfeven[i-1] + pfodd[n-1] - pfodd[i]
            sum_odd = pfodd[i-1] + pfeven[n-1] - pfeven[i]
        if sum_even == sum_odd:
            special_index_count = special_index_count + 1
        print("sum even:",sum_even)
        print("sum_odd:",sum_odd)
        print("special index count:",special_index_count)
    return special_index_count

if __name__=="__main__":
    elements = list(map(int, input("Enter array elements:").split()))
    pfeven = create_even_prefix_sum(elements)
    pfodd = create_odd_prefix_sum(elements)
    print(pfeven,pfodd,sep='\n')
    count = special_index(pfeven, pfodd)
    print(count)