import time
import math

def fibr(n):
    if n <3:
        return 1
    else:
        return fibr(n-1) + fibr(n-2)

n = 40
start = time.time() * 1000
print(f"fib({n}) = {fibr(n)}")
end = time.time() * 1000

print(f"time    = {end-start} milliseconds")