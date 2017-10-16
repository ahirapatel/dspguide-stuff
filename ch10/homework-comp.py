#!/usr/bin/env python3

import matplotlib.pyplot

# Input side algorithm for convolution
def convolve(input_sig, impulse_response):
    convolution_out_len = len(input_sig) + len(impulse_response) - 1
    y = [0] * convolution_out_len
    for i, in_sample in enumerate(input_sig):
        for j, impulse_sample in enumerate(impulse_response):
            y[i+j] += in_sample * impulse_sample
    return y

def DFT(data):
    from math import sin, cos, pi
    N = len(data)
    real = [0] * (N//2+1)
    imag = [0] * (N//2+1)
    for k in range(len(real)):
        for i in range(N):
            real[k] += data[i] * cos(2*pi*k*i/N)
            imag[k] += -data[i] * sin(2*pi*k*i/N)
    return real, imag

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

def rect_to_polar(real, imag):
    from math import atan, pi
    mag = []
    phase = []
    for r, i in zip(real, imag):
        mag.append((r**2 + i**2)**.5)

        if r == 0:  # Do what book does to prevent div by 0. There seems like there is probably a better way.
            r = 1e-20
        # Correct arctan range from -pi to pi. lim(arctan(x)) as x approaches infinity == pi/2
        if r < 0 and i < 0:
            phase.append(atan(i / r) - pi)
        elif r < 0 and i >= 0:
            phase.append(atan(i / r) + pi)
        else:
            phase.append(atan(i / r))

    return mag,phase

def polar_to_rect(mag, phase):
    from math import sin, cos

    real = []
    imag = []
    for m, p in zip(mag, phase):
        real.append(m * cos(p))
        imag.append(m * sin(p))

    return real, imag

"""
CHAPTER 10: PROPERTIES OF THE DFT
"""

"""
Time domain shifting, time domain aliasing.
"""

"""
1. Generate and plot a 512 sample signal containing a Gaussian curve:

x[n] = exp(-(n-200)^2/900)
"""
from math import exp
x = [exp((-(n-200)**2)/900) for n in range(512)]

matplotlib.pyplot.plot(x)
matplotlib.pyplot.title("exp(-(n-200)^2/900)")
matplotlib.pyplot.show()

"""
2. Calculate the DFT, convert to polar form, and plot the magnitude and
phase. 
"""
real, imag = DFT(x)
mag, phase = rect_to_polar(real, imag)

matplotlib.pyplot.plot(mag)
matplotlib.pyplot.title("magnitude of DFT")
matplotlib.pyplot.show()

matplotlib.pyplot.plot(phase)
matplotlib.pyplot.title("phase of DFT")
matplotlib.pyplot.show()

"""
3. Modify the frequency spectrum such that the time domain signal will be
shifted by 270 samples to the right.  
"""
from math import pi
# x[n+s] => phase X[f] + 2πsf, where is is a fraction of the sampling rate from 0 to .5
phase_shifted = [phase_val + -2*pi*270*(f/512) for f,phase_val in enumerate(phase)]
#print(phase)
#print(phase_shifted)

"""
4. Take the Inverse DFT of the modified spectrum. Plot the resulting time
domain signal. Has the signal shifted as expected? Has aliasing occurred?
Explain. 
"""
# The signal has shifted as expected, however the signal has also wrapped
# back around to the start
real, imag = polar_to_rect(mag, phase_shifted)
shifted_signal = IDFT(real, imag)
matplotlib.pyplot.plot(shifted_signal)
matplotlib.pyplot.title("shifted signal")
matplotlib.pyplot.show()






"""
Modulation and frequency domain aliasing.

For each of the following steps, plot the time domain signal, calculate the
DFT, and plot the magnitude. 
"""

"""
5. Generate and plot the following 512 sample signal, calculate the DFT, and
plot the magnitude. 

x[n] = exp(-(n-200)^2/900)  sin(2 pi n 0.027) + 0.08
"""
from math import sin, exp, pi
x1 = [exp((-(n-200)**2)/900) * sin(2*pi*n*0.027) + 0.08 for n in range(512)]
real1, imag1 = DFT(x)
mag1, phase1 = rect_to_polar(real, imag)
matplotlib.pyplot.plot(mag1)
matplotlib.pyplot.title("magnitude of exp((-(n-200)**2)/900) * sin(2*pi*n*0.027) + 0.08")
matplotlib.pyplot.show()

"""
6. Generate and plot the following 512 sample signal, calculate the DFT, and
plot the magnitude. 


x[n] =  sin(2 pi n 0.3125) 
"""
x2 = [sin(2*pi*n*0.3125) for n in range(512)]
real2, imag2 = DFT(x2)
mag2, phase2 = rect_to_polar(real2, imag2)
matplotlib.pyplot.plot(mag2)
matplotlib.pyplot.title("magnitude of sin(2*pi*n*0.3125)")
matplotlib.pyplot.show()


"""
7. Multiply the time domain signals created in steps 5 and 6, plot,
calculate the DFT, and plot the magnitude.  On your plot, identify the upper
sideband, the lower sideband, and the carrier wave.  Has aliasing occurred?
"""
# No aliasing as there is nothing at .5
x3 = [a*b for a,b in zip(x1,x2)]
real3, imag3 = DFT(x3)
mag3, phase3 = rect_to_polar(real3, imag3)
matplotlib.pyplot.plot(mag3)
matplotlib.pyplot.title("magnitude of (exp((-(n-200)**2)/900) * sin(2*pi*n*0.027) + 0.08) * sin(2*pi*n*0.3125)")
matplotlib.pyplot.show()

"""
8.  Repeat (6), except using a frequency of 0.4922 for the sinusoid (instead
of 0.3125).  Has aliasing occurred?  Why are their two peaks to the left of
the carrier wave, instead of only one? Explain.
"""
# Looks aliased, there is no wave to the right of the carrier as we overflowed out
# of the period. There are two peaks to the left of the carrier because the 
# right peak overflows outside the period and reappears on the left. The left most
# peak is the actual lower sideband. The other one is from aliasing. (You can math it out,
# the sideband peaks are about 15 samples away from carrier peak, the carrier peak is about
# 5 samples away from the edge of the period, so the upper sideband would appear 10 samples
# OUTSIDE the period, so it reappears / aliases in 10 samples before the end of the period)
x2 = [sin(2*pi*n*0.4922) for n in range(512)]
x3 = [a*b for a,b in zip(x1,x2)]
real3, imag3 = DFT(x3)
mag3, phase3 = rect_to_polar(real3, imag3)
matplotlib.pyplot.plot(mag3)
matplotlib.pyplot.title("magnitude of (exp((-(n-200)**2)/900) * sin(2*pi*n*0.027) + 0.08) * sin(2*pi*n*0.3125)")
matplotlib.pyplot.show()



