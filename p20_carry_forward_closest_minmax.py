"""
Given an array find the closest min-max subarray. closest min-max subarray is the
smallest subarray which contains both min and max value of the array.
"""

def minimum_value(elements):
    minimum = elements[0]
    for i in range(1,len(elements)):
        if elements[i] < minimum:
            minimum = elements[i]
    return minimum

def maximum_value(elements):
    maximum = elements[0]
    for i in range(1,len(elements)):
        if elements[i] > maximum:
            maximum = elements[i]
    return maximum

def closest_minmax(elements, mini, maxi):
    ans = len(elements)
    min_index = -1
    max_index = -1
    if mini == maxi:
        return 1
    for i in range(len(elements)):
        if elements[i] == mini:
            min_index = i
            if max_index != -1:
                subarray_length = min_index - max_index + 1
                ans = min(ans, subarray_length)
        elif elements[i] == maxi:
            max_index = i
            if min_index != -1:
                subarray_length = max_index - min_index + 1
                ans = min(ans, subarray_length)
    return ans

if __name__=="__main__":
    elements = list(map(int,input("Enter the numbers:").split()))
    mini = minimum_value(elements)
    maxi = maximum_value(elements)
    answer = closest_minmax(elements, mini, maxi)
    print(answer)