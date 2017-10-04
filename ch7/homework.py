#!/usr/bin/env python3

"""
CHAPTER 7: PROPERTIES OF CONVOLUTION
"""
 
"""
1. Classify the following signals as either casual or noncausal.

a. x[n] = delta[n]
b. x[n] = delta[n-2]
c. x[n] = delta[n-1] + delta[n+1]
d. x[n] = delta[n] -  5 delta[n-5]
e. x[n] = delta[n] + delta[n+5]
f. x[n] = delta[n-1] - delta[n-4] + delta[n-7]
g. x[n] = exp(-n)
h. x[n] = exp(-abs(n))  (where "abs" is the absolute value function)
i. x[n] = abs(n)
j. x[n] = n + abs(n)
"""
# a. x[n] = delta[n]
# causal
# b. x[n] = delta[n-2]
# causal
# c. x[n] = delta[n-1] + delta[n+1]
# non-causal
# d. x[n] = delta[n] -  5 delta[n-5]
# causal
# e. x[n] = delta[n] + delta[n+5]
# non-causal
# f. x[n] = delta[n-1] - delta[n-4] + delta[n-7]
# causal
# g. x[n] = exp(-n)
# non-causal
# h. x[n] = exp(-abs(n))  (where "abs" is the absolute value function)
# non-causal
# i. x[n] = abs(n)
# non-causal
# j. x[n] = n + abs(n)
# causal

"""
2. Classify the signals in the last problem as either zero phase, linear
phase, or nonlinear phase.
"""
# a. x[n] = delta[n]
# zero phase
# b. x[n] = delta[n-2]
# linear phase
# c. x[n] = delta[n-1] + delta[n+1]
# zero phase
# d. x[n] = delta[n] -  5 delta[n-5]
# non-linear phase
# e. x[n] = delta[n] + delta[n+5]
# linear phase
# f. x[n] = delta[n-1] - delta[n-4] + delta[n-7]
# linear phase
# g. x[n] = exp(-n)
# non-linear phase
# h. x[n] = exp(-abs(n))  (where "abs" is the absolute value function)
# zero-phase
# i. x[n] = abs(n)
# zero-phase
# j. x[n] = n + abs(n)
# non-linear phase

"""
3. The impulse responses of three linear systems are given below.  Calculate
the impulse response of the indicated combination
system A:  3, 2, 1, 0
system B:  0, 1,-1, 0
system C:  1, 1, 1, 1
a. The parallel combination of system A and system B.
b. The parallel combination of system A, system B, and system C. 
c. The cascade of System A and system B. 
d. The cascade of System B and system A.
e. The cascade of System A and system B, in parallel with system C.
"""
from numpy import convolve

print("Number 3")
systemA = [3, 2, 1, 0]
systemB = [0, 1,-1, 0]
systemC = [1, 1, 1, 1]
print("system A", systemA)
print("system B", systemB)
print("system C", systemC)
# parallel => add em, cascade => convolve em
print("a. The parallel combination of system A and system B.\n\t",
        [a+b for a,b in zip(systemA,systemB)])
print("b. The parallel combination of system A, system B, and system C.\n\t",
        [a+b+c for a,b,c in zip(systemA,systemB,systemC)])
print("c. The cascade of System A and system B.\n\t",
        convolve(systemA,systemB))
print("d. The cascade of System B and system A.\n\t",
        convolve(systemB,systemA))
print("e. The cascade of System A and system B, in parallel with system C.")
temp = convolve(systemA,systemB) # Convolving will make len(temp) bigger than len(C)
for index,val in enumerate(systemC):
    temp[index] += val
print("\t",temp)


"""
4. System A is an "all pass" system, meaning that its output is identical to
its input.  System B is a low-pass filter that passes all frequencies below
the cutoff frequency without change, and blocks all frequencies above.  Call
the impulse response of system B, b[n]. 

a. What is the impulse response of system A?
b. How would the impulse response of system B need to be changed to make the
system have an inverted output (i.e., the same output, just changed in sign)?
c. If the two systems are arranged in parallel with added outputs, what is
the impulse response of the combination?
d. If the two systems are arranged in parallel, with the output of system B
subtracted from the output of system A, what is the impulse response of the
combination?
e. What kind of filter is the system in (d)?
f. Describe an algorithm for changing a low-pass filter kernel into a high-
pass filter kernel. 
g. Describe an algorithm for changing a high-pass filter kernel into a low-
pass filter kernel.  Is this exactly the same procedure as in (f)?
h. In this problem, system B has the ideal characteristic of passing certain
frequencies "without change."  How would the algorithm you described in (f)
be affected if the low-pass filter delayed (i.e., shifted) the output signal
by a small amount, relative to the input signal?    
"""
#a. What is the impulse response of system A?
#   delta[n]

# b. How would the impulse response of system B need to be changed to make the
# system have an inverted output (i.e., the same output, just changed in sign)?
#    -b[n]

# c. If the two systems are arranged in parallel with added outputs, what is
# the impulse response of the combination?
#    a[n] + b[n]

# d. If the two systems are arranged in parallel, with the output of system B
# subtracted from the output of system A, what is the impulse response of the
# combination?
# a[n] - b[n]

# e. What kind of filter is the system in (d)?
#    High pass filter is (delta - lpf)

# f. Describe an algorithm for changing a low-pass filter kernel into a high-
# pass filter kernel. 
#    delta[n] - lpfkernel[n]

# g. Describe an algorithm for changing a high-pass filter kernel into a low-
# pass filter kernel.  Is this exactly the same procedure as in (f)?
#    delta[n] - hpfkernel[n], yus

# h. In this problem, system B has the ideal characteristic of passing certain
# frequencies "without change."  How would the algorithm you described in (f)
# be affected if the low-pass filter delayed (i.e., shifted) the output signal
# by a small amount, relative to the input signal?    
#    It would be fine if the delta[n] also delayed the signal the same amount
#    else it wouldn't, and would be something like delta[n] - lpfkernel[n-blah]

"""
5. From calculus, you know that the derivative and integral are inverse
operations; one undoes the effect of the other.  Prove that the first
difference and the running sum are also inverse operations.  That is, show
that the cascade of these two systems is identical to the delta function. 
"""
print()
print("Number 5")
def first_difference(samples):
    from numpy import convolve
    first_diff_impulse = [1, -1, 0, 0, 0, 0]
    return convolve(samples, first_diff_impulse)

def running_sum(samples):
    from numpy import convolve
    # Technically this impulse needs to run forrrrrrrever
    running_diff_impulse = [1, 1, 1, 1, 1, 1]
    return convolve(samples, running_diff_impulse)

first_diff_impulse = [1, -1, 0, 0, 0, 0]
running_diff_impulse = [1, 1, 1, 1, 1, 1]
print("firstdiff✴runningsum == {}✴{} == {}".format(first_diff_impulse, running_diff_impulse,
          convolve(first_diff_impulse, running_diff_impulse)))
a = [-1,2,3,1,3,2,5,1,5]
print("Example of needing infinte running sum:\n\t" +
        "orig {}\n\tfirst_diff {}\n\trunning sum of first diff {}\n"
        .format(a, first_difference(a), running_sum(first_difference(a))))
print("They are inverse operations... if the running sum impulse goes forever")

"""
6. Echoes are added to audio signals to make the listener "feel" that they
are in a particular size of room.  Assume that an audio signal is sampled at
44 kHz, and that sound propagates at 332 meters/second. In a "small" room, a
person stands about 3 meters from the walls; in a "large" room, the distance
increases to about 10 meters.

a. In a small room, how long is the delay between a person making a sound
and its echo from the walls. 
b. How many samples does this correspond to in the digital signal?
c. What is the impulse response of a digital system simulating this echo, if
the amplitude of the echo is 20%?
d. Repeat (a) to (c) for the large room.
e. In a real listening environment, each echo will also generate another
echo.  That is, each original sound will be heard over and over with
diminishing amplitude. How would the impulse response in (c) be modified to
account for these echoes of echoes?
"""
# a. In a small room, how long is the delay between a person making a sound
# and its echo from the walls. 
#    3 meters to wall + 3 meters back to person = 6 meters
#    6 meters * (1 second / 332 meters) = 0.018072289156626505 seconds

# b. How many samples does this correspond to in the digital signal?
#    44 kHZ == 44000 Hz == 44000 samples/second
#    44000 samples / second * 0.018072289156626505 seconds
#    795.1807228915662 samples => 795 (probably miss that data of .1807228915662 samples)

# c. What is the impulse response of a digital system simulating this echo, if
# the amplitude of the echo is 20%?
#    .2 * delta[n-795] ?

# d. Repeat (a) to (c) for the large room.
#    a. 10 + 10 = 20 meters, 20 * (1/332) = 0.060240963855421686 seconds
#    b. 44000 * 0.060240963855421686 = 2650.602409638554 => 2650
#    c. .2 * delta[n-2650]

# e. In a real listening environment, each echo will also generate another
# echo.  That is, each original sound will be heard over and over with
# diminishing amplitude. How would the impulse response in (c) be modified to
# account for these echoes of echoes?
# Have some impulses in parallel with each previous output of the echo generator.
# .2 * delta[n-time] would feed into another .2 * delta[n-time], etc.
# Could the echo generator feed into itself? Eg (original signal + echo generator out)
# feeding into the echo generator
