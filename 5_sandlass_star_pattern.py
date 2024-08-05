"""
Program to print below sandglass pattern:
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * *
"""
no_of_stars = int(input("Enter number of stars:"))
for i in range(no_of_stars):
    for k in range(i):
        print(' ', end="")
    for j in range(no_of_stars - i):
        print('* ', end="")
    print("\n")
for l in range(no_of_stars):
    for m in range(no_of_stars-l-1):
        print(' ', end="")
    for n in range(l+1):
        print('* ', end="")
    print('\n')

    