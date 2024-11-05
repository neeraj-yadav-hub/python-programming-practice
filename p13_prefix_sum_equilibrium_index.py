"""
Given an array find the count of equilibrium index in that array. Equilibrium index is the 
index in which the sum of elements before the index and sum of elements after 
the index are equal.
"""

from p12_prefix_sum_between_range import create_prefix_sum

def count_equilibrium_index(list_of_elements):
    equilibrium_count = 0
    length = len(list_of_elements)
    for i in range(len(list_of_elements)): 
        if i == 0:
            left = 0
            right = list_of_elements[length - 1] - list_of_elements[i]
        else:
            left = list_of_elements[i-1]
            right =  list_of_elements[length - 1] - list_of_elements[i]
        if left == right:
            equilibrium_count = equilibrium_count + 1
    return equilibrium_count

if __name__=="__main__":
    elements = list(map(int,input("Enter the array elements:").split()))
    #example elements list, elements=[3,-1,2,-1,1,2,1]
    prefix_array = create_prefix_sum(elements)
    count = count_equilibrium_index(prefix_array)
    print(count)