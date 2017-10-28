#!/usr/bin/env python3

"""
CHAPTER 12: THE FAST FOURIER TRANSFORM
"""

"""
1. Write (or copy) an FFT and an IFFT subroutine. 
"""
import numpy.fft

"""
2. Test that the subroutines are operating correctly:

a. Generate two random signals, each containing 256 samples, and place them
in the real and imaginary parts of the time domain.  Take the FFT and then
the IFFT.  Calculate the difference between the original signals, and the
reconstructed signals.  Is the difference zero?  Explain.  Make a plot of
the difference for the real part. 

b. Place a random signal into the real part of the time domain, and zeros
into the imaginary part. Take the FFT and convert to polar form.  Plot the
real & imaginary parts.  (To make the frequency spectra easier to graph, you
will probably want to use random numbers that have a mean of zero).   Does
the frequency domain have the proper symmetry? Explain 
"""
from random import random
import matplotlib.pyplot
from numpy import absolute, angle, real, imag

# a.
random_signal = [random() + (random()*(0+1j)) for x in range(256)]
fft_out = numpy.fft.fft(random_signal)
reconstructed_signal = numpy.fft.ifft(fft_out)
delta = [abs(a-b) for a,b in zip(random_signal, reconstructed_signal)]
# The max difference is at the range of double precision errors
print(max(delta))
matplotlib.pyplot.plot(delta)
matplotlib.pyplot.show()

# b.
random_signal = [random()*1j for x in range(256)]
fft_out = numpy.fft.fft(random_signal)
mag, phase = absolute(fft_out), angle(fft_out)
mag_real = real(mag)
mag_imag = imag(mag)
# Looks pretty symmetric barring the DC offset at 0
matplotlib.pyplot.plot(mag_real)
matplotlib.pyplot.plot(mag_imag)
matplotlib.pyplot.show()

"""
3. Use the FFT in a spectral analysis problem:

a. Generate a 1,024,000 sample signal containing normally distributed random
noise with zero mean and a standard deviation of one, plus a sine wave with
amplitude 0.1, and a frequency of 0.2. 
b. Plot 1024 samples from this signal.  Is the sine wave visible?  
c. Take the FFT of these 1024 samples and plot the magnitude.  Is the sine
wave visible?
d. Use the method of Chapter 9 to calculate the average frequency spectrum
of the 1,024,000 point signal (break the signal into 1024 sample segments,
calculate the FFTs, and average the magnitudes). Is the sine wave visible in
the averaged spectrum?
"""
from random import gauss
from math import sin, pi
# a.
sig = [gauss(0, 1) + (.1 * sin(.2*2*pi*x)) for x in range(1024000)]

# b. sine wave is not visible
matplotlib.pyplot.plot(sig[:1024])
matplotlib.pyplot.show()

# c. sine wave is not visible
fft_out = numpy.fft.fft(sig[:1024])
mag, phase = absolute(fft_out), angle(fft_out)
matplotlib.pyplot.plot(real(mag))
matplotlib.pyplot.show()

# d. sine wave is WAAAAAAY more visible
diced_data = [sig[i:i+1024] for i in range(0, len(sig), 1024)]
diced_fft = [absolute(numpy.fft.fft(data)) for data in diced_data] # gets polar magnitude
# my god, use zip() with 1000 input values
summed_fft = [sum(lots_of_vals) for lots_of_vals in zip(*diced_fft)]
averaged_fft = [x / 1024 for x in summed_fft]
matplotlib.pyplot.plot(real(averaged_fft))
matplotlib.pyplot.show()

"""
4.  Answer the following questions.

a. If the DFT by correlation were used in step 2a instead of the FFT,
approximately how much larger in amplitude would the difference signal be?
b. In step 2b, why will the frequency spectra be easier to plot if the time
domain signals have a mean of zero?
c. In step 2b, if the random signal were placed in the imaginary part, and
all zeros placed in the real part, how would the frequency domain be changed?
"""
# a. Not much, FFT should be more accurate due to less floating point operations.
#    However, I can find many papers online about FFT inaccuracies when poorly
#    implemented.
# b. The noise averages out?
# c. Yes it would be changed.
