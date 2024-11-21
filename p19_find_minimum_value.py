"""
Given an array find the minimum value in that array.
"""

elements = list(map(int,input("Enter numbers:").split()))
minimum = elements[0]
for i in range(1,len(elements)):
    if elements[i] < minimum:
        minimum = elements[i]
print(minimum)