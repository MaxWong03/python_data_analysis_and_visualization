import numpy as np
Z = np.array([[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]])
N = np.zeros(Z.shape, dtype=int)
N[1:-1, 1:-1] += (Z[:-2, :-2] + Z[:-2, 1:-1] + Z[:-2, 2:] +
                  Z[1:-1, :-2] + Z[1:-1, 2:] +
                  Z[2:, :-2] + Z[2:, 1:-1] + Z[2:, 2:])

# Flatten arrays
N_ = N.ravel() #create a 1 dimenional array N_
Z_ = Z.ravel() #create a 1 dimensional array Z_
print(N_)
print(Z_)
# Apply rules
R1 = np.argwhere( (Z_==1) & (N_ < 2) )
R2 = np.argwhere( (Z_==1) & (N_ > 3) )
R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
R4 = np.argwhere( (Z_==0) & (N_==3) )
print(R1)

# Set new values
Z_[R1] = 0
Z_[R2] = 0
Z_[R3] = Z_[R3]
Z_[R4] = 1

# print(Z_)

# Make sure borders stay null
# First row , last row, first column, last column
Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0
# print(Z)
birth = (N==3)[1:-1,1:-1] & (Z[1:-1,1:-1]==0) #active cell state
survive = ((N==2) | (N==3))[1:-1,1:-1] & (Z[1:-1,1:-1]==1)#deactive cell states
Z[...] = 0
Z[1:-1,1:-1][birth | survive] = 1