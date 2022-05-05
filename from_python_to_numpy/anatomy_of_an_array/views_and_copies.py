'''
Views and Copies
  - important concepts for opimization of numerical computation

Direct and indirect access
  - Copy is when contents are physically stored in another location (new / different array)
  - View is when a different view of the same memory content is provided (same array)

Indexing and Fancy Indexing
  - Indexing return a view (same array, different view of the same memory content)
  - Fancy Indexing return a copy (new / different array with contents stored in another location)
'''

import numpy as np
Z = np.zeros(9) 
Z_view = Z[:3] # Indexing, returns a view
Z_view[...] = 1 # Z_view modifies the base array Z

Z = np.zeros(9)
Z_copy = Z[[0,1,2]] # Fancy indexing, returns a copy
Z_copy[...] = 1 # Z_copy does not modify the base array Z