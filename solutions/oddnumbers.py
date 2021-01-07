# 1/6/2021 DUSO Team Problem #3


import math
print(".run")

num = 14
n = math.factorial(num)
count = 0
print(n)

for x in range(1, int(n**0.5)+1):
  if n % x == 0:
    if(x % 2 == 1):
      count += 1
    if(n % x == 0 and (n/x)%2==1):
      count += 1

print("\n\n")
print("answer:" + str(count))
