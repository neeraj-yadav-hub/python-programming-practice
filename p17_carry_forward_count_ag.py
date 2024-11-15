"""
count the pair of 'ag' in the array such that i < j & s[i] = 'a' & s[j] = 'g'
"""

elements = input("Enter characters:").split()
answer = 0
count = 0
for i in elements:
    if i == 'a':
        count = count + 1
    elif i == 'g':
        answer = answer + count
print(answer)