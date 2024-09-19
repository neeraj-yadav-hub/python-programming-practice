"""
Program to print below star pattern:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

no_of_stars:int = int(input("Enter number of stars:"))
for i in range(no_of_stars):
    n = no_of_stars - 1 - i
    for j in range(n):
        print(" ", end=" ")
    for k in range(i+1):
        print('* ', end="")
    print()