'''
Scipy is for scientific computing
'''

from scipy import stats
import numpy as np


# Calculating correlatiobn
array_1 = np.array([1,2,3,4,5,6])
array_2 = array_1
print(stats.pearsonr(array_1, array_2)) # gives back the correlation value and p value

# Generating samples from distributions

# Generate 10 values randmoly sampled from a normal distribution with mean 0 and standard deviation of 10
# loc = mean
# scale = standard deivation
# size = num o samples to return
x = stats.norm.rvs(loc=0, scale=10, size=10)

# Probability density function
p1 = stats.norm.pdf(x=-100, loc=0, scale=10) # Get probability of sampling a value of -100
p2 = stats.norm.pdf(x=0, loc=0, scale=10) # Get probability of sampling a value of 0

# Cumulative distribution function
p1 = stats.norm.cdf(x=0, loc=0, scale=10) # Get probability of sampling a value less than or equal to 0
print(p1)

# Calculating descriptive statistics
# Calculate descriptive statistics for 500 data points sampled from normal distribvution with mean 0 and standard deviation of 1
print(stats.describe(stats.norm.rvs(loc=0, scale=1, size=500)))