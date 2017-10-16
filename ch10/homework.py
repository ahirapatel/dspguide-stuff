#!/usr/bin/env python3

"""
CHAPTER 10: PROPERTIES OF THE DFT
"""

"""
1. If x[n] has the frequency domain: Xreal[f] and Ximag[f], and y[n] has the
frequency domain: Yreal[f] and Yimag[f], calculate the frequency domain of
the following signals:

a. x[n]/5
b. 5.5y[n]
c. x[n] + y[n] 
d. 3.14x[n] + y[n]/3.14
e. ax[n] + by[n], where a and b are constants
"""
# a. X[f]/5
# b. 5.5Y[f]
# c. X[f] + Y[f]
# d. 3.14X[f] + Y[f]/3.14
# e. aX[f] + bY[f], where a and b are constants
# I guess it wanted me to use Xreal and that stuff, but that just seems straightforward?

"""
2. If x[n] has the frequency domain: Xmag[f] and Xphase[f], and y[n] has the
frequency domain: Ymag[f] and Yphase[f], calculate the frequency domain of
the following signals:

a. x[n-2]
b. 1.2x[n-1]
c. y[n+2]/10
d. ax[n-b],  where a and b are constants
"""
# x[n+s] = Xmag[f], Xphase[f] + 2πsf
# a. Xmag[f], Xphase[f] + -2*2πf
#    Xmag[f], Xphase[f] + -4πf
# b. 1.2Xmag[f], Xphase[f] + -2πf
# c. Ymag[f]/10, Yphase[f] + 4πf
# d. a*Xmag[f], Xphase[f] + -2πbf

"""
3. Regarding the signals in problems 1 and 2:

a. In problem 1, why would it be difficult to calculate the frequency domain
of: x[n-2]?  
b. In problem 2, why would it be difficult to calculate the frequency domain
of x[n] + y[n]?
c. Complete the following statements describing this situation: 
"When time domain signals are added, the frequency domain is easiest to
understand when in [fill in the blank] form."
"When time domain signals are shifted, the frequency domain is easiest to
understand when in [fill in the blank] form."
"When time domain signals are scaled, the frequency domain is easiest to
understand when in [fill in the blank] form."
"""
# a. You cannot use rectangular notation (the Re/Im) with a time domain shift. You
#    would need to convert it to polar notation first, then modify the phase, then
#    convert it back.
# b. You cannot add the frequency spectrum in polar notation, you must convert to 
#    rectangular, add, then back to polar.
# c. Rectangular for addition
#    Polar for shifting
#    Either notation is easy for scaling (although in polar, you only need to scale one set of points)

"""
4. Suppose that the frequency spectrum in Fig 9-2 represents a digital
signal with a sampling rate of 160 Hz. Sketch the digital frequency spectrum
for frequencies between -2.0 and 2.0.  
"""
# SEE NOTEBOOK

"""
5. A digital low-pass filter passes all frequencies below 0.1, and blocks
all frequencies above. 

a. Sketch this frequency response, showing all frequencies between -1.5 and
1.5.
b. If the filter kernel is multiplied by a sine wave with a frequency of
0.3, sketch the new frequency response.
c. Based on the method in (b), describe an algorithm for converting a low-
pass filter with cutoff frequency, fc, into a bandpass filter with a center
frequency, fcenter, and a bandwidth, BW.
d. If the low-pass filter kernel is multiplied by a cosine wave with a
frequency of 0.5, sketch the new frequency response.
e. Based on the method in (d), describe an algorithm for converting a low-
pass filter with cutoff frequency, flp, into a high-pass filter with a
cutoff frequency, fhp. 
f. Why must a cosine wave be used in (e) instead of a sine wave?
"""
# a. See notebook. And figure 10-9 in the book
# b. See notebook. (also I think this means multiply by sine in time domain)
# c. You multiply by a sine you want to shift the center frequency to. eg, the .3 frequency
#    sine shifts the lpf filter portion down to .3. Words are hard.
# d/e. Assuming b means multiply time domain kernel by time domain sine with .3 frequency, 
#      that would be like convolving the frequency by a shifted delta, which would shift
#      the frequency spectrum down. If you shift the frequency spectrum far enough, say
#      with a .5 frequency sine wave, then the lpf frequency response will mirror around
#      .25 frequency. See super bad looking rendering of frequency response in ascii below.
#
#  original sig                       original sig multiplied by .5 freq sinusoid in TIME DOMAIN
# |
# |-------                               -------
# |      |                               |
# |       |                             |
# |        |                           |
# |        |                           |
# |         \                         /
# |_____________________________________________
# 0.0                 .25                     .5
#
# So effectively you just need to multiple by a sine in the time domain to shift the signal, and
# if it is .5 or higher it will shift a MIRRORED version back from .5
# f. No clue? Something to do with sin(0) == 0? The phase?

"""
6. To represent the sound of a human voice, a signal only needs to contain
frequencies between 100 Hz and 4 kHz.  In comparison, high-fidelity music
must contain all the frequencies that humans can hear, i.e., 20 Hz to 20
kHz.  

a. Sketch and label the frequency spectra of these two signals, including
the negative frequencies. Assume all the frequencies have the same
amplitude.
b. A DC bias is often added to audio signals in electronic circuits.  This
is to make the voltage representing the signal always have a positive value
(see Fig. 10-14a). Repeat (a) assuming that each audio signal has such a DC
bias.
c. Sketch the frequency spectrum of a voice signal multiplied by a sine wave
at 1 MHz.  Repeat for a voice signal plus DC bias.
d. Sketch the frequency spectrum of a music signal multiplied by a sine wave
at 1.1 MHz.  Repeat for a music signal plus DC bias.
e. If the signal in (c) is transmitted from a radio station, what band of
frequencies must be assigned by the government to avoid interference with
other radio applications?  Repeat for the signal in (d). 
f. If a frequency band of 50.1 to 50.2 MHz were available, how many voice
signals could be simultaneously transmitted?  How many high-fidelity music
signals?  Explain how the signals would be prepared for this simultaneous
transmission. 
"""
# a. SEE NOTEBOOK
# b. SEE NOTEBOOK
# c. Ugh, pretty much just see figure 10-14 for how this should be
# d. Ugh, pretty much just see figure 10-14 for how this should be
# e. Centered at 1MHz so the band around 1MHz would be (1MHz-4kHz, 1MHz+4kHz)
# f. Using the joys of frequency domain multiplexing, we have from 50.1 to
#    50.2 a .1MHz (100,000Hz) band. Voice needs 4000Hz, so 100000/4000 yields
#    25 simultaneous voice signals, and music needs 20000kHz, so 100000/20000
#    yields 5 simultaneous music signals

"""
7. The "no bias" signal in (c) of the last problem is filtered to remove all
frequencies below 1 MHz. The result is called "single-sideband" (SSB)
modulation. 

a. Sketch the single-sideband frequency spectrum. 
b. Does this contain the same information as the original voice signal?  
c. A disadvantage of SSB is that it requires more complicated modulation and
demodulation electronics. What would be the advantage of using single-
sideband modulation over AM?  
d. If the lower sideband were retained instead, would the information in the
original signal still be preserved? Explain. 
"""
# a. SEE NOTEBOOK
# b. Yes? The negative and positive frequencies below and above the carrier shouldn't
#    both be needed to reconstruct the signal.
# c. A lower band width for transmission of signals. Some other single could occupy the
#    frequency where the other sideband would have been.
# d. Yes, but I THINK you'd have to modify the flipped frequency spectrum to get the
#    info you want.

