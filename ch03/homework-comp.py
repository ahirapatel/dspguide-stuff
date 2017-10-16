#!/usr/bin/env python3

"""
CHAPTER 3: ADC AND DAC
"""


"""
1. Generate a 1000 point digital signal that simulates an analog signal,
consisting of a sine wave at 30.76 hertz, being sampled at 1 kHz for 1
second.  Plot this digital signal with the x-axis labeled "time", running
from 0 to 1 second.  
"""
import matplotlib.pyplot

def sin_wave(sample_rate_hz, duration):
    """
    sample_rate_hz is the sampling rate.. in hertz
    duration is how long you want the signal to run for in seconds

    return a pair of lists with sample time in one list and output values in other
    """
    from math import sin
    from math import pi
    num_samples = sample_rate_hz * duration
    sample_steps = 1 / sample_rate_hz
    xdata, ydata = [], []
    for i in range(num_samples):
        x = i * sample_steps * 2*pi # Convert to radians with 2pi
        y = sin(30.76*x)
        #y = sin(x)
        xdata.append(i*sample_steps) # We want the time in seconds, not the radian values
        ydata.append(y)

    return xdata, ydata

xdata1000hz, ydata1000hz = sin_wave(1000, 1)
matplotlib.pyplot.plot(xdata1000hz, ydata1000hz, marker='.')
matplotlib.pyplot.title('30.76Hz sin wave sampled @ 1000Hz')
matplotlib.pyplot.xlabel('time (seconds)')
matplotlib.pyplot.show()


"""

2. Simulate sampling the analog signal at 200 Hz, by discarding every 4 out
of  5 samples from the digital signal you created in step 1.  
          
a. Plot this resampled signal, with the x-axis labeled as "time", running 
from 0 to 1 second.  
"""
xdata200hz = xdata1000hz[::5]
ydata200hz = ydata1000hz[::5]
#print(len(xdata200hz)) # Check we discard 4 of 5 samples correctly
matplotlib.pyplot.plot(xdata200hz, ydata200hz, marker='.')
matplotlib.pyplot.title('30.76Hz sin wave sampled @ 1000Hz, then decimated to 200Hz')
matplotlib.pyplot.xlabel('time (seconds)')
matplotlib.pyplot.show()
"""
b. Has aliasing occurred in this signal? Explain.
"""
# No, the signal is a 30.76 hz sin wave and we sample at greater than 2 times
# the frequency of the signal. Book definition of nyquist frequency is
# 1/2 the sampling rate. The signal we have is below the nyquist frequency,
# so it would not have aliasing.

"""
c. What is the digital frequency of this signal?
"""
# 30.76 Hz?

"""
d. Could the original analog signal be reconstructed from this digital 
signal?
"""
# Yes, as it is not aliased / data is not lost. The shape of the waveform is a 
# little jaggedy, but we can still recreate it.


"""
3. Repeat #2 with the sampling at 50 Hz, 33.33 Hz, and 28.57 Hz.
"""

"""

50 Hz

"""
"""
b. Has aliasing occurred in this signal? Explain.
"""
# Yes, it does not fit the requirements of the nyquist sampling theorem
"""
c. What is the digital frequency of this signal?
"""
# ~20Hz? phase shifted too right
"""
d. Could the original analog signal be reconstructed from this digital 
signal?
"""
# No
xdata50hz = xdata1000hz[::20]
ydata50hz = ydata1000hz[::20]
#print(len(xdata50hz)) # Check we discard 4 of 5 samples correctly
matplotlib.pyplot.plot(xdata50hz, ydata50hz, marker='.')
matplotlib.pyplot.title('30.76Hz sin wave sampled @ 1000Hz, then decimated to 50Hz')
matplotlib.pyplot.xlabel('time (seconds)')
matplotlib.pyplot.show()

"""

33.33 Hz

"""
"""
b. Has aliasing occurred in this signal? Explain.
"""
# Yes, it does not fit the requirements of the nyquist sampling theorem
"""
c. What is the digital frequency of this signal?
"""
# ~2.5Hz? and it is phase shifted
"""
d. Could the original analog signal be reconstructed from this digital 
signal?
"""
# No

# 33.33333 Hz decimation is approximately every 30th sample
xdata33hz = xdata1000hz[::30]
ydata33hz = ydata1000hz[::30]
#print(len(xdata33hz)) # Check we discard 4 of 5 samples correctly
matplotlib.pyplot.plot(xdata33hz, ydata33hz, marker='.')
matplotlib.pyplot.title('30.76Hz sin wave sampled @ 1000Hz, then decimated to 33.33Hz')
matplotlib.pyplot.xlabel('time (seconds)')
matplotlib.pyplot.show()

"""

28.57 Hz

"""
"""
b. Has aliasing occurred in this signal? Explain.
"""
# Yes, it does not fit the requirements of the nyquist sampling theorem
"""
c. What is the digital frequency of this signal?
"""
# ~2.2Hz?
"""
d. Could the original analog signal be reconstructed from this digital 
signal?
"""
# No

# 28.57 Hz decimation is approximately every 35th sample
xdata28hz = xdata1000hz[::35]
ydata28hz = ydata1000hz[::35]
#print(len(xdata33hz)) # Check we discard 4 of 5 samples correctly
matplotlib.pyplot.plot(xdata28hz, ydata28hz, marker='.')
matplotlib.pyplot.title('30.76Hz sin wave sampled @ 1000Hz, then decimated to 28.57Hz')
matplotlib.pyplot.xlabel('time (seconds)')
matplotlib.pyplot.show()
