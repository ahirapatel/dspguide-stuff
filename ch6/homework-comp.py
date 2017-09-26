#!/usr/bin/env python3

import matplotlib.pyplot

"""
CHAPTER 6: CONVOLUTION

1. Write a program that calculates y[n] = x[n]*h[n], where y[n] is 598
samples, x[n] is 500 samples, and h[n] is 99 samples.  

"""
# Input side algorithm for convolution
def convolve(input_sig, impulse_response):
    convolution_out_len = len(input_sig) + len(impulse_response) - 1
    y = [0] * convolution_out_len
    for i, in_sample in enumerate(input_sig):
        for j, impulse_sample in enumerate(impulse_response):
            y[i+j] += in_sample * impulse_sample
    return y

# It never specified values
x = [3] * 500
h = [2] * 99
y = convolve(x,h)
print("1. len(x) is {}, len(h) is {}, len(y) is {}".format(len(x), len(h), len(y)))

"""
2. Generate an impulse response, h[n], according to the algorithm below. As
discussed in Chapter 16, this is the filter kernel for a "low-pass
windowed-sinc" filter.  When convolved with an input signal, this filter 
passes sinusoids that have fewer than 25 cycles in 500 samples, and blocks
sinusoids with a higher frequency. Make a plot of this signal.

for i = 0 to 98
 h[i] = 0.31752 * sin(0.314159 * (i-49.00001)) / (i-49.00001)    
 h[i] = h[i] * (0.54 - 0.46 * cos(0.0641114 * i))
next i
"""
def make_kernel():
    from math import sin, cos
    h = [0] * 99
    for i in range(0,99):
        h[i] = 0.31752 * sin(0.314159 * (i-49.00001)) / (i-49.00001)
        h[i] = h[i] * (0.54 - 0.46 * cos(0.0641114 * i))
    return h


lpws_filter = make_kernel()
matplotlib.pyplot.plot(lpws_filter)
matplotlib.pyplot.title("just the kernel")
matplotlib.pyplot.show()


"""
3. Test your program by convolving h[n] with the signal described below. 
What should the output of your program be in response to this signal? Why?   

x[n] = 1 for n = 0
x[n] = 0 otherwise


"""
x = [1] + ([0]*100)
matplotlib.pyplot.plot(convolve(x, lpws_filter))
matplotlib.pyplot.title("convolution of kernel with delta")
matplotlib.pyplot.show()
# The output should be the lpws_filter kernel because the x[n] data is the
# delta function

"""
4. Generate a more complicated test signal, x[n], that consists of two
sinusoids added together.  The first sinusoid will have an amplitude of 1,
and make 6 complete cycles in the 500 samples.  The second sinusoid will
have an amplitude of 0.5 and make 44 complete cycles in the 500 samples. 
Make of plot of this signal.  
"""


"""
5. Test your convolution program by filtering the signal you created in 4,
with the filter kernel you created in 2. Plot this signal. Has the filter
passed the lower frequency signal, while blocking the higher frequency
signal?  Comment on its effectiveness.  


6. Turn the filter kernel into a high-pass filter by changing the sign of
all the samples, and then adding one to sample 49  (you can look ahead to
Fig. 14-5 if you want more information on this procedure). Test this
high-pass filter in the same way as step 4.
"""
