#!/usr/bin/env python3

import matplotlib.pyplot

"""
CHAPTER 6: CONVOLUTION

1. A system has an impulse response, h[n], given by:  1, 2, 2, 1, 0, -1, 0,
0, for the values of samples 0 to 7.  Calculate the output of the system in
response to the following input signals.  

a.  1, 0, 0, 0, 0, 0, 0, 0, 0
b. -3, 0, 0, 0, 0, 0, 0, 0, 0 
c.  0, 0, 1, 0, 0, 0, 0, 0, 0
d.  1, 0, 1, 0, 0, 0, 0, 1, 0
e.  3, 0,-1, 0, 0, 2, 0, 0, 0
f.  2,-1, 0, 0, 1, 0,-1, 0, 0 
"""

# Input side algorithm for convolution
def convolve(input_sig, impulse_response):
    convolution_out_len = len(input_sig) + len(impulse_response) - 1
    y = [0] * convolution_out_len
    for i, in_sample in enumerate(input_sig):
        for j, impulse_sample in enumerate(impulse_response):
            y[i+j] += in_sample * impulse_sample
    return y

h = [1, 2, 2, 1, 0, -1, 0, 0]
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.title("#1 impulse response, h[n]")
matplotlib.pyplot.show()

a = [1, 0, 0, 0, 0, 0, 0, 0, 0]
output = convolve(a, h)
print(output) # Should be unit impulse, just bigger len()
matplotlib.pyplot.plot(a, marker='.')
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output, marker='.')
matplotlib.pyplot.title("#1a input and convolution output")
matplotlib.pyplot.show()

b = [-3, 0, 0, 0, 0, 0, 0, 0, 0]
output = convolve(b, h)
print(output)
matplotlib.pyplot.plot(b, marker='.')
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output, marker='.')
matplotlib.pyplot.title("#1b input and convolution output")
matplotlib.pyplot.show()

c = [0, 0, 1, 0, 0, 0, 0, 0, 0]
output = convolve(c, h)
print(output)
matplotlib.pyplot.plot(c, marker='.')
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output, marker='.')
matplotlib.pyplot.title("#1c input and convolution output")
matplotlib.pyplot.show()

d = [1, 0, 1, 0, 0, 0, 0, 1, 0]
output = convolve(d, h)
print(output)
matplotlib.pyplot.plot(d, marker='.')
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output, marker='.')
matplotlib.pyplot.title("#1d input and convolution output")
matplotlib.pyplot.show()

e = [3, 0,-1, 0, 0, 2, 0, 0, 0]
output = convolve(e, h)
print(output)
matplotlib.pyplot.plot(e, marker='.')
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output, marker='.')
matplotlib.pyplot.title("#1e input and convolution output")
matplotlib.pyplot.show()

f = [2,-1, 0, 0, 1, 0,-1, 0, 0]
output = convolve(f, h)
print(output)
matplotlib.pyplot.plot(f, marker='.')
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output, marker='.')
matplotlib.pyplot.title("#1f input and convolution output")
matplotlib.pyplot.show()

"""
2.   Adding zeros to the end of a signal is a common DSP technique called
"padding with zeros."  Use your results in the last problem to answer the
following: 

a. How would the output signals be changed if 5 additional samples, all with
a value of zero, were added to the end of the impulse response?  
b. How would the output signals be changed if 5 additional samples, all with
a value of zero, were added to the end of the input signals? 
c. How would the output signals be changed if 5 additional samples, all with
a value of zero, were added to the end of both the input signals and the
impulse response?       
d. Complete the following statement summarizing how "padding with zeros"
affects convolution: "When M zeros are added to either the input signal or
the impulse response, the only change to the output signal is [fill in the
blank].  
"""
# a. The output signals would be the same here, they would just have a longer
#    convolution output padded with zero
h_padded = h + [0]*5 # padding with 5 additional samples of zero
d = [1, 0, 1, 0, 0, 0, 0, 1, 0]
output = convolve(d, h)
output_padded = convolve(d, h_padded)
print("Original output of 1d:", output)
print("Output of 1d with padded h[n]:", output_padded)
matplotlib.pyplot.plot(d, marker='.')
matplotlib.pyplot.plot(output, marker='o')
matplotlib.pyplot.plot(output_padded, marker='x')
matplotlib.pyplot.title("#1d input and convolution output and convolution output with padded h[n]")
matplotlib.pyplot.show()

# b. The output signals would be the same here, they would just have a longer
#    convolution output padded with zero. Order of operations in convolution
#    technically doesn't matter in terms of the math, so it's like 2.a.
d = [1, 0, 1, 0, 0, 0, 0, 1, 0]
d_padded = d + [0]*5
output = convolve(d, h)
output_padded = convolve(d_padded, h)
print("Original output of 1d:", output)
print("Output of 1d with padded :", output_padded)
matplotlib.pyplot.plot(d_padded, marker='.')
matplotlib.pyplot.plot(output, marker='o')
matplotlib.pyplot.plot(output_padded, marker='x')
matplotlib.pyplot.title("#1d padded input and convolution output and padded input signal convolution output")
matplotlib.pyplot.show()

# c. The output signals would be the same here, they would just have an even longer
#    convolution output padded with zero.
output = convolve(d, h)
output_padded = convolve(d_padded, h_padded)
print("Original output of 1d:", output)
print("Output of 1d with padded :", output_padded)
matplotlib.pyplot.plot(d_padded, marker='.')
matplotlib.pyplot.plot(output, marker='o')
matplotlib.pyplot.plot(output_padded, marker='x')
matplotlib.pyplot.title("#1d padded input and convolution output and padded input signal convolution output")
matplotlib.pyplot.show()



"""
3. Two signals, x[n] and h[n], are defined by:

x[n]:  1, 0, 2, 3, 2, 1,-1,-2,-1, 0, 2, 3, 3, 2, 1, 1  (samples 0-15) 
h[n]:  1, 2, 3,-3,-2,-1  (samples 0-5)  

If y[n] = x[n]*h[n], use the input side algorithm to determine the
contribution to y[n] from the indicated sample:

a. x[2]
b. x[6]
c. x[9]
"""
# Input side algorithm for convolution
def input_side_convolve_contributions(input_sig, impulse_response, sample_index):
    convolution_out_len = len(input_sig) + len(impulse_response) - 1
    y = [0] * convolution_out_len
    in_sample = input_sig[sample_index]
    for j, impulse_sample in enumerate(impulse_response):
        y[sample_index+j] += in_sample * impulse_sample
    return y

x = [1, 0, 2, 3, 2, 1,-1,-2,-1, 0, 2, 3, 3, 2, 1, 1]
h = [1, 2, 3,-3,-2,-1]
print("3a: x[2]")
convolve(x, h)
print("contributions of x[2]", input_side_convolve_contributions(x, h, 2))

print("3b: x[6]")
convolve(x, h)
print("contributions of x[6]", input_side_convolve_contributions(x, h, 6))

print("3c: x[9]")
convolve(x, h)
print("contributions of x[9]", input_side_convolve_contributions(x, h, 9))



"""
4. For the signals in the last problem, use the output side algorithm to
calculate the value of the following samples:  

a. y[8]
b. y[10]
c. y[3]
d. y[18]
"""
# Output side algorithm for convolution
def output_side_convolve(input_sig, impulse_response):
    convolution_out_len = len(input_sig) + len(impulse_response) - 1
    y = [0] * convolution_out_len
    for i in range(len(y)):
        for j, impulse_sample in enumerate(impulse_response):
            if (i-j) < 0 or (i-j) > len(input_sig)-1:
                continue
            y[i] += impulse_sample * input_sig[i-j]
    return y

def output_side_convolve_contributions(input_sig, impulse_response, sample_index):
    y = 0
    for j, impulse_sample in enumerate(impulse_response):
        if (sample_index-j) < 0 or (sample_index-j) > len(input_sig)-1:
            continue
        y += impulse_sample * input_sig[sample_index-j]
    return y

x = [1, 0, 2, 3, 2, 1,-1,-2,-1, 0, 2, 3, 3, 2, 1, 1]
h = [1, 2, 3,-3,-2,-1]
print("4a: y[8]")
print("y[8]", output_side_convolve(x, h)[8])

print("4b: y[10]")
convolve(x, h)
print("y[10]", output_side_convolve(x, h)[10])

print("4c: y[3]")
convolve(x, h)
print("y[3]", output_side_convolve(x, h)[3])

print("4d: y[18]")
convolve(x, h)
print("y[18]", output_side_convolve(x, h)[18])

"""
5. Two signals, a[n] and b[n], are defined by:

a[n]:  1, 0, 0, 2, 1, 0 
b[n]:  0,-1,-2, 0, 0, 1

a. Calculate a[n]*b[n] by using an impulse decomposition on a[n], convolving
each of the components with b[n], and synthesizing (adding) the resulting
signals.
b. Calculate a[n]*b[n] by using an impulse decomposition on b[n], convolving
each of the components with a[n], and synthesizing (adding) the resulting
signals.
c. Do the results of these two methods agree? What property is demonstrated
in this problem?
"""
#a. This is kind of what the input side convolve code does anyway, so yes.
#b. This is kind of what the input side convolve code does anyway, so yes.
#c. Yes each agrees, this demonstrates associativity.


"""
6. Calculate the convolution of the signal: h[n] = 1, 2, 3, 0, 0 with the 
indicated signals (assume each of the following run from sample 0 to 7).

a. x[n] =  delta[n]
b. x[n] = -5 delta[n-2] 
c. x[n] =  2 delta[n+1] - delta[n+1]
d. x[n] =  1, 2, 3, 0, 0 ...
e. x[n] = -n  for  0 < n < 5, and 0 otherwise  
f. x[n] =  2^(-n)
g. x[n] = sin(2 pi n)
h. x[n] = cos(2 pi n)
i. x[n] = sin (pi n)     
"""
h = [1, 2, 3, 0, 0]
#a. x[n] =  delta[n]
x = [1,0,0,0,0,0,0,0]
output = convolve(x, h)
print("5a. delta[n]", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5a")
matplotlib.pyplot.show()

#b. x[n] = -5 delta[n-2]
x = [0,0,-5,0,0,0,0,0]
output = convolve(x, h)
print("5b. -5 delta[n-2]", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5b")
matplotlib.pyplot.show()

#c. x[n] =  2 delta[n+1] - delta[n+1]
x = [0,0,0,0,0,0,0,0]  # ?? I think ??
output = convolve(x, h)
print("5c. 2 delta[n+1] - delta[n+1]", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5c")
matplotlib.pyplot.show()

#d. x[n] =  1, 2, 3, 0, 0 ...
x =  [1, 2, 3, 0, 0, 0, 0, 0]
output = convolve(x, h)
print("5d. 1, 2, 3, 0, 0 ...", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5d")
matplotlib.pyplot.show()

#e. x[n] = -n  for  0 < n < 5, and 0 otherwise
x =  [(-n if 0 < n < 5 else 0) for n in range(0,8)]
output = convolve(x, h)
print("5e. -n  for  0 < n < 5, and 0 otherwise", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5e")
matplotlib.pyplot.show()

#f. x[n] =  2^(-n)
x = [2**-n for n in range(0,8)]
output = convolve(x, h)
print("5f. 2^(-n)", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5f")
matplotlib.pyplot.show()

#g. x[n] = sin(2 pi n)
from math import sin, cos, pi
x = [sin(2*pi*n) for n in range(0,8)]
output = convolve(x, h)
print("5g. sin(2 pi n)", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5g")
matplotlib.pyplot.show()

#h. x[n] = cos(2 pi n)
x = [cos(2*pi*n) for n in range(0,8)]
output = convolve(x, h)
print("5h. cos(2 pi n)", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5h")
matplotlib.pyplot.show()

#i. x[n] = sin (pi n)
x = [sin(pi*n) for n in range(0,8)]
output = convolve(x, h)
print("5i. sin(pi*n)", output, len(output))
matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(h, marker='.')
matplotlib.pyplot.plot(output)
matplotlib.pyplot.title("5i")
matplotlib.pyplot.show()

"""
7. Calculate the convolution of the following signals (your answer will be
in the form of an equation): 

a. h[n] = delta[n], x[n] = delta[n]
b. h[n] = delta[n], x[n] = delta[n-k]
c. h[n] = delta[n-2], x[n] = delta[n-1] + delta[n+4]
d. h[n] = delta[n-1] + delta[n+1], x[n] = delta[n-a] + delta[n+b]
e. h[n] = delta[n], x[n] = exp(-n)
f. h[n] = delta[n+2], x[n] = exp(n)
g. h[n] = delta[n-2], x[n] = exp(-n)
h. h[n] = exp(-n), x[n] = delta[n-2]
i. h[n] = delta[n] - delta[n-1], x[n] = exp(-n)
"""
x = [0,0,1,0,0,0] # n-2
h = [0,1,0,0,0,0] # n-1 
print("pre-7 example convolution of {} {} = {}", x, h, convolve(x, h)) # and the result is n-3

# ASSUME MY USE OF * FOR THIS PROBLEM IS FOR CONVOLUTION

#a. h[n] = delta[n], x[n] = delta[n]
#a. y[n] = delta[n]

#b. h[n] = delta[n], x[n] = delta[n-k]
#b. y[n] = delta[n-k]

#c. h[n] = delta[n-2], x[n] = delta[n-1] + delta[n+4]
#c. y[n] = delta[n-2] * delta[n-1] + delta[n-2] * delta[n+4]
#          delta[n-3] + delta[n+3]

#d. h[n] = delta[n-1] + delta[n+1], x[n] = delta[n-a] + delta[n+b]
#d. y[n] = delta[n-1] * delta[n-a] + delta[n-1] * delta[n+b] + delta[n+1] * delta[n-a] + delta[n+1] * delta[n+b]
#d.        delta[n-1-a] + delta[n-1+b] + delta[n+1-a] + delta[n+1+b]

#e. h[n] = delta[n], x[n] = exp(-n)
#e. y[n] = exp(-n)

#f. h[n] = delta[n+2], x[n] = exp(n)
#f. y[n] = exp(n+2)
from math import exp
h = [0,0,1,0,0,0] # n-2
x = [exp(n) for n in range(6)]
print("Example: {}, {}, convolve == {}".format(h,x,convolve(x,h))) #exp(n-2)

#g. h[n] = delta[n-2], x[n] = exp(-n)
#g. y[n] = exp(-(n-2))

#h. h[n] = exp(-n), x[n] = delta[n-2]
#h. y[n] = exp(-(n-2))

#i. h[n] = delta[n] - delta[n-1], x[n] = exp(-n)
#i. y[n] = delta[n] * exp(-n) - delta[n-1] * exp(-n)
#i. y[n] = exp(-n) - exp(-(n-1))


"""
8. A financial expert receives daily reports on the value of a particular
stock. Each day he calculates the average value of the stock over the last 
30 days.  If this averaging were described as a system: 

a. What are the input and output signals?
b. Is this system linear?
c. What is the impulse response of the system?
d. What practical purpose would this system be serving?
e. What would be the impulse response if the average was taken over M days? 
"""
#a. Input: Last 30 days of stock value, Output: Average of 30 days of stock value
#b. Yes, this merely adds the stock values for previous days, then divides them
#   by a constant of 30.
#c. it is a bunch of 1/30s for 30 days, then goes to 0
#d. Getting a general trend of the stock value without focusing on huge jumps and dips.
#   Like a smoothing filter I guess.
#e. The same as (c.) but the values would be 1/M for M days


"""
9. If the signal, x[n], has a value of zero over the interval:  A <= n <= B, 
and if signal, h[n], has a value of zero over the interval: C <= n <= D, then 
x[n]*h[n] must be zero over the interval, E <= n <= F.  Express the variables, 
E and F, in terms of: A, B, C, and D.  
"""
# E = A-C, F = B+D


"""
10. Two signals, a[n] and b[n], each contain 6 points, as defined below. 
Calculate a[n]*b[n].

a[n]:  1,  0,  0, 2, 1, 0  
b[n]:  0, -1, -2, 0, 0, 1  

a. Where both signals run from sample 0 to 5
b. Where both signals run from sample 2 to 7
c. Where a[n] runs from sample 0 to 5, and b[n] runs from sample -3 to 2
d. Where a[n] runs from sample -10 to -5, and b[n] runs from sample -5 to 0 
"""

# a.
a = [1,  0,  0, 2, 1, 0]
b = [0, -1, -2, 0, 0, 1]
print("10a: both run 0 to 5", convolve(a,b))
# b.
a2 = [0]*2 + a
b2 = [0]*2 + b
print("10b: both run 2 to 7", convolve(a2,b2))
# c. ??????????????????????????????????????? I don't know
a3 = [0]*3 + a
b3 = b
print("10c: where a runs from 0 to 5, b runs -3 to 2", convolve(a3,b3))
# d. ???????????????????????????????????????
a4 = a
b4 = [0]*2 + b
print("10d: where a runs -10 to -5, b runs -5 to 0", convolve(a4,b4))
