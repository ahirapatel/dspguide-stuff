#!/usr/bin/env python
import matplotlib.pyplot

#matplotlib.pyplot.plot(t, x, marker='.')
#matplotlib.pyplot.title('256 samples of 3 periods')
#matplotlib.pyplot.xlabel('time')
#matplotlib.pyplot.ylabel("Signal Amplitude")
#matplotlib.pyplot.show()

"""
CHAPTER 5: LINEAR SYSTEMS

1. Two discrete waveforms, x[n] and y[n], are each eight samples long, given
by:

    x[n]:   1, 2, 3, 4,-4,-3,-2,-1  
    y[n]:   0,-1, 0, 1, 0,-1, 0, 1
            
For this problem, you can add additional samples with a value of zero on
either side of the signals, as needed.  Calculate, sketch and label the
following signals: 
"""

x = [1, 2, 3, 4,-4,-3,-2,-1]
y = [0,-1, 0, 1, 0,-1, 0, 1]


"""
a. x[n]
"""
matplotlib.pyplot.title('x[n]')
matplotlib.pyplot.plot(x)
matplotlib.pyplot.show()

"""
b. y[n]
"""
matplotlib.pyplot.title('y[n]')
matplotlib.pyplot.plot(y)
matplotlib.pyplot.show()
"""
c. 5x[n]
"""
matplotlib.pyplot.title('5x[n]')
matplotlib.pyplot.plot([5 * val for val in x])
matplotlib.pyplot.show()
"""
d. -7y[n]    
"""
matplotlib.pyplot.title('-7y[n]')
matplotlib.pyplot.plot([-7 * val for val in y])
matplotlib.pyplot.show()
"""
e. x[n-3]
"""
matplotlib.pyplot.title('x[n-3]')
matplotlib.pyplot.plot([valx for valx in ([0]*3)+x[:-3]])
matplotlib.pyplot.show()
"""
f. y[n+1]
"""
matplotlib.pyplot.title('y[n+1]')
matplotlib.pyplot.plot([valy for valy in y[1:]+[0]])
matplotlib.pyplot.show()
"""
g. 2x[n+1]
"""
matplotlib.pyplot.title('2x[n+1]')
matplotlib.pyplot.plot([2*valx for valx in x[1:]+[0]])
matplotlib.pyplot.show()
"""
h. -y[n-1]
"""
matplotlib.pyplot.title('-y[n-1]')
matplotlib.pyplot.plot([-valy for valy in [0]+y[:-1]])
matplotlib.pyplot.show()

"""
i. x[n] + y[n] 
"""
matplotlib.pyplot.title('x[n] + y[n]')
matplotlib.pyplot.plot([valx + valy for valx,valy in zip(x,y)])
matplotlib.pyplot.show()
"""
j. -2x[n-1] + 3y[n+2]
"""
newx = [-2*valx for valx in [0]+x[:-1]]
newy = [3*valy for valy in y[2:]+([0]*2)]
totals = [valx + valy for valx,valy in zip(newx,newy)]
matplotlib.pyplot.title('-2x[n-1] + 3y[n+2]')
matplotlib.pyplot.plot(totals)
matplotlib.pyplot.show()
"""
k. 3x[n+2] - 2y[n+2]
"""
newx = [3*valx for valx in x[2:]+([0]*2) ]
newy = [2*valy for valy in y[2:]+([0]*2)]
totals = [valx - valy for valx,valy in zip(newx,newy)]
matplotlib.pyplot.title('3x[n+2] - 2y[n+2]')
matplotlib.pyplot.plot(totals)
matplotlib.pyplot.show()
"""
l. x[n] + x[n-2]
"""
newx = [valx for valx in ([0]*2)+x[:-2]]
totals = [valx + valx2 for valx,valx2 in zip(x,newx)]
matplotlib.pyplot.title('x[n] + x[n-2]')
matplotlib.pyplot.plot(totals)
matplotlib.pyplot.show()
"""
m. 2x[n] -3x[n-2] + 3y[n+1]
"""
first = [2*valx for valx in x]
second = [3*valx for valx in ([0]*2)+x[:-2]]
third = [3*valy for valy in y[1:]+[0]]
totals = [a-b+c for a,b,c in zip(first,second,third)]
matplotlib.pyplot.title('2x[n] - 3x[n-2] + 3y[n+1]')
matplotlib.pyplot.plot(totals)
matplotlib.pyplot.show()

"""
2. Sketch the following discrete signals for -8 < n < 8:

    a. x[n] = sin(2 pi n / 8)
    b. x[n] = cos(2 pi n / 4)
    c. x[n] = sin(2 pi n / 2)
    d. x[n] = cos(2 pi n / 2)
    e. x[n] = n-3 if n > 2, 0 otherwise
    f. x[n] = 1 if n < -3, 0 if 0 < n < 4, 5 otherwise

3. Sketch the following continuous signals for -8 < t < 8: 

    a. x(t) = sin(2 pi t / 8)
    b. x(t) = cos(2 pi t / 4)
    c. x(t) = sin(2 pi t / 2)
    d. x(t) = cos(2 pi t / 2)
    e. x(t) = n-3 if t > 2, 0 otherwise
    f. x(t) = 1 if t < -3, 0 if 0 < t < 4, 5 otherwise
"""
from math import sin, cos, pi
from numpy import arange

ns = arange(-8,8,step=.1)

a = [sin(2*pi*n/8) for n in ns]
matplotlib.pyplot.title('sin(2 pi n / 8)')
matplotlib.pyplot.plot(a, marker='.')
matplotlib.pyplot.show()

b = [cos(2*pi*n/4) for n in ns]
matplotlib.pyplot.title('cos(2 pi n / 4)')
matplotlib.pyplot.plot(b, marker='.')
matplotlib.pyplot.show()

c = [sin(2*pi*n/2) for n in ns]
matplotlib.pyplot.title('sin(2 pi n / 2)')
matplotlib.pyplot.plot(c, marker='.')
matplotlib.pyplot.show()

d = [cos(2*pi*n/2) for n in ns]
matplotlib.pyplot.title('cos(2 pi n / 2)')
matplotlib.pyplot.plot(d, marker='.')
matplotlib.pyplot.show()

e = [n-3 if n > 2 else 0 for n in ns]
matplotlib.pyplot.title('n-3 if t > 2, 0 otherwise')
matplotlib.pyplot.plot(e, marker='.')
matplotlib.pyplot.show()

f = [1 if n < -3 else (0 if 0 < n and n < 4 else 5) for n in ns]
matplotlib.pyplot.title('1 if t < -3, 0 if 0 < t < 4, 5 otherwise')
matplotlib.pyplot.plot(f, marker='.')
matplotlib.pyplot.show()

"""
4. Samples 0 to 11 of a signal have the value: 0, 2, 3, 4, 3, 2,-1, 0, -2,
-3, 2, 1.   Calculate, sketch and label:
    a. The even and odd parts.
    b. The interlaced decomposition.
    c. The step decomposition.
"""
signal = [0, 2, 3, 4, 3, 2,-1, 0, -2, -3, 2, 1]
matplotlib.pyplot.title("Original signal")
matplotlib.pyplot.plot(signal)
matplotlib.pyplot.show()

def even_odd_decomposition(x):
    even = []
    odd = []
    N = len(signal) - 1
    for n in range(len(signal)):
        even.append((x[n] + x[N-n])/2)
        odd.append((x[n] - x[N-n])/2)
    odd[0] = 0 # Definition explicitly says odd[0] = 0
    return even, odd


even, odd = even_odd_decomposition(signal)
matplotlib.pyplot.title("Even / Odd signals")
matplotlib.pyplot.plot(even)
matplotlib.pyplot.plot(odd)
matplotlib.pyplot.show()

def step_decomposition(x):
    steps = []
    N = len(x)
    for n in range(len(x)):
        current_sample = x[n]
        steps.append(([0] * n) + ([current_sample] * (N-n)))
    return steps

steps = step_decomposition(signal)
matplotlib.pyplot.title("step decomposition")
for step in steps:
    matplotlib.pyplot.plot(step)
matplotlib.pyplot.plot(signal)
matplotlib.pyplot.show()

"""
5. Two continuous waveforms, b(t) and x(t) are defined by: 

b(t) =  1 for 0 < t < 2
        0 otherwise

x(t) = -1 for 1 < t < 2
        1 for 2 < t < 3
        4 for 3 < t < 4
        2 for 4 < t < 5
        0 otherwise

    a. Sketch b(t) and x(t)
    b. Show that x(t) can be decomposed into three scaled and shifted versions of
    b(t).  That is, find: a1, a2, a3, s1, s2, s3, such that: x(t) = a1 b(t-s1) +
    a2 b(t-s2) + a3 b(t-s3)
    c. Sketch these three component signals.
"""

from numpy import arange
def B(t):
    if 0 < t <= 2: return 1
    else: return 0

def X(t):
    if 1 < t <= 2: return -1
    elif 2 < t <= 3: return 1
    elif 3 < t <= 4: return 4
    elif 4 < t <= 5: return 2
    else: return 0
B_values = [B(t) for t in arange(0,5,.1)]
X_values = [X(t) for t in arange(0,5,.1)]

matplotlib.pyplot.title("original signal")
matplotlib.pyplot.plot(X_values, 'r')
matplotlib.pyplot.show()

# I should've really made a class instead of manually doing this :|
"""
x(t) = -1*b(t-1) + 2*b(t-2) + 2*b(t-3)
"""
term1 = [-1 * B(t) for t in arange(0,5,.1)]
term1 = ([0] * 10) + term1[:-10]             # Pad and remove excess elements since we don't have a matching time array
term2 = [2 * B(t) for t in arange(0,5,.1)]
term2 = ([0] * 20) + term2[:-20]
term3 = [2 * B(t) for t in arange(0,5,.1)]
term3 = ([0] * 30) + term3[:-30]
totals = [a+b+c for a,b,c in zip(term1,term2,term3)]
matplotlib.pyplot.title("composed signal")
matplotlib.pyplot.plot(term1)
matplotlib.pyplot.plot(term2)
matplotlib.pyplot.plot(term3)
matplotlib.pyplot.plot(totals, 'r')
matplotlib.pyplot.show()

"""
6. Systems are proven to be linear by mathematically showing that they obey
the properties of additivity and homogeneity.  However, systems in the real
world are often only understood by empirical measurements.  That is, a
scientist or engineer places a test signal into the input, and looks at what
comes out. 
        
a. Is it possible to prove that a system is linear based on measurements of
the input and output alone, without knowing the formal mathematical 
relationship between the input and output?  Explain.  

b. Is if possible to prove that a system is nonlinear in this way? Explain.

To help you answer these questions, think about an electronics technician
testing a "black box" for being linear.  He does this by placing signals
into the input and observing the output.  However, the technician has
absolutely no information about what is "inside" the system.  For instance,
it might contain an evil demon trying to deceive the technician.  Or in
another case, it might contain a timer that scrambles the output once every
ten million years of operation. 
"""

# a. It is possible to have high confidence in a system being linear based on measurements.

# b. It is possible, but may not be readily apparently (eg in the case of a timer that
#    scrambles the output once every ten million years of operation.
