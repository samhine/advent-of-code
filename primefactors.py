import math
from datetime import datetime
start=datetime.now()

n = 600851475143

def find_factors(k):
    facs = []
    for i in range(2,math.floor(math.sqrt(k))):
        if k%i==0:
            facs.append(i)
            facs.append(k//i)

    return facs

def is_prime(k):
    for i in range(2,math.floor(math.sqrt(k))):
        if k%i==0:
            return False
    return True


for num in find_factors(n):
    if is_prime(num):
        print(num)

print((datetime.now()-start).total_seconds())