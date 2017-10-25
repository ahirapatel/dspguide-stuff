#!/usr/bin/env python3

"""
CHAPTER 12: THE FAST FOURIER TRANSFORM
"""

"""
1. The following spectrum was produced by the real DFT. Generate the
frequency spectrum of the corresponding complex DFT. 

samples 0 to 8 of the real part:        1, 2,-1,-2, 0, 1, 2, 3, 2 
samples 0 to 8 of the imaginary part:   0, 2, 4, 5,-3,-2, 1, 1, 0
"""


"""
2. A time domain signal, consisting of a real part, rex[n], and an imaginary
part, imx[n], has the following complex spectrum:

samples 0 to 7 of the real part:        1, 2,-1,-2, 1, 0, 2, 3
samples 0 to 7 of the imaginary part:   3, 2, 4, 5,-1,-2, 1, 1

a. Separate this spectrum (both the real and imaginary parts) into even and
odd parts. 
b. What would be the spectrum if the values in imx[n] were set to zero?
e. What would be the spectrum if the values in rex[n] were set to zero?
"""
     

"""
3.  Suppose you want to conduct a spectral analysis of a signal containing
1,003,520 samples, and the computer you are using has values of: Kdft = 1
microsecond, and Kfft = 1.5 microsecond. 

a. Calculate the execution time if the signal is broken into 64 sample
segments, and the DFT by correlation algorithm is used.  Repeat for segment
lengths of: 256, 1024, and 4096. (Ignore the calculation time for averaging
the frequency spectra).
b. Repeat (a) using the FFT algorithm.  
"""
