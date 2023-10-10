import math
import sys
# Find The greatest common divisor of multiple numbers read from the console.

def gcdofarray(arr, idx):
    if idx == len(arr)-1:
        return arr[idx]
        
    a = arr[idx]
    b = gcdofarray(arr, idx+1)
      
    return math.gcd(a, b)


arr = sys.argv[1].split(',')
arr = [int(num) for num in arr]  # Convert string elements to integers
print(gcdofarray(arr, 0))
