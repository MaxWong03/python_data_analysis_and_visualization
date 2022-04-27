'''
Numpy
  - provide array data structures similar to Python lists
  - faster, take up less space, and have more functionality
  - fixed size and type that you define at creation
'''

# One dimensional array

import numpy as np
np_array = np.array([5, 10, 15, 20, 25, 30, 30])
print(np.unique(np_array))
print(np.std(np_array))
print(np_array.max())
print(np_array ** 2)
print(np_array + np_array)
print(np.sum(np_array ** 2))
print(np_array.shape)

# Two dimensional array
np_2d_array = np.array([[1,2,3], [4,5,6]])
np_2d_array_T = np_2d_array.T #calculate transpose (swap columns and rows)
print(np_2d_array_T)
print(np_2d_array.shape)
print(np_2d_array[1,1])
print(np_2d_array[0,2])

# Important functionalities
dot_product = np.dot(np_array, np_array)
print(dot_product)

# Generating random values
np.random.rand() # generate single random number in range [0, 1)

np.random.rand(3,2) # generate matrix of random numbers in rage [0, 1) with shape (3,2)

np.random.randint(5, 15, 2) # generate 2 values between 5 and 15

np.random,randint(5, 15, (3,2)) # generate a matrix of shape (3, 2) with values between 5 and 15

# Sampling data
array = np.array([1,2,3,4,5])
np.random.choice(array, 10, replace=True) # w/ replacement means the same value can be sample more than once
np.random.choice(array, 3, replace=False) # w/o replacement means the same value can't be sample more than once

# Randomly shuffling values
np.random.seed(42) # seed means the random selection will be same everytime
x=[1,2,3,4,5]
np.random.shuffle(x)
