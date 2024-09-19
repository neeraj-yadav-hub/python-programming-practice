"""
program to print diamond shaped star pattern:
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
"""
no_of_stars:int = int ( input ('Enter number of stars:') )
for i in range(no_of_stars):
    for k in range(no_of_stars-i-1):
        print(' ', end="")
    for j in range(i+1):
        print('* ', end="")
    print()

for l in range(no_of_stars-1):
    for m in range(l+1):
        print(' ', end="")
    for n in range(no_of_stars-1-l):
        print('* ', end="")
    print()