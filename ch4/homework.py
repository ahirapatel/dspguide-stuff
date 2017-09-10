#!/usr/bin/env python

"""
CHAPTER 4: DSP SOFTWARE

1. The following subroutine is used to calculate the function: y = exp(x),
using an efficient implementation of Eq. 4-3:

y = 1
term = 1
for counter = 1 TO 150
 term = term * x / counter
 y = y + term
next counter

a. What are the values of "y" and "term" at the end of the first, second,
and third loops? 
b. At the end of all 150 loops, how many terms have been included in the
calculation?
"""
def expthing(k, x):
    y = 1
    term = 1
    for counter in range(1,k+1):
        term = term * x / counter
        y = y + term
        print("counter {}, term: {}, y: {}".format(counter, term, y))
"""
part a
"""
#actually what does he want?

"""
part b
 uh.. 150?
"""



"""
2.  Calculate the numeric value of the first 14 terms of the series for
exp(x) (Eq. 4-3), where x = 1.3. From this data, how many terms must be used
to achieve an accuracy of one part in one-million?  
"""
expthing(14, 1.3)
#11 terms?

"""
3. To illustrate the size of quantization levels, imagine representing the
heights of two buildings as digital numbers.  Building A is exactly 100
meters in height, while Building B is 100.0001 meters.  That is, Building B
is about the thickness of a sheet of paper (0.1 mm)  higher than building A. 
Indicate whether or not each of the following types of digitized numbers
could show that the two buildings are different in height. 

a. Integer (8 bit, unsigned)
# Nope
b. Integer (16 bit, 2's complement)
# Nope
c. Single precision floating point
# Yep, it becomes 100.00099 though
d. Double precision floating point
# Yep
"""


"""
4.  Repeat problem 3 for Building B being one ten-millionth of a meter
higher than Building A (about the diameter of a single atom).  If double
precision were used, how much smaller than the diameter of an atom are the
quantization levels?
"""
a = 100.0
b = 100.0 + 1/10000000 # 100.0 + 10**-7
# Error of doubles are about one part in forty quadrillion (10**-15) from book
print("This much smaller", 10**-8)

"""
5. Find the decimal number that corresponds to the following floating point
bit patterns.

a. 10111000101010100000000000000000
   1 01110001               01010100000000000000000
   - 2^((1+16+32+64)-127) x 1.(1/4+1/16+1/64)
   - 2^(113-127)          x 1.328125
   - 2^(-14) x 1.328125
   -1.328125 x 2^-14
   -8.106231689453125e-05

b. 10000000000000000000000000000000 
   1 00000000 00000000000000000000000 
   -0

c. 01111001111110010000000000000000
   0 11110011    11110010000000000000000
   2^(243-127) x 1.9453125
   2^(116) x 1.9453125
   1.6161023972189651e+35

d. 01111111100000000000000000000000 
   0 11111111 00000000000000000000000 
   +Infinity
"""

"""
6. Convert the following decimal numbers into their IEEE floating point bit
patterns: 

a. 1
  0 01111111 00000000000000000000000 
b. 2
  0 10000000 00000000000000000000000 
c. 4
  0 10000001 00000000000000000000000 
d. -5
  1 10000001 01000000000000000000000
             this is 1.25 so 4 * 1.25 = 5
e. 18
  0 10000011 00100000000000000000000
"""


"""
7. Imagine you are trying to represent the number: 4.0000003 in single
precision.  

a. What bit pattern corresponds to the number 4?
  0 10000001 00000000000000000000000 

b. What bit pattern corresponds to the next largest number that can be
represented?  
  0 10000001 00000000000000000000001

c. What decimal number corresponds to the bit pattern in (b)?   
  4.000000476837158203125

d. Which of the above two binary patterns should be used to represent the
number: 4.0000003?  Why? 
  4.000000476837158203125
  The latter, it has less error that way from the actual value we want to store

e. What is the error introduced when this number is stored in single
precision?  Express you answer both as an absolute number, and as a fraction
of the number being represented.  
    Error = ~1.7683715825000945e-07
    Ratio = ~4.4209286246805893e-08

"""

"""
8. In an FIR digital filter, each sample in the output signal is found by
multiplying M samples from the input signal by M predetermined coefficients,
and adding the products.  The characteristics of these filters (high-pass,
low-pass, etc.) are determined by the coefficients used. For this problem,
assume M = 5000, and that single precision floating point math is used.  

a. How many math operations (the number of multiplications plus the number
of additions) need to be conducted to calculate each point in the output
signal?  

M samples * M coefficients + M additions
25005000

b. If the output signal has an average amplitude of about one-hundred, what
is the expected error on an individual output sample.  Assume that the
round-off  errors combine by addition.  Give your answer both as an absolute
number, and as a fraction of the number being represented.  

# one part in forty million (4e7), multiplied by the number of operations it has been through
4e7 * 25005000
>>> 1/4e7 * 25005000
0.6251249999999999

c. Repeat (b) for the case that the round-off errors combine randomly.
hmmmmmmm approximately nothing?
"""
