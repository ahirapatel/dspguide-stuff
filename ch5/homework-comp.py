#!/usr/bin/env python
import matplotlib.pyplot

"""
CHAPTER 5: LINEAR SYSTEMS

These computer exercises will help you understand "The Fundamental Concept
in DSP", as illustrated in Fig. 5-11.

1. Generate and plot the following four signals, each 500 samples long: 

a. x1[n] =  sin(2*pi*n/100)
b. x2[n] =  4*exp(-(n-150)^2/300) - exp(-(n-150)^2/2500)         
c. x3[n] =  1 for 240 < n < 300
           -2 for 299 < n < 380
            0  otherwise 
d. x4[n] =  rnd+rnd+rnd+rnd+rnd+rnd-3
            (where the function rnd returns a random number uniformly        
             distributed between 0 and 1)         
"""
from random import random as rnd
from math import sin, exp, pi

x1 = [sin(2*pi*n/100) for n in range(500)]
x2 = [4*exp(-((n-150)**2)/300) - exp(-((n-150)**2)/2500) for n in range(500)]
x3 = [1 if 240 < n < 300
        else -2 if 299 < n < 380
        else 0
        for n in range(500)]
x4 = [(rnd()+rnd()+rnd()+rnd()+rnd()+rnd()-3) for _ in range(500)]

matplotlib.pyplot.title('x1')
matplotlib.pyplot.plot(x1)
matplotlib.pyplot.show()

matplotlib.pyplot.title('x2')
matplotlib.pyplot.plot(x2)
matplotlib.pyplot.show()

matplotlib.pyplot.title('x3')
matplotlib.pyplot.plot(x3)
matplotlib.pyplot.show()

matplotlib.pyplot.title('x4')
matplotlib.pyplot.plot(x4)
matplotlib.pyplot.show()

"""
2. Generate and plot the sum of these four signals:
        
x[n] = x1[n] + x2[n] + x3[n] + x4[n]
"""
sums = [a+b+c+d for a,b,c,d in zip(x1,x2,x3,x4)]
matplotlib.pyplot.title('x1+x2+x3+x4')
matplotlib.pyplot.plot(sums)
matplotlib.pyplot.show()

"""
3. Pass each of the five signals through the linear system defined below,
creating the signals: y[n], y1[n], y2[n], y3[n] and y4[n].  Using x[n] and
y[n] as an example, the system is defined by the difference equation:        
 
      
y[n] = 0.05 x[n] + 0.95 y[n-1]
        
This can be carried out with the following program: 

y[0] = 0
for n = 1 to 499
 y[n] = 0.05*x[n] + 0.95*y[n-1]
next n
        
As will be discussed in Chapter 19, this is called a "single-pole recursive
low-pass filter."  It operates in the same way as an RC circuit in
electronics, smoothing the waveform and removing high-frequency noise.       
"""
def single_pole_recursive_low_pass(x):
    y = [0] * len(x) # List with same size as x, all elements are zeroed
    for n in range(1,500):
        y[n] = 0.05*x[n] + 0.95*y[n-1]
    return y

matplotlib.pyplot.title('x1 low passed')
matplotlib.pyplot.plot(single_pole_recursive_low_pass(x1))
matplotlib.pyplot.show()

matplotlib.pyplot.title('x2 low passed')
matplotlib.pyplot.plot(single_pole_recursive_low_pass(x2))
matplotlib.pyplot.show()

matplotlib.pyplot.title('x3 low passed')
matplotlib.pyplot.plot(single_pole_recursive_low_pass(x3))
matplotlib.pyplot.show()

matplotlib.pyplot.title('x4 low passed')
matplotlib.pyplot.plot(single_pole_recursive_low_pass(x4))
matplotlib.pyplot.show()

matplotlib.pyplot.title('x1+x2+x3+x4 low passed')
matplotlib.pyplot.plot(single_pole_recursive_low_pass(sums))
matplotlib.pyplot.show()

"""
4. Compare y[n] with the sum of y1[n], y2[n], y3[n], and y4[n]. Are they
identical?  Test this by subtracting one from the other.  Plot the result
and explain any difference between the two signals.
"""
# Differences are probably double precision float errors. Most of the differences
# are e-16 or e-15 which is nearing the edge of precision of double
y1 = single_pole_recursive_low_pass(x1)
y2 = single_pole_recursive_low_pass(x2)
y3 = single_pole_recursive_low_pass(x3)
y4 = single_pole_recursive_low_pass(x4)
sums_y = [a+b+c+d for a,b,c,d in zip(y1,y2,y3,y4)]
sums_lpf = single_pole_recursive_low_pass(sums)
diffs = [a-b for a,b in zip(sums_lpf, sums_y)]
print(diffs)
matplotlib.pyplot.title('y1+y2+y3+y4 with x1+x2+x3+x4 and differences')
matplotlib.pyplot.plot(sums_lpf)
matplotlib.pyplot.plot(sums_y)
matplotlib.pyplot.plot(diffs)
matplotlib.pyplot.show()
