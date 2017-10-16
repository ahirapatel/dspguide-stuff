#!/usr/bin/env python

"""
CHAPTER 4: DSP SOFTWARE

"""


"""
This exercise looks at the problem of adding numbers that are very different
is size.   Write a computer program(s) to complete the following.

1. Generate a 256 samples long sine wave with an amplitude of one, and a
frequency such that it completes 3 full periods in the 256 samples. 
Represent each of the samples using single precision floating point.  We
will call this signal, x[ ]

"""
def dothething(k):
    import matplotlib.pyplot
    def sin_wave():
        """
        return a pair of lists with sample time in one list and output values in other
        """
        from math import sin
        from math import pi

        num_samples = 256
        sample_steps = 1 / num_samples
        xdata, ydata = [], []
        for i in range(num_samples):
            x = i * sample_steps * 2*pi # Convert to radians with 2pi
            y = sin(3*x)
            xdata.append(i*sample_steps) # We want the time in seconds, not the radian values
            ydata.append(y)

        return xdata, ydata

    t,x = sin_wave()
    #matplotlib.pyplot.plot(t, x, marker='.')
    #matplotlib.pyplot.title('256 samples of 3 periods')
    #matplotlib.pyplot.xlabel('time')
    #matplotlib.pyplot.ylabel("Signal Amplitude")
    #matplotlib.pyplot.show()


    """

    2. Add a constant, k = 300,000 to each of the samples in the signal.

    3. Subtract the same constant, k, from each of the samples.  Call this
    reconstructed signal, y[ ]

    4. Find the difference (i.e., the reconstruction error) between x[ ] and
    y[].   Call this signal, d[ ].

    5. Plot the reconstructed signal, y[ ], and the difference signal, d[ ].

    """
    y = [val+k for val in x]
    y = [val-k for val in y]
    d = [old - new for old,new in zip(x,y)]

    fig,ax1 = matplotlib.pyplot.subplots()
    ax2 = ax1.twinx()

    ax2.set_xlabel('time')
    ax2.set_ylabel("Signal Amplitude")
    ax1.set_ylabel("Error", color='r')
    matplotlib.pyplot.title('Error of adding then subtracting {}'.format(k))

    ax2.plot(t, y, marker='.')
    ax1.plot(t, d, 'r', marker='.')
    matplotlib.pyplot.show()


"""
6. Repeat steps 1-5 for k = 3,000,000.

7. Repeat steps 1-5 for k = 30,000,000.
"""
dothething(300000)
dothething(3000000)
dothething(30000000)
# Python does not have single precision so let's be excessive to get the 
# point of this exercise
dothething(300000000000000)
dothething(3000000000000000)
dothething(30000000000000000)

"""

8.  Answer the following questions:

a. "When floating point numbers of very different size are added, the
quantization noise on the [fill in the blank] number destroys the
information contained in the [fill in the blank] number. "

# large number
# small number

"""

"""

b. The results of step 7 show that the information in the reconstructed
signal is completely destroyed with k is equal to 30 million, or greater. 
If this exercise were repeated with the sine wave of amplitude 0.001, how
large of value of k would be needed to destroy the information in the
reconstructed signal?
# No idea cuz I'm not using single precision floats. Oh well

c. If this exercise were repeated using double precision, how large of value
for k would be needed to destroy the information in the reconstructed
signal?
# See 6 and 7
"""
