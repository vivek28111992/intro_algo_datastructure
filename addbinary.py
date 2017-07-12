"""
Complexity: O()
"""
from array import *

def addbinary(a, b):
    n = len(a)
    ar = list(reversed(a))
    br = list(reversed(b))
    carry = 0
    c = []
    for i in range(0, n):
        c.append(int((ar[i] + br[i] + carry) % 2))
        carry = (ar[i] + br[i] + carry) / 2
        print(c)
    c.append(int(carry))

    return list(reversed(c))


print(addbinary([1, 1, 0], [1, 1, 1]))
