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
import numpy.fft
real = [1, 2,-1,-2, 0, 1, 2, 3, 2]
imag = [0, 2, 4, 5,-3,-2, 1, 1, 0]
data = [complex(r,i) for r,i in zip(real, imag)]
orig_sig = numpy.fft.irfft(data)
print(data)
print(orig_sig)
complex_fft = numpy.fft.fft(orig_sig)
print(complex_fft)
# Should just be complex conjugates, confirmed with above code.
# NOTE: Sample 0 is dc offset so it is not mirrored
# samples 9 to 16 of the real part:         3,  2, 1, 0, -2, -1,  2, 1
# samples 9 to 16 of the imaginary part:   -1, -1, 2, 3, -5, -4, -2, 0

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
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
# TODO: OOPS I MISREAD. The values are the spectrum, not the time domain siggy
from numpy import absolute
import matplotlib.pyplot
real = [1, 2,-1,-2, 1, 0, 2, 3]
imag = [3, 2, 4, 5,-1,-2, 1, 1]
# a. Why? I am confused about a. Do I do even/odd decomposition or just
#    every other sample? What does this even show?
def even_odd_decomposition(x):
    even = []
    odd = []
    N = len(x) - 1
    for n in range(len(x)):
        even.append((x[n] + x[N-n])/2)
        odd.append((x[n] - x[N-n])/2)
    odd[0] = 0 # Definition explicitly says odd[0] = 0
    even[0] = x[0] # Definition explicitly says even[0] = x[0]
    return even, odd

data = [complex(r,i) for r,i in zip(real, imag)]
matplotlib.pyplot.plot(absolute(numpy.fft.fft(data)))
matplotlib.pyplot.show()
# b.
data = [complex(r,0) for r in real]
matplotlib.pyplot.plot(absolute(numpy.fft.fft(data)))
matplotlib.pyplot.show()
# c.
data = [complex(0,i) for i in imag]
matplotlib.pyplot.plot(absolute(numpy.fft.fft(data)))
matplotlib.pyplot.show()


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

# a. 1003520 / 64 = 15680
#    (1 * 64^2) * 15680 = 64225280
#    1003520 / 256 = 3920
#    (1 * 256^2) * 3920 = 256901120
#    1003520 / 1024 = 980
#    (1 * 1024^2) * 980 = 1027604480
#    1003520 / 4096 = 245
#    (1 * 4096^2) * 245 = 4110417920 micros

# b. 1003520 / 64 = 15680
#    (1.5 * 64*log64) * 15680 = 9031680
#    1003520 / 256 = 3920
#    (1.5 * 256*log256) * 3920 = 12042240
#    1003520 / 1024 = 980
#    (1.5 * 1024*log1024) * 980 = 15052800
#    1003520 / 4096 = 245
#    (1.5 * 4096*log4096) * 245 = 18063360
