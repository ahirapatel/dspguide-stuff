#!/usr/bin/env python
"""
CHAPTER 8: THE DISCRETE FOURIER TRANSFORM
"""

"""
1. A sinusoid at 1.7 kHz is digitized at 10,000 samples per second.  The
signal is passed through a 2048 point DFT, and converted to polar form. Draw
four sketches of the magnitude, one for each of the four ways that the
frequency domain's independent variable can be expressed. Be sure to
indicate the frequency symbol used, the range of values, the units, and at
what frequency the sinusoid appears. 
"""
# IN NOTEBOOK

"""
2. A peak appears at index number 19 when a 256 point DFT is taken of a
signal.  

a. What is the frequency of the peak expressed as a fraction of the sampling
rate? Do you need to know the actual sampling rate to answer this question?
b. What is the frequency of the peak expressed as a natural frequency?
c. What is the sampling rate if the peak corresponds to 21.5 kHz in the
analog signal?
d. What is the frequency of the sinusoid (in hertz) if the sampling rate is
100 kHz?    
"""
# 2a. 19/256 = 0.07421875, assuming DFT bands are 1Hz. No don't need sampling rate.
# 2b. 19/256 * π = 0.23316507975861744
# 2c. 19/256 * Sample_Rate = 21500Hz
#     Sample_Rate = 21500Hz * 256 / 19
#     Sample_Rate = 289684.2105263158 Hz
#     Sample_Rate = ~289.684 KHz
# 2d. 19/256 * 100000Hz = 7421.875 Hz

"""
3. Calculate, sketch and label the basis functions for an 8 point DFT. 
"""
# IN NOTEBOOK
# Sin == Im
# Cos == Re

"""
4. An 8 sample signal is given by: 20,21,22,23,24,25,26,27.  Its frequency
domain is given by: R0,R1,R2,R3,R4 and I0,I1,I2,I3,I4.  Write the
simultaneous equations relating the frequency domain and the time domain.
Use the numerical value for each point in the basis functions, for example,
use 0.7071, not sin(pi/4). How difficult would it be to solve these
equations?
"""
# Too lazy to type this all out

# form of sin(2*pi*k*i/N), k is which sinusoid, i is which sample
# Note the first and last waveforms of imaginary / sin will always be 0 for k=0,k=5

# Take the first(index i is 0) sample of each basis function (see k going up?),
# add em together with appropriate scaling factors (a-h), then you get your first sample.
# Note how sins don't have a k=0, but cos does. (and sin won't have k=5, but cos will)
# 20 = a*sin(2*pi*1*0/8) + b*sin(2*pi*2*0/8) + ... + g*cos(2*pi*0*0/8) + ... + h*cos(2*pi*5*0/8)

# Take the second (index i is 1) sample of each basis function.
# 21 =  a*sin(2*pi*1*1/8) + b*sin(2*pi*2*1/8) + ... + g*cos(2*pi*0*1/8) + ... + h*cos(2*pi*5*1/8)

# And so on...
# 22 = 
# 23 = 
# 24 = 
# 25 = 
# 26 = 
# 27 = 

# So you get 8 equations, with 8 unknowns (a-h) and then need to solve them. Using the joys of matrix
# math you can solve them. It'd be more annoying to solve this in terms of programming it or by hand,
# in in terms of performance.

"""
5. Using the signals in the last problem, write 10 equations for calculating
the 10 points in the frequency domain, using the correlation algorithm.
Solve these equations. 
"""
# See equation 8-4 in the book. Or the computer exercises in the DFT() function.

"""
6. The frequency domain of a signal is given by:

real part:  1, 2, 3, 3, 1,-2,-1, 1, 2
imag part:  0,-1,-2, 0, 0, 0, 2, 1, 0

a. What length of DFT does this correspond to? 
b. Calculate the amplitudes of the sine and cosine waves that comprise the
time domain signal.
c. What is the mean (average value) of the time domain signal?
"""
# 6a. 16
# 6b. Real part maps to cosine, imaginary part maps to sine.
#     The first real value of 1, indicates 1 amplitude for the first basis cosine.
#     ....and so on and so forth.
# 6c.
real = [1, 2, 3, 3, 1,-2,-1, 1, 2]
imag = [0,-1,-2, 0, 0, 0, 2, 1, 0]
def IDFT(real, imag):
    from math import pi, sin, cos

    N = len(real) + len(imag) - 2 # num elements in original signal
    scale = N/2 # N/2+1 elements, but we divide by N/2 to scale amplitudes
    real = [r/scale for r in real]
    imag = [-i/scale for i in imag]
    orig = [0] * N

    for i in range(N):
        for k in range(0,N//2+1):
            orig[i] += real[k] * cos(2*pi*k*i/N)
            orig[i] += imag[k] * sin(2*pi*k*i/N)

    return orig

original_siggy = IDFT(real, imag)
# .125
print("6c. average value of original signal is", sum(original_siggy)/len(original_siggy))

"""
7. You are told that the following signals are the frequency domain of a 32
point real DFT. Give two reasons why this is not possible.
     
real part:  1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0 
imag part:  8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7 
"""
# real and imag parts are only 16 values in length, they should be 17 each
# N/2 + 1, not N/2
# The imaginary part always has a 0 for the first and last values, it does not here.

"""
8. Convert the following real and imaginary parts into polar form. Sketch a
diagram of each, such as Fig. 8-9.  In each case, state if the conversion
equation: phase = arctan(IP/RP), provides the correct answer without
additional steps: 

a. RP =  1, IP =  1
b. RP =  1, IP = -1
c. RP = -1, IP =  1
d. RP = -1, IP = -1
e. RP =  1, IP =  0
f. RP = -1, IP =  0
g. RP =  0, IP =  1
h. RP =  0, IP = -1
"""

# a. RP =  1, IP =  1
#    mag = 1.414
#    phase = pi/4
# b. RP =  1, IP = -1
#    mag = 1.414
#    phase = -pi/4
# c. RP = -1, IP =  1
#    mag = 1.414
#    phase = 3pi/4  # do the add pi thing
# d. RP = -1, IP = -1
#    mag = 1.414
#    phase = -5pi/4 # do the subtract pi thing
# e. RP =  1, IP =  0
#    mag = 1
#    phase = 0
# f. RP = -1, IP =  0
#    mag = 1
#    phase = pi # do the add pi thing
# g. RP =  0, IP =  1
#    mag = 1
#    phase = pi/2
# h. RP =  0, IP = -1
#    mag = 1
#    phase = -pi/2

# Not sure how to sketch a "diagram of each"

