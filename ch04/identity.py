#!/usr/bin/env python3
from random import random

t = 1.0

print("Before:", t)
print("Then add random digit 1, random digit 2, subtract random digit 1, random digit 2")
for i in range(0,1000):
    a,b = random(), random()
    t += a
    t += b
    t -= a
    t -= b

print("After:", t)
