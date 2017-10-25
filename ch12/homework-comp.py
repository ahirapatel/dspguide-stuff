#!/usr/bin/env python3

"""
CHAPTER 12: THE FAST FOURIER TRANSFORM
"""

"""
1. Write (or copy) an FFT and an IFFT subroutine. 
"""

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


"""
4.  Answer the following questions.

a. If the DFT by correlation were used in step 2a instead of the FFT,
approximately how much larger in amplitude would the difference signal be?
b. In step 2b, why will the frequency spectra be easier to plot if the time
domain signals have a mean of zero?
c. In step 2b, if the random signal were placed in the imaginary part, and
all zeros placed in the real part, how would the frequency domain be changed?
"""

