"""
Given an array rotate that array K times from right to left. For example,
let array=[1,2,3,4,5] and K=3 then rotated array will be array=[3,4,5,1,2]
"""

from p8_reverse_array import reverse_array
from p9_reverse_array_within_range import reverse_array_within_range

def rotate_array(arr,ktimes):
    arr = reverse_array(arr)
    arr = reverse_array_within_range(0, ktimes - 1, arr)
    arr = reverse_array_within_range(ktimes, len(arr) - 1, arr)
    return arr

if __name__=="__main__":
    a = [1,2,3,4,5,6,7,8]
    print(rotate_array(a,4))