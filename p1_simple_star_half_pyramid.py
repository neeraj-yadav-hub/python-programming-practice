"""
Program to print half pyramid like below:
* 
* * 
* * * 
* * * * 
* * * * *
"""
import time
no_of_star:int = int(input("Enter the number of stars:"))
for i in range(no_of_star):
    for j in range(i+1):
        print("* ", end="")
    print()