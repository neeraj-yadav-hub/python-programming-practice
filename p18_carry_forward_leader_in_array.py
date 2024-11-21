"""
Given an array find the count of leaders in the array. A leader is a element who is strictly
greater than the right side elements of the array.
"""

elements = list(map(int,input("Enter numbers:").split()))
length = len(elements)
max = elements[length - 1]
count = 1
for i in range(length - 2,-1,-1):
    if elements[i] > max:
        count = count + 1
        max = elements[i]
print(count)