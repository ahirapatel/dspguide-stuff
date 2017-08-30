import matplotlib.pyplot
from numpy import histogram
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
    one_thou = []
    for x in range(n):
        one_thou.append(the_algorithm())
    # Range of values is -.2 to 1.0, with a width of 0.01, so use 120 bins
    freq, buckets = histogram(one_thou, bins=120)

    #print(freq, buckets)
    # Uh, apparently I don't need histogram from numpy... oh well
    matplotlib.pyplot.hist(list(one_thou), bins=buckets)
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

"""
i. Explain the apparent contradiction between your answers in (g) and (h).   

 
2. Calculation of the mean and standard deviation.

a. Generate a signal containing 10,000 points from this algorithm. Calculate
the mean and standard deviation, using a method of your choice.       
b. Generate three signals as in (a), and add them together.  Calculate the 
mean and standard deviation of the resulting signal.
c. Repeat (b) adding 10 signals. 
d. Repeat (b) adding 30 signals.  
e. Make a graph of your data in (a)-(d), proving that when random signals
are added, their means add and their standard deviations add in quadrature.
In your graphs, the x-axis should be "number of points," and the y-axis
should be "mean" or "standard deviation."


3. The Central Limit Theorem.
  
a. Calculate and plot the histogram of the signal in 2(c).   
b. On this same graph, show a Gaussian curve with the mean and standard 
deviation determined in 2(c).  
c. Comment on the match between the two in terms of accuracy and precision.  
d. Would increasing the number of samples improve the accuracy or precision 
of the match?  
e. Would increasing the number of signals added improve the accuracy of the 
match? 

"""
