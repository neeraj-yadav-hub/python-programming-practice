"""
Program to print below pattern:
* * * * *  
* * * *  
* * *  
* *  
*
"""

no_of_stars: int = int(input("enter the number of stars:"))
for i in range(no_of_stars):
    for j in range(no_of_stars - i):
        print('* ', end="")

    for k in range (i):
        print(" ", end=" ")
    print()