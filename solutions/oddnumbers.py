# 1/6/2021 DUSO Team Problem #3

import math
print("Starting Up")

num = 14
n = math.factorial(num)
count = 0
print(F"Calclating odd factors for {n}.")

for x in range(1, int(n**0.5)+1): # Goes through every number between 1 & the square root of n + 1.
  if n % x == 0: # if n / x (will be every number above) has a remainder of 0, continue
    if(x % 2 == 1): # if x divided by 2 has a reminder of 1, that means its odd, add to the count.
      count += 1
    if(n/x)%2==1): # If n/x is odd, add to the count.
      count += 1

print("\n\n")
print("Answer:" + str(count))
