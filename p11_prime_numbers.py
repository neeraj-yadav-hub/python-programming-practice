"""
Given a number tell if it is a prime number or not.
"""

def prime_number(number):
    count = 0
    if number in [0,1]:
        return "Not a Prime Number"
    i = 1
    while i*i <= number:
        if (number % i == 0):
            if (i == number/i):
                count = count+1
            else:
                count = count+2
        i = i+1
    if count == 2:
        return "It is a prime number"
    else:
        return "Not a Prime Number"


if __name__== "__main__":
    number = int(input("Enter number:"))
    is_prime = prime_number(number)
    print(is_prime)