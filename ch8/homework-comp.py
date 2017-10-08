#!/usr/bin/env python

import matplotlib.pyplot

"""
CHAPTER 8: THE DISCRETE FOURIER TRANSFORM
"""

"""
1. Generate and plot a 512 point test signal:

x[n] = (sin(2 pi n 0.08) + 2 sin(2 pi n 0.3)) exp(-(n-200)^2 / 60^2)

This signal is composed of two sinusoids, with frequencies of 0.08 and 0.3,
multiplied by a Gaussian, with a standard deviation of 60.  Each sinusoid
produces a peak in the frequency domain, while the Gaussian makes these
peaks wider and more uniform (more about this in Chapter 9).  
"""
from math import pi, sin, exp
x = [(sin(2*pi*n*0.08) + 2*sin(2*pi*n*0.3))*exp(-(n-200)**2 / 60**2)
     for n in range(512)]

matplotlib.pyplot.plot(x, marker='.')
matplotlib.pyplot.title("That test signal")
matplotlib.pyplot.show()

"""
2. Take the DFT of this signal.  Plot the real and imaginary parts.  These
plots contain the same information that is contained in the time domain. Is
the information in a form that humans can easily understand? Explain, using
these plots as an example.
"""
# You can get a general picture of what it means. The negative frequencies
# and imaginary part are still confusing to me though.
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

real, imag = DFT(x)

matplotlib.pyplot.stem(real)
matplotlib.pyplot.title("real dft output")
matplotlib.pyplot.show()

matplotlib.pyplot.stem(imag)
matplotlib.pyplot.title("imag dft output")
matplotlib.pyplot.show()

#from numpy.fft import rfft
#real = rfft(x)
#matplotlib.pyplot.stem(real)
#matplotlib.pyplot.title("real fft from numpy output")
#matplotlib.pyplot.show()

"""
3. Convert the frequency spectrum into polar form. Plot the magnitude on a
linear amplitude scale. Is this information in a form that humans can easily
understand? Explain.
"""
# Yes, its easy enough to understand
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

mag, phase = rect_to_polar(real, imag)
matplotlib.pyplot.plot(mag, marker='.')
matplotlib.pyplot.title("Magnitude of DFT in polar form")
matplotlib.pyplot.show()

"""
4. Plot the magnitude on a log amplitude scale. Do the samples between the
two peaks have a value of zero?  Explain. 
"""
# No. Noise.
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.plot(mag, marker='.')
matplotlib.pyplot.title("Log magnitude of DFT in polar form")
matplotlib.pyplot.show()
matplotlib.pyplot.yscale('linear')

"""
5. Plot the phase signal. Identify those sections of the phase that are
meaningful, and those sections that are nothing more than meaningless noise.
"""
# Not sure? I imagine everywhere but around 50 and 150 are the noise?
matplotlib.pyplot.plot(phase, marker='.')
matplotlib.pyplot.title("Phase of DFT in polar form")
matplotlib.pyplot.show()

"""
6. Unwrap the phase in the meaningful sections, and plot.  Does this
unwrapping make the phase easier to understand? Explain.
"""
# What are the meaningful sections? Not 100% certain here.
def unwrap_phase(phase):
    from math import pi
    unwrapparoni = [0] * len(phase)
    for i in range(1,len(phase)):
        c = round((unwrapparoni[i-1] - phase[i]) / (2*pi))
        unwrapparoni[i] = phase[i] + c*2*pi
    return unwrapparoni

# Probably off by 1 somewhere in here..
unwrapper = [0]*29 + unwrap_phase(phase[30:51]) + \
            [0]*(145-51) + unwrap_phase(phase[146:160]) + \
            [0]*(256-160)
matplotlib.pyplot.plot(unwrapper, marker='.')
matplotlib.pyplot.title("Phase unwrapping of DFT in polar form")
matplotlib.pyplot.show()

"""
7. Convert the polar frequency spectrum back into rectangular notation, and
then take the Inverse DFT.  Compare the resulting time domain signal with
the original?  Are they identical?  Plot the difference between the two
signals, and explain why it is not entirely zero. 
"""
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


def polar_to_rect(mag, phase):
    from math import sin, cos

    real = []
    imag = []
    for m, p in zip(mag, phase):
        real.append(m * cos(p))
        imag.append(m * sin(p))

    return real, imag

real_syn, imag_syn = polar_to_rect(mag, phase)
orig_sig = IDFT(real_syn, imag_syn)


#from numpy.fft import fft, ifft
#orig_sig = ifft(fft(x))
#orig_sig = IDFT(real, imag)

delta = [b-a for a, b in zip(orig_sig, x)]

matplotlib.pyplot.plot(x)
matplotlib.pyplot.plot(orig_sig)
matplotlib.pyplot.plot(delta)
matplotlib.pyplot.title("original signal, reconstructed signal, and delta")
matplotlib.pyplot.show()

