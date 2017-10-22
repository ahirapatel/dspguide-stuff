#!/usr/bin/env python3
"""
CHAPTER 11: FOURIER TRANSFORM PAIRS
"""
import matplotlib.pyplot
from math import sin, cos, pi, exp
from numpy import arange

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

def polar_DFT(data):
    # * is argument unpacking operator. Neat I guess.
    return rect_to_polar(*DFT(data))


"""
1. Give the mathematical equation for the frequency domain corresponding to
the following waveforms.  You can state your answer in either rectangular or
polar form. Example: x[n] = delta[n], answer: Mag X[f] = 1, Phase X[f] = 0.

a. x[n] = 2delta[n-2]
b. x[n] = sin(2 pi n 14 / 256)
c. x[n] = cos(2 pi n 0.2)
d. x[n] = 1 for 10 < n < 18, 0 otherwise
e. The signal in (d) convolved with itself
f. A Gaussian centered at sample 100, with a standard deviation of 20.
g. The signal in (f) multiplied by a cosine wave of frequency 0.3.
"""
# shifted to the right TWO, so we will see ONE whole period
# when f goes from 0 to .5
# a. Real X[f] = 2*cos(2*2*pi*f), Imag X[f] = -2*sin(2*2*pi*f)
# b. Real X[f] = 0, Imag X[f] = delta[f-14/256] 
# c. Real X[f] = delta[f-.2], Imag X[f] = 0
# d. 7 samples from where signal is high.
#    Mag X[f] = abs(sin(pi*f*7) / sin(pi*f)), X[0] = M, Phase X[f] = bunch of zigs and zags
# e. Yields a triangle wave when convolved with itself. Which is sinc squared in frequency
#    domain. Additionally, convolving in time is multiplication in frequency.
#    Mag X[f] = abs(sin(pi*f*7) / sin(pi*f))^2, Phase X[f] = spikes and stuff
# f. Gaussian in time yields gaussian in frequency. 2*pi*std_of_frequency = 1/std_of_time
#    So solving that yields std_of_frequency = 1/(20*2*pi) = 1/(40*pi). See equation
#    2-8 for the gaussian function (apparently the above stdev relation only holds if you
#    ignore aliasing)
#    Mag X[f] = gauss(f, mean=0, std=1/(40*pi)), Phase X[f] = Jaggedys
# g. Shifts the gaussian to be centered around .3
#    Mag X[f] = gauss(f-.3, mean=0, std=1/(40*pi)), Phase X[f] = Jaggedys

#a = [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#b = [cos(2*pi*x*.2) for x in arange(500)]
#d = [0]*10 + [1]*7 + [0]*1000
#real, imag = DFT(d)
#mag, phase = rect_to_polar(real, imag)
#matplotlib.pyplot.plot(mag)
#matplotlib.pyplot.show()


"""
2. Those experienced in DSP and electronics can approximate the highest
frequency contained in a signal simply by look at its graph.  This problem
will help you master this useful skill.  In general, the most rapidly
changing sections of a signal will correspond to the highest frequency
contained in the signal.  As an example, the sinc function in Fig. 11-5a has
a period of about 11 samples.  This corresponds to the highest frequency
present in the signal being about 1/11 = 0.09.  In a more realistic example,
Figs. (c) and (d) show waveforms that resemble one-half cycle of a sinusoid
being completed over 16 cycles.  This corresponds to one cycle every 32
samples, or a highest frequency of 1/32 = 0.03. Use this method to estimate
the highest frequency component in the following signals:
  
a. Fig. 7-14, y[n]
b. Fig. 8-8b
c. Fig. 9-7a
d. Fig. 11-6b-d
e. Fig. 3-5a (for "time" in seconds)
f. Fig. 10-14a
g. Fig. 13-8a
h. A signal where each sample is obtained from a random number generator.
i. In some of the above figures, the actual frequency spectra are also
given. Using this information, approximately how accurate is this method?
(Choose from 1%,3%,10%, or 30%)
"""
# TODO: Check with an actual DFT
# a. 1/20 = .05
# b. maybe 12 or 16 per cycle, 1/16 = .0625
# c. fastest cycle is about 4 samples? 1/4 = .25f
# d. b->1/1024, c->1/512, d->1/128
# e. maybe half a second to complete fastest cycle, 1/.5 = 2 Hz
# f. 1/.4ms = 2.5kHz (the picture shows this is sorta close)
# g. about 15ms per cycle, 1/20ms = 50 Hz (picture says this is horribly off)
# h. NOISY, should have frequencies all over the spectrum
# i. eh

"""
3. A signal contains 16 consecutive samples with a value of 1, with the
remainder of the samples having a value of zero.  

a. What are the frequencies of the first four zeros crossings in the
frequency domain?  
b. What are the periods of these frequencies?
c. Make a sketch showing how sinusoids at the first two zero crossings fit
evenly inside the rectangular pulse.
"""
# 1 period fits in 16 samples for 1/16 freq, 2 periods fit in 16 samples for 2/16 freq, etc.
# a.1/16, 2/16, 3/16, 4/16
# b.16 samples, 8 samples, 5.333 samples, 4 samples
# c. eh, no. It's easy to visualize in my noggin.

#rect = [1]*16 + [0]*144
#mag, phase = polar_DFT(rect)
#matplotlib.pyplot.plot(mag)
#matplotlib.pyplot.show()

"""
4.  A discrete sinusoid of frequency 0.125 is half-wave rectified (that is,
all the negative valued samples are set to zero). 

a. Sketch the original time domain signal and its frequency spectrum.
b. Sketch the rectified time domain signal and its frequency spectrum (don't
worry about the exact amplitude of the harmonics).
c. Which harmonics of the rectified signal will be aliased?
d. At what frequency does the 5th harmonic appear?
e. At what frequency does the 10th harmonic appear?
f. At what frequency does the 100th harmonic appear?  
"""
# a.
sin_sig = [sin(2*pi*.125*x) for x in arange(64, step=.0625)]
matplotlib.pyplot.plot(sin_sig)
matplotlib.pyplot.show()

mag, phase = polar_DFT(sin_sig)
matplotlib.pyplot.plot(mag)
matplotlib.pyplot.show()

# b.
sin_rect = [0 if x < 0 else x for x in sin_sig]
matplotlib.pyplot.plot(sin_rect)
matplotlib.pyplot.show()

mag, phase = polar_DFT(sin_rect)
matplotlib.pyplot.plot(mag)
matplotlib.pyplot.show()

# c. There appear to only be odd harmonics, but there is also one
#    at sample 16 for some reason.
#    It seems half wave rectifying also makes it appear as if there
#    is a DC offset, where spectrum[0] has a non-zero amplitude

# I don't know if I include the harmonic at sample 16 for d-f, let's assume not?
# d. 2*5f
# e. 2*10f
# f. 2*100f

"""
5. Referring to the chirp system in Fig. 11-10:  

a. What is the frequency domain magnitude of the signal in (a)?  Of the
signal in (b)?
b. What is the frequency domain phase of the signal in (a)?  Of the signal
in (b)? (express these answers as equations using the constants alpha and
beta).
c. Using Parseval's relation, what is the relationship between the total
energy contained in the waveforms in (a) and (b)? Explain.
d. Recall from physics that power is equal to the total energy released
divided by the time over which it is released. If the waveform in (a) is one
sample long, and the waveform in (b) is 80 samples long, what power
reduction is provided by this chirp system?
"""
# a. 1, 1*sin(2*pi*f), because impulse's DFT is sinusoidal?
# b. ak+bk^2,0+ak+bk^2, phase of delta[n] is 0, so add 0?
# c. The area under the input signal's curve squared equals the output signal's curve squared
#    Squaring is because we want a magnitude
# d. a would be 1/1 = 1, b would be on average 1/80 * 80 samples = 1
#    Or I do I need to solve for 1/x^2 * 80 = 1? Hmmm
 
"""
6. Figures 11-5 (a) and (e) illustrate a sinc function and a Gaussian,
respectively. Both these functions decrease in amplitude toward the left and
right. However, neither of these functions ever reach a constant value of
zero.

a. Write an equation describing how the amplitude of the sinc's oscillations 
decrease, moving away from the center of symmetry. 
b. Repeat (a) for the Gaussian (estimating the standard deviation from the
figure). 
c. When the main lobes are about the same width [as illustrated in Figs. (a)
and (e)], which of these two functions drops toward zero faster?  To answer
this, evaluate the amplitude of the two functions at 3, 10, 30, 100, and 300
samples from the center of symmetry.
d. For each function, how many samples must you move away from the center of
symmetry before the amplitude fall below the single precision round-off
noise? 
e. Would a Gaussian or a rectangular pulse in the frequency domain be more
likely to result in time domain aliasing? Explain.
f. Would a Gaussian or a rectangular pulse in the time domain be more likely
to result in frequency domain aliasing? Explain.
"""
# a. Wouldn't I just give a shifted sinc function?
# b. Wouldn't I just give a shifted gaussian with a mean of 40 and stdev of about maybe 2?
# c. The sinc seems to.
# d. Pretty far for sinc
# f. Rectangular pulse?
# g. Rectangular pulse?



