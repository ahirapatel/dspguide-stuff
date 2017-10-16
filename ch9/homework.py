#!/usr/bin/env python3

"""
CHAPTER 9: APPLICATIONS OF THE DFT
"""

"""
1. There are three signals involved in linear systems: the input signal
(containing information we want to understand), the impulse response
(controlling how the information is modified), and the output signal (a
result of the other two signals).  It is not a coincidence that the DFT has
three main uses.  Match each DFT techniques with its corresponding signal.
Explain how each DFT technique provides a way of understood or dealing with
the associated signal.
"""
# (I think he's referring to these 3 things as the chapter header talks about 3 things)
# (I have no idea though)
# Look at frequency spectrum of input to understand characteristics of the wave
# Get system's frequency response via DFT and impulse
# FFT Convolution to get the output using input + impulse.
# FFT Convolution to get the input if you have output and impulse

"""
2. A scientist acquires 65,536 samples from an experiment at a sampling rate
of 1 MHz.  He knows that the signal contains a sinusoid at 100 kHz.  He
needs to determine is if there is a second sinusoid at 103 kHz.  As a start,
he takes a 65,536 point DFT of the signal.  To his surprise, all he can see
in the spectrum is noise.  He estimates that the signal he is looking for is
4 times lower in amplitude than the random noise (i.e., SNR = 0.25). He also
estimates that the SNR will need to be at least 3.0 for the signal to be
detected, if present.  To improve the SNR, he decides to break the signal
into segments, and average their spectra.  Arrange your answers to the
following questions in a table. 

a. If he uses a segment length of 16,384 samples, what will be the frequency
resolution (i.e., the spacing between data points) in the averaged spectrum?
Give your answer in hertz.  How many segments will be averaged?  What is the
SNR of the averaged spectrum?  Does this have the required frequency
resolution?  Does this have the required SNR?

b. Repeat for segment lengths of: 8192, 4096, 2048, 1024, 512, 256, and 128.
"""
# Random noise reduces in proportion to the square-root of the number of segments
#     sqrt(num_segments)
#     So two segments yields noise/sqrt(2)
# Signal is estimated to be 4 times lower in amplitude than noise, so we
#     need noise/sqrt(16), but that is still making noise and desired signal at
#     same level, so we need to go further.

# N samples in domain yields N/2+1 samples in frequency domain
# 1 MHz == 1000000 Hz == 1000000 samples/second

# 16,384 yields 8193 samples in frequency domain
# 1000000/8193 = 122.055 Hz bands
# 4 segments
# SNR = 1/(4/sqrt(4)), 4*noise because it is estimated to be 4 times larger
# SNR = 1/2
# 122.055 Hz bands are enough to distinguish 100kHz and 103kHz
#### Remember, the frequency band samples are in the middle of the band, so sample N would span
#### 122.055/2 Hz to the left and 122.055/2 Hz to the right of the sample

# 8192 yields 4097 samples in frequency domain
# 1000000/4097 = 244.081 Hz bands
# 8 segments
# SNR = 1/(4/sqrt(8)), 4*noise because it is estimated to be 4 times larger
# SNR = .707
# 244.081 Hz bands are enough to distinguish 100kHz and 103kHz

# 4096 yields 2049 samples in frequency domain
# 1000000/2049 = 488.043 Hz bands
# 16 segments
# SNR = 1/(4/sqrt(16)), 4*noise because it is estimated to be 4 times larger
# SNR = 1
# 488.043 Hz bands are enough to distinguish 100kHz and 103kHz

# 2048 yields 1025 samples in frequency domain
# 1000000/1025 = 975.610 Hz Bands
# 32 segments
# SNR = 1/(4/sqrt(32)), 4*noise because it is estimated to be 4 times larger
# SNR = 1.414
# 975.610 Hz bands are enough to distinguish 100kHz and 103kHz
# The desired bands would go from APPROXIMATELY 99.5kHz to 100.5kHz, and 102.5kHz to 103.5kHz
# (use a for loop to get bands cuz I was lazy)

# 1024 yields 513 samples in frequency domain
# 1000000/513 = 1949.318 Hz Bands
# 64 segments
# SNR = 1/(4/sqrt(64)), 4*noise because it is estimated to be 4 times larger
# SNR = 2
# 1949.318 Hz bands are enough (sort of) to distinguish 100kHz and 103kHz
# The desired bands would go from APPROXIMATELY 100kHz to 102kHz, and 102kHz to 104kHz
# (use a for loop to get bands cuz I was lazy)
# Spectral leakage may impact this and mush the two desired bands

# 512 yields 257 samples in frequency domain
# 1000000/257 = 3891.051 Hz Bands
# 128 segments
# SNR = 1/(4/sqrt(128)), 4*noise because it is estimated to be 4 times larger
# SNR = 2.828
# 3891.051 Hz bands are NOT enough to distinguish 100kHz and 103kHz

# 256 yields 129 samples in frequency domain
# 1000000/129 = 7751.938 Hz Bands
# 256 segments
# SNR = 1/(4/sqrt(256)), 4*noise because it is estimated to be 4 times larger
# SNR = 4
# 7751.938 Hz bands are NOT enough to distinguish 100kHz and 103kHz

# 128 yields 65 samples in frequency domain
# 1000000/65 = 15384.615 Hz Bands
# 512 segments
# SNR = 1/(4/sqrt(512)), 4*noise because it is estimated to be 4 times larger
# SNR = 5.657
# 15384.615 Hz bands are NOT enough to distinguish 100kHz and 103kHz

"""
3. If the scientist in the last problem wanted to improve this experiment,
what advice could you give?  
"""
# Increase the number of samples, because the averaging technique WITH MORE SAMPLES
# would improve the frequency resolution and the noise

"""
4. A filter kernel (impulse response) consists of 250 samples, and is
designed to pass all frequencies below 0.11, and block all frequencies above
0.12. To evaluate how this filter performs, you want to closely inspect its
frequency response over this range.  To do this, you pad the impulse
response with zeros to make the total length 256 samples, and then take the
DFT. 

a. How many data points are spread over the range of interest? 
b. Repeat using a DFT length of 2048. 
c. Repeat using a DFT length of 2 to the 50th power.  
d. Is there anything limiting how many samples can be placed over this range
of interest? How does this relate to the DTFT? Explain.
"""
# a. .11 * 256 = 28.16 => 28, .12 * 256 = 30.72 => 30
# b. .11 * 2048 = 225.28 => 225, .12 * 2048 = 245.76 => 245
# c. .11 * 2^50 = 123848989752688.64 => 123848989752688, .12 * 2^50 = 135107988821114.88 => 135107988821114
# d. How long it takes to do a DFT. This relates to the DTFT in that the DTFT works on aperiodic signals,
#    if you keep adding zeroes, you make it more and more aperiodic seeming (a period of length infinite).

"""
5. A signal containing 1000 points is to be convolved with a signal
containing 128 points.

a. What is the length of the resulting signal?
b. If frequency domain convolution is used, what length of DFT is
appropriate?
c. If a 1024 point DFT is used, how many samples are correct, and how many
are corrupted by circular convolution?
d. Repeat (a) to (c) for the two signals having 490 samples and 23 samples. 
"""
# a. N+M-1 = 1000+128-1 = 1127
# b. 2048 would be the nearest power of 2 (which is nice for FFTs), but anything greater
#    than or equal to 1127 should do it just fine
# c. 1127 - 1024 = 103, 103 samples at the start of the DFT will be corrupted, and you 
#    will miss the 103 points of convolution data points that should have been at the end
# d. 490+23-1 = 512. A 512 point DFT will work just fine.
