#!/usr/bin/env python3

"""
CHAPTER 7: PROPERTIES OF CONVOLUTION

The exercise looks at two different ways of detect a known waveform in a
noisy signal.  The waveform to be detected is an exponentially decaying
pulse. The first detection method is to threshold the first difference of
the signal.  The second method is to threshold the correlation of the signal
with the known waveform. 

1.  Generate a 600 sample test signal, containing three target pulses:

x[n] =  exp(-(n-100)/15), if   99 < n < 160
     =  exp(-(n-300)/15), if  299 < n < 360
     =  exp(-(n-500)/15), if  499 < n < 560
     =  0, otherwise
"""
from math import exp
import matplotlib.pyplot

siggy = [exp(-(n-100)/15) if 99 < n < 160 else
     exp(-(n-300)/15) if 299 < n < 360 else
     exp(-(n-500)/15) if 499 < n < 560 else
     0
     for n in range(600)]

matplotlib.pyplot.plot(siggy, marker='.')
matplotlib.pyplot.title("3 spikes")
matplotlib.pyplot.show()

"""
2. Generate a 600 sample signal of normally distributed random noise with
mean = 0, and SD = 1.
"""
import random
#               gauss(mean,std)
rands = [random.gauss(0,1) for _ in range(600)] 

# Double check I'm not a goober
#from statistics import stdev
#print("stdev {}, average {}".format(stdev(rands), sum(rands)/len(rands)))

"""
3. Generate four test signals with signal-to-noise ratios (SNRs) of 50, 10,
5, and 2.5. Do this by adding the signal from step 1, with an appropriately
scaled version of the noise from step 2. For this problem, we will define
the SNR to be equal to the peak amplitude of the target waveform (which is
one), divided by the standard deviation of the noise.  Plot these four test
signals.
"""
# SNR(50) == 1/stdev == 1/.02
# SNR(10) == 1/stdev == 1/.1
# SNR(5) == 1/stdev == 1/.2
# SNR(2.5) == 1/stdev == 1/.4
snr50    = [(50**-1)  * r + s for r,s in zip(rands, siggy)]
snr10    = [(10**-1)  * r + s for r,s in zip(rands, siggy)]
snr5     = [(5**-1)   * r + s for r,s in zip(rands, siggy)]
snr2half = [(2.5**-1) * r + s for r,s in zip(rands, siggy)]

matplotlib.pyplot.plot(snr2half, marker='.')
matplotlib.pyplot.plot(snr5, marker='.')
matplotlib.pyplot.plot(snr10, marker='.')
matplotlib.pyplot.plot(snr50, marker='.')
matplotlib.pyplot.legend(("with SNR of 2.5", "with SNR of 5", "with SNR of 10", "with SNR of 50"))
matplotlib.pyplot.title("four random signals added to spikes")
matplotlib.pyplot.show()

"""
4. Calculate and plot the first difference of the four test signals.
"""
# Input side algorithm for convolution
def convolve(input_sig, impulse_response):
    convolution_out_len = len(input_sig) + len(impulse_response) - 1
    y = [0] * convolution_out_len
    for i, in_sample in enumerate(input_sig):
        for j, impulse_sample in enumerate(impulse_response):
            y[i+j] += in_sample * impulse_sample
    return y

def first_difference(samples):
    # Do first difference in terms of convolution.
    first_diff_impulse = [1, -1, 0, 0, 0, 0]
    return convolve(samples, first_diff_impulse)

diff50 = first_difference(snr50)
diff10 = first_difference(snr10)
diff5 = first_difference(snr5)
diff2half = first_difference(snr2half)
matplotlib.pyplot.plot(diff2half, marker='.')
matplotlib.pyplot.plot(diff5, marker='.')
matplotlib.pyplot.plot(diff10, marker='.')
matplotlib.pyplot.plot(diff50, marker='.')
matplotlib.pyplot.legend(("with SNR of 2.5", "with SNR of 5", "with SNR of 10", "with SNR of 50"))
matplotlib.pyplot.title("spikes plus four random signals's's's first difference")
matplotlib.pyplot.show()

"""
5. Calculate and plot the correlation of each of the four signals with the
60 point target signal.  (Check your program by making sure that the peaks
have the proper symmetry).
"""
# Correlation is just input signal[n] ✴ target[-n]
def correlate(input_sig, target):
    return convolve(input_sig, target[::-1]) # [::-1] will reverse the list

target = [exp(-n/15) for n in range(60)]
#print(target)
matplotlib.pyplot.plot(target, marker='.')
matplotlib.pyplot.title("the 60 point target signal to be cross correlated")
matplotlib.pyplot.show()

# It looks symmetric when plotting.
corr50 = correlate(snr50, target)
corr10 = correlate(snr10, target)
corr5 = correlate(snr5, target)
corr2half = correlate(snr2half, target)
matplotlib.pyplot.plot(corr2half, marker='.')
matplotlib.pyplot.plot(corr5, marker='.')
matplotlib.pyplot.plot(corr10, marker='.')
matplotlib.pyplot.plot(corr50, marker='.')
matplotlib.pyplot.legend(("with SNR of 2.5", "with SNR of 5", "with SNR of 10", "with SNR of 50"))
matplotlib.pyplot.title("correlations with target siggy")
matplotlib.pyplot.show()

# Let's plot it wrong without doing the index negation on the target just
# to see what it looks like.
# It does NOT look symmetric when plotting.
corr50 = convolve(snr50, target)
corr10 = convolve(snr10, target)
corr5 = convolve(snr5, target)
corr2half = convolve(snr2half, target)
matplotlib.pyplot.plot(corr2half, marker='.')
matplotlib.pyplot.plot(corr5, marker='.')
matplotlib.pyplot.plot(corr10, marker='.')
matplotlib.pyplot.plot(corr50, marker='.')
matplotlib.pyplot.legend(("with SNR of 2.5", "with SNR of 5", "with SNR of 10", "with SNR of 50"))
matplotlib.pyplot.title("correlations with target siggy BUT DONE WRONG (target index isn't negated)")
matplotlib.pyplot.show()

"""
6. Based on your results, estimate the minimum SNR that the signal must have
in order to reliably detect the target by:

a. a visual inspection of the waveform
b. thresholding the first difference
c. thresholding the correlation signal
"""
# a. Visually you can tell for each of the SNRs, but all but SNR50 look janky
# b. SNR 50, SNR 10 are pretty good if you put a threshold on it, the rest are iffy.
# c. They are all pretty good and easy to see using correlation
