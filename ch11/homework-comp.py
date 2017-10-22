#!/usr/bin/env python3

import matplotlib.pyplot

"""
CHAPTER 11: FOURIER TRANSFORM PAIRS
"""
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

def polar_DFT(data):
    # * is argument unpacking operator. Neat I guess.
    return rect_to_polar(*DFT(data))


# Could've probably used numpy, but let's use that new found DSP knowledge
# Also this seems like a mediocre implementation in terms of performance
# and correctness...
def get_area_under_curve(curve):
    # The running sum impulse needs to be of infinite length technically,
    # but obviously I cannot do that, so just make it huge
    integral = convolve(curve, [1]*1000)
    #print(integral)
    return abs(integral[len(integral) // 2])

def calc_gauss(mean, std, x):
    """
    From equation 2-8 in the book
    """
    scale = 1 / (sqrt(2*pi)*std)
    power = -(x-mean)**2 / (2*(std**2))
    e = exp(power)
    return scale * e

def get_normalized_rectangle():
    rectangle = [0] * 178 + [1] * 45 + [0] * 289
    area = get_area_under_curve(rectangle)
    rectangle = [x / area for x in rectangle]
    return rectangle

def get_normalized_triangle():
    triangle = [0] * 178 + [-abs(x) + 22 for x in range(-22,23)] + [0] * 289 # y = -|x| + 22
    area = get_area_under_curve(triangle)
    triangle = [x / area for x in triangle]
    return triangle

def get_normalized_triangle_MODDED():
    triangle = [0] * 167 + [-abs(x) + 33 for x in range(-33,34)] + [0] * 278 # y = -|x| + 22
    area = get_area_under_curve(triangle)
    triangle = [x / area for x in triangle]
    return triangle

def get_normalized_gauss():
    gauss = [calc_gauss(200, 13.5, x) for x in range(512)]
    area = get_area_under_curve(gauss)
    gauss = [x / area for x in gauss]
    return gauss

def get_normalized_hamming():
    # Is hamming supposed to be zero padded? It seems weird on the outside.
    hamming = [0]*167 + [(.54 - .46*cos(2*pi*i/66)) for i in range(67)] + [0]*278 # M = 66, get 67 elems from 0 to 66
    area = get_area_under_curve(hamming)
    hamming = [x / area for x in hamming]
    return hamming

"""
1. Generate the following waveforms, each 512 samples long, centered on
sample 200. Normalize the amplitude of each waveform to give it unity area.

a. Rectangular pulse, 45 samples wide  (i.e., 45 nonzero values)
b. Triangular pulse, 45 samples wide  (i.e., 43 nonzero values)
c. Gaussian, standard deviation = 13.5
e. Hamming window, M = 66 (see Eq. 16-1 and Fig. 16-2a)
"""
# Unity AREA so divide by area under the curve.
from math import pi, exp, sqrt, cos
rectangle = get_normalized_rectangle()
triangle = get_normalized_triangle()
gauss = get_normalized_gauss()
hamming = get_normalized_hamming()

#print(len(rectangle))
#matplotlib.pyplot.plot(rectangle)
#matplotlib.pyplot.show()
#print(len(triangle))
#matplotlib.pyplot.plot(triangle)
#matplotlib.pyplot.show()
#print(len(gauss))
#matplotlib.pyplot.plot(gauss)
#matplotlib.pyplot.show()
#print(len(hamming))
#matplotlib.pyplot.plot(hamming)
#matplotlib.pyplot.show()

"""
2. Calculate the DFT of each waveform and convert to polar form.
"""
rectangle_mag, rectangle_phase = polar_DFT(rectangle)
triangle_mag, triangle_phase = polar_DFT(triangle)
gauss_mag, gauss_phase = polar_DFT(gauss)
hamming_mag, hamming_phase = polar_DFT(hamming)

#matplotlib.pyplot.title("rectangle_mag")
#matplotlib.pyplot.plot(rectangle_mag)
#matplotlib.pyplot.show()
#matplotlib.pyplot.title("triangle_mag")
#matplotlib.pyplot.plot(triangle_mag)
#matplotlib.pyplot.show()
#matplotlib.pyplot.title("gauss_mag")
#matplotlib.pyplot.plot(gauss_mag)
#matplotlib.pyplot.show()
#matplotlib.pyplot.title("hamming_mag")
#matplotlib.pyplot.plot(hamming_mag)
#matplotlib.pyplot.show()

"""
3.  To allow a fair comparison of the four magnitudes, each of these signals
has a "cutoff frequency" equal to 0.01.  That is, the width of each time
domain waveform is selected to make the magnitude have a value of 0.707 at
sample 5 (i.e., 5/512  = 0.01).  However, one of these four signals is
incorrect, it does not have a cutoff frequency of 0.01.  Identify which of
the four is incorrect, and modify it so that it does have a cutoff frequency
of 0.01.  Explain your modification.
"""

# The cutoff at sample 5
print("Rectangle magnitude at desired cutoff", rectangle_mag[5])
print("Triangle magnitude at desired cutoff", triangle_mag[5]) # This peanut is off a bit
print("Gauss magnitude at desired cutoff", gauss_mag[5])
print("Hamming magnitude at desired cutoff", hamming_mag[5])

# I just expanded the time domain to compress the frequency domain. (the triangle_mag[5]
# value was high, so I needed to squish it back)
# It wasn't exactly done pragmatically.
# Since DFT(triangle) == sinc squared, I THINK I could've worked backwards doing something like
# k*sinc(x) = .707 at x=5, and found and appropriate scalar for the frequency domain, then
# IDFT'd the signal
triangle = get_normalized_triangle_MODDED()
triangle_mag, triangle_phase = polar_DFT(triangle)
print("Triangle magnitude at desired cutoff after modding", triangle_mag[5])

"""
4. Plot each of the four time domain waveforms (the correct versions), each
of the four magnitudes, and each of the four magnitudes on a logarithmic
amplitude scale. 
"""

matplotlib.pyplot.plot(rectangle)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(triangle)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(gauss)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(hamming)
matplotlib.pyplot.show()

matplotlib.pyplot.title("rectangle_mag")
matplotlib.pyplot.plot(rectangle_mag)
matplotlib.pyplot.show()
matplotlib.pyplot.title("triangle_mag")
matplotlib.pyplot.plot(triangle_mag)
matplotlib.pyplot.show()
matplotlib.pyplot.title("gauss_mag")
matplotlib.pyplot.plot(gauss_mag)
matplotlib.pyplot.show()
matplotlib.pyplot.title("hamming_mag")
matplotlib.pyplot.plot(hamming_mag)
matplotlib.pyplot.show()

matplotlib.pyplot.yscale('log')
matplotlib.pyplot.title("rectangle_mag in log scale")
matplotlib.pyplot.plot(rectangle_mag)
matplotlib.pyplot.show()
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.title("triangle_mag in log scale")
matplotlib.pyplot.plot(triangle_mag)
matplotlib.pyplot.show()
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.title("gauss_mag in log scale")
matplotlib.pyplot.plot(gauss_mag)
matplotlib.pyplot.show()
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.title("hamming_mag in log scale")
matplotlib.pyplot.plot(hamming_mag)
matplotlib.pyplot.show()

"""
5. Suppose that these four waveforms were being used as filter kernels.  The
goal is to pass a signal at frequency 0.005, while blocking noise in the
frequency band of 0.03 to 0.4.  Answer the following.  

a.  Why must the four time domain waveforms be normalized to have the same
area in this comparison?  What would be the affect on the magnitudes if they
were allowed to have different areas?
b. Are any of these four filters better or worse than the others in how well
the signal is passed? Explain.
c. Are any of these four filters better or worse than the others in how well
the noise is blocked? Explain.
d. Which of these four filters is the best for this application?
e.  Which of these four filters is the worst for this application?
"""
# a. It is easier to compare the frequency spectrum's, and rolloff, etc?
#    The magnitudes would be different with different areas (something something
#    Parseval's relationa)
# b. The gaussian seems to pass the signal through the best as it has a more gradual
#    rolloff at the desired .005 frequency (.005 * 512 == 2.56)
# c. Gauss seems to be good at removing noise, however the rolloff takes forever compared
#    to the other filters. Gaussian may not be as desirable due to this.
# d/e. .03 * 512 = 15.36
#    .4 * 512 = 204.8
#    Rectangle seems the worst all around if you look at the rolloff and noise blocking.
#    Triangle also seems bad for the noise blocking.
#    Gauss seems to pass the signal a LITTLE better than hamming and has better noise
#    attentuation after the gaussian rolls off completely. The hamming rolls off faster
#    but has a spectrum with oscillations that are much higher than gauss in the cutoff
#    range. I'd probably try both and see what seems better. If I had to choose here
#    I'd probably say hamming, as the amplitudes of the oscillations later in the spectrum
#    are pretty darn small.
