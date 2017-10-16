#!/usr/bin/env python3

"""
CHAPTER 9: APPLICATIONS OF THE DFT
"""
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


"""
1. Create a 600 sample test signal: x[n] = cos(2 pi n 8 / 600) exp(n/200). 
Add random noise to this signal, with mean = 0 and SD = 1. Plot this signal.
"""
from math import cos, exp, pi
siggy = [cos(2*pi*n*8/600) * exp(n/200) for n in range(600)]

# I think he means uniform noise and not gaussian?
import random
rands = [random.uniform(-1.75,1.75) for _ in range(600)] # Close enough.
                                                         # unless he meant gaussian noise?
# Double check I'm not a goober
#from statistics import stdev
#print("stdev {}, average {}".format(stdev(rands), sum(rands)/len(rands)))

#randy_siggyton = siggy
#randy_siggyton = rands
randy_siggyton = [a+b for a,b in zip(siggy, rands)]

matplotlib.pyplot.plot(randy_siggyton)
matplotlib.pyplot.title("x[n] = cos(2 pi n 8 / 600) exp(n/200) with noise")
matplotlib.pyplot.show()

"""
2. Create a 9 point impulse response, h[n]: 1/25, 2/25, 3/25, 4/25, 5/25,
4/25, 3/25, 2/25, 1/25.  Plot this signal.  What kind of filter is this?
"""
# I have no idea what kind of filter this is in terms of a name.
# It seems to be a smoothing filter of some kind.
triangle_filter = [1/25, 2/25, 3/25, 4/25, 5/25, 4/25, 3/25, 2/25, 1/25]

matplotlib.pyplot.plot(triangle_filter)
matplotlib.pyplot.title("9 point impulse")
matplotlib.pyplot.show()

"""
3. Calculate and plot the convolution of x[n] and h[n].  How has this
convolution improved the signal?
"""
# It has smoothed out the noise. For lower amplitude signals it still sucks though.
filtered_siggy = convolve(randy_siggyton, triangle_filter)
matplotlib.pyplot.plot(filtered_siggy)
matplotlib.pyplot.title("Convolution with smoothing filter")
matplotlib.pyplot.show()
print(len(filtered_siggy))

"""
4. Pad x[n] with zeros to form a 1024 sample signal, calculate the spectrum,
and plot the magnitude. 
"""
# Uhh, 5 seems to imply I should be plotting the signal WITH noise, but he says x[n]
# in the problems... so I am confused.
for _ in range(1024-len(randy_siggyton)):
    randy_siggyton.append(0)
print(len(randy_siggyton))

real, imag = DFT(randy_siggyton)
mag, phase = rect_to_polar(real, imag)
matplotlib.pyplot.stem(mag)
matplotlib.pyplot.title("DFT of (x[n] = cos(2 pi n 8 / 600) exp(n/200) with noise)")
matplotlib.pyplot.show()

"""
5. In the spectrum of x[n], identify the portion that is mostly signal, and
the portion that is mostly noise.  What characteristic of the noise
generated in step 1 insures that the noise is white? Why does the noise
appear irregular in this spectrum, instead of perfectly flat?  How could you
make the noise appear flatter?
"""
# Hard to describe without the picture. So just plot without the noise added in
# and then boom.
# The noise is white because they are random unrelated values with an equal chance
# of any value being chosen.
# Why is it not flat? I have no clue. I wouldn't have thought it should have been,
# but what do I know?
# Use a different kind of noise like pink or brownian?

"""
6. Pad h[n] with zeros to form a 1024 sample signal, calculate the frequency
response, and plot the magnitude.  Identify the frequencies that are passed
through the filter (> 90% amplitude), those that are partially passed, and
those that are mostly blocked (< 10% amplitude).
"""
# It allows frequencies below ~.0838 (look at sample 43)
# It partially allows frequencies below ~.3080 (look at sample 158)
# Everything else is mostly blocked
for _ in range(1024-len(triangle_filter)):
    triangle_filter.append(0)

real, imag = DFT(triangle_filter)
mag, phase = rect_to_polar(real, imag)
matplotlib.pyplot.stem(mag)
matplotlib.pyplot.title("DFT of padded filter")
matplotlib.pyplot.show()

"""
7. Multiply the frequency spectrum by the frequency response (see Eq. 9-1),
and take the inverse DFT. Is this signal identical to that obtained by
direct convolution?  Test this by subtracting the two signals, and plotting
the result.  Explain the result. 
"""
# The delta is all triangles (or I did something wrong).
# I am not sure why they differ. Hmmm.

# Man these are all terribly named
realT, imagT = DFT(triangle_filter)
realS, imagS = DFT(randy_siggyton)

realO, imagO = [], []
for r_s, i_s, r_t, i_t in zip(realS, imagS, realT, imagT):
    realO.append(r_s*r_t - i_s*i_t)
    imagO.append(i_s*r_t + r_s*i_t)

reconstructed_siggy = IDFT(realO, imagO)

delta = [a-b for a,b in zip(filtered_siggy, reconstructed_siggy)]

matplotlib.pyplot.plot(delta)
#matplotlib.pyplot.plot(reconstructed_siggy)
#matplotlib.pyplot.plot(filtered_siggy)
matplotlib.pyplot.title("delta of time domain convolution and frequency domain multiplication")
matplotlib.pyplot.show()



