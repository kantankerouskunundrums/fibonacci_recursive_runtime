import time

# Bypass Python's internal limit on number of recursive function calls.
from functools import lru_cache

@lru_cache(maxsize=None)
def fibr(n):
    if n < 3:
        return 1
    else:
        return fibr(n-1) + fibr(n-2)

n = 40

# Time the compute duration
start = time.time() * 1000
ans = fibr(n)
delta = time.time() * 1000 - start

# Print as required
print(f"fib({n}) = {ans}")
print(f"time    = {delta} milliseconds")
