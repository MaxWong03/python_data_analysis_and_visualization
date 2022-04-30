'''
Create a function which takes that numpy 1-D array as input and returns the following (in the same order as listed):

Max - Maximum value in the array
Std - Measure of variation between the elements of an array
Sum - Value obtained as a result of adding all the elements of an array
Dot product - Inner product of the vectors
Try to implement the function below. Feel free to view the solution, after giving it a few shots. Good Luck!
'''

import numpy as np

def perform_calculations(array) 
  np_array = np.array(array) #convert array to numpy array
  max = np_array.max()
  std = np.std(np_array)
  sum = np.sum(np_array)
  dot_product = np.dot(np_array, np_array)
  return max, std, sum, dot_product


'''
Scipy#
Create a function that takes in two numpy 1-D arrays and returns the correlation and p-value as a tuple.

Try to implement the function below. Feel free to view the solution, after giving it a few shots. Good Luck!
'''

from scipy import stats

def calculate_correlation(array_1, array_2)
  np_array_1 = np.array(array_1)
  np_array_2 = np.array(array_2)
  return stats.pearsonr(np_array_1, np_array_2)

'''
Using the functions
'''

print(perform_calculations(np.random.rand(5)))

print(calculate_correlation(np.random.rand(5),np.random.rand(5)))
