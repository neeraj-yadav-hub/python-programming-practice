"""
Given N array elements, count number of elements having atleast 1 or more numbers greater
then itself. (DON'T USE EXTERNAL LIBRARIES)
"""
elements = list(map(int,input("Enter number of elements:").split()))
print(elements)
max = elements[0]
count = 0
for i in range(len(elements)):
    if elements[i] > max:
        max = elements[i]
        count+=1
    elif elements[i] < max:
        count+=1

print(f"No. of elements having number greater then itself:{count}") 
