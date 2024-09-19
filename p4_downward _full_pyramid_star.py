"""
program to print below pattern:
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""

no_of_stars: int = int(input("Enter the number of stars:"))
for i in range(no_of_stars):
    for k in range(i):
        print(" ", end="")

    for j in range(no_of_stars-i):
        print("* ", end="")
    print()
