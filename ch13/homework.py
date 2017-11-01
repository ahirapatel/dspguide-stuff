#!/usr/bin/env python3

"""
CHAPTER 13: CONTINUOUS SIGNAL PROCESSING
"""

"""
1. How short must a pulse be to act as an impulse to the following systems?
(Give an "order-of- magnitude" approximation and justify your reasoning).

a. A high-fidelity music system, designed to reproduce sounds between 20 Hz
and 20 kHz.  
b. An automotive suspension (think about how fast it recovers after the
vehicle hits a bump).
c. An 8 pole Bessel low-pass filter with a cutoff frequency of 1 kHz. (hint:
see Fig. 3-13)
d. The disruption of a galaxy when struck by another galaxy (see the picture
on the cover of the book, and the caption opposite the title page). Hint:
The "time constant" of disruption is the time it takes the expanding gas to
equal the diameter of the galaxy. 
"""
# a. 20 kHz
# b. Very tiny, very tiny and sudden bumps can yield quick changes, or 
#    larger, slower changes like speed bumps can yield changes.
# c. .3 or .4ish seconds
# d. 

"""
2. Calculate and sketch the convolution of a(t) and b(t). Also provide
sketches showing how each region in the output signal is calculated.  

a. a(t) = 1 for 0 < t < 2, and 0 otherwise 
   b(t) = 1 for 0 < t < 2, and 0 otherwise

b. a(t) = 2 for 0 < t < 1, and 0 otherwise 
   b(t) = 1 for 2 < t < 5, and 0 otherwise

c. a(t) = 1 for 0 < t < 1, and 0 otherwise 
   b(t) = t for 0 < t < 3, and otherwise

d. a(t) = exp(-kt) for 0 < t, and 0 otherwise, and k is a constant
   b(t) = exp(-kt) for 0 < t, and 0 otherwise

e. a(t) = exp(-kt) for 0 < t, and 0 otherwise
   b(t) = -2 delta(t-2)
"""

"""
3. Convolve the following signals by differentiating one to reduce it to
impulses (such as in Fig. 13-7).

a(t) = 1 for 0 < t < 4, and 0 otherwise
b(t) = sin(2 pi t) for -1 < t < 1, and 0 otherwise  
"""

"""
4. Calculate the Fourier transform of the following signals.  Give your
answer in rectangular form.

a. x(t) = 1 for -1 < t < 1, and 0 otherwise. 
b. x(t) = t for -1 < t < 1, and 0 otherwise
c. x(t) = delta(t)
d. x(t) = exp(-abs(kt)), where abs is the absolute value and k is a constant
"""

"""
5. Which of the following signals has a larger 15th harmonic: a square wave,
a triangle wave, or a sawtooth wave?
"""
# Square wave. It has sharper edges than the others, so higher frequency harmonics
