import matplotlib.pyplot
from numpy import histogram, std, var
from random import random 

"""
CHAPTER 2: STATISTICS, PROBABILITY AND NOISE

Use the following algorithm to find the value of each sample in a test
signal, where the function "rnd" returns a random number between 0 and 1:

x = rnd 
if x < 0.6 then x = x-0.2 

1. Calculation of the histogram.

a. Sketch the pdf of the process that generated this signal. 
--> Whiteboard it with dudes.
"""

"""
b. Generate and plot a signal containing 300 points from this algorithm. 
"""
def the_algorithm():
    x = random()
    return x-.2 if x < 0.6 else x

three_hundo = []
for x in range(300):
    three_hundo.append(the_algorithm())
#print(three_hundo, len(three_hundo))

matplotlib.pyplot.plot(three_hundo, linestyle='None',marker='.')
matplotlib.pyplot.show()

"""
c. Generate and plot the histogram of 1000 points acquired from this 
algorithm.  Use a bin width of 0.01. 
"""
def histo_n(n):
    # Numpy. Yes.
    data = []
    for x in range(n):
        data.append(the_algorithm())
    # Range of values is -.2 to 1.0, with a width of 0.01, so use 120 bins
    freq, buckets = histogram(data, bins=120)

    #print(freq, buckets)
    # Uh, apparently I don't need histogram from numpy... oh well
    matplotlib.pyplot.hist(data, bins=buckets)
    matplotlib.pyplot.show()

    return freq,buckets

f1000, b1000 = histo_n(1000)


"""
d. Repeat (b) using 10,000 samples.
"""
f10000, b10000 = histo_n(10000)
"""
e. Repeat (b) using 100,000 samples. 
"""
f100000, b100000 = histo_n(100000)

"""
f. Estimate the peak-to-peak noise on the histograms in (c) to (e). Give 
your answer as the actual number, not a percentage.
"""
#uhhhh wat
print("1000 sample peak-to-peak", max(f1000) - min(f1000))
print("10000 sample peak-to-peak", max(f10000) - min(f10000))
print("100000 sample peak-to-peak", max(f100000) - min(f100000))

"""
g. Which of these three histograms is the best estimate of the pdf?  The 
worst estimate?
"""
# The best would be with more data, worst is with least data.

"""
h. Which histogram has the lowest peak-to-peak noise?  The highest peak-to-
peak noise?  
"""
print("lowest peak-to-peak is 1000 samples, highest peak-to-peak is 100,000 samples")

"""
i. Explain the apparent contradiction between your answers in (g) and (h).   
"""
print("more samples in one, you gotta normalize them")

"""
2. Calculation of the mean and standard deviation.

a. Generate a signal containing 10,000 points from this algorithm. Calculate
the mean and standard deviation, using a method of your choice.       
"""
tenK = []
for x in range(10000):
    tenK.append(the_algorithm())
print("Name,\tSTD,\t\tVAR,\t\tMEAN")
print("1", std(tenK), var(tenK), sum(tenK)/len(tenK))

"""
b. Generate three signals as in (a), and add them together.  Calculate the 
mean and standard deviation of the resulting signal.
"""
tenK2 = []
for x in range(10000):
    tenK2.append(the_algorithm())
tenK3 = []
for x in range(10000):
    tenK3.append(the_algorithm())
print("2", std(tenK2), var(tenK2), sum(tenK2)/len(tenK2))
print("3", std(tenK3), var(tenK3), sum(tenK3)/len(tenK3))
sumK = []
for a,b,c in zip(tenK, tenK2, tenK3):
    sumK.append(a+b+c)
print("sumsX3", std(sumK), var(sumK), sum(sumK)/len(sumK))

"""
c. Repeat (b) adding 10 signals. 
"""

ten_siggies = []
for x in range(10000):
    ten_samples = []
    for i in range(10):
        ten_samples.append(the_algorithm())
    ten_siggies.append(ten_samples)

sum10 = []
for vals in ten_siggies:
    sum10.append(sum(vals)) # Sum up values at t=<blah> then stick em in sum10 at t=<blah>
print("sumsX10", std(sum10), var(sum10), sum(sum10)/len(sum10))

"""
d. Repeat (b) adding 30 signals.  
"""
thirty_siggies = []
for x in range(10000):
    thirty_samples = []
    for i in range(30):
        thirty_samples.append(the_algorithm())
    thirty_siggies.append(thirty_samples)

sum30 = []
for vals in thirty_siggies:
    sum30.append(sum(vals)) # Sum up values at t=<blah> then stick em in sumK at t=<blah>
print("sumsX30", std(sum30), var(sum30), sum(sum30)/len(sum30))

"""
e. Make a graph of your data in (a)-(d), proving that when random signals
are added, their means add and their standard deviations add in quadrature.
In your graphs, the x-axis should be "number of points," and the y-axis
should be "mean" or "standard deviation."
"""
# No. Instead just look at print statements, doing the math in your head is easy enough.

"""
3. The Central Limit Theorem.

a. Calculate and plot the histogram of the signal in 2(c).   
""" 
matplotlib.pyplot.hist(sum10, bins=25)
matplotlib.pyplot.show()

"""
b. On this same graph, show a Gaussian curve with the mean and standard 
deviation determined in 2(c).  
"""
# Eh, you can kind of just look at it to see the shape.

"""
c. Comment on the match between the two in terms of accuracy and precision.  
"""
# Could be more accurate as it is not very rounded like a gaussian, but more signals
# added to it would make it more gaussian.

"""
d. Would increasing the number of samples improve the accuracy or precision 
of the match?  
"""
# More precise, standard deviation will be lower.
# The accuracy would also go up for non-random signals, as we'd be closer to the
# "true value"

"""
e. Would increasing the number of signals added improve the accuracy of the 
match? 
"""
# Yes, as more signals are added, it would become more and more bell shaped in
# the distribution
