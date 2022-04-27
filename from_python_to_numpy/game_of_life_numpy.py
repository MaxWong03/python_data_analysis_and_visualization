'''
Figure out 

# Flatten arrays
N_ = N.ravel() #create a 1 dimenional array N_
Z_ = Z.ravel() #create a 1 dimensional array Z_

Z_[R1] = 0
Z_[R2] = 0
Z_[R3] = Z_[R3]
Z_[R4] = 1


Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0

birth = (N==3)[1:-1,1:-1] & (Z[1:-1,1:-1]==0) #active cell state
survive = ((N==2) | (N==3))[1:-1,1:-1] & (Z[1:-1,1:-1]==1)#deactive cell states
Z[...] = 0
Z[1:-1,1:-1][birth | survive] = 1
'''
