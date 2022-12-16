import random

FloatNumber = 9.956 
print("%.2f" % FloatNumber) # make round the float number and keep 2 digits after decimal

# random numbers from 0 till 3
print("%.2f" % random.uniform(0,3)) # make round the float number and keep 2 digits after decimal
print("%.5f" % random.uniform(0,3)) # make round the float number and keep 5 digits after decimal
print("%.10f" % random.uniform(0,3)) # make round the float number and keep 10 digits after decimal
print("%.20f" % random.uniform(0,3)) # make round the float number and keep 20 digits after decimal
print("%.30f" % random.uniform(0,3)) # make round the float number and keep 30 digits after decimal