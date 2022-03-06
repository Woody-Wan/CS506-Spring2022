import numpy as np
dis_array = np.array(dis) # convert dis to array
dis_array.ravel() # convert an array of all demensions to one dimension
np.unravel_index(i , dis_array.shape)
"""
np.unravel_index(i, dis_array.shape) is aming
to return the original index of these elements in the originlal matrix (dis_array.shape)"""
np.mat(A) # convert A to matrix
np.zeros([2,3]) # form a 2*3 zero matrix
np.dot(A,B) # dot multiple of A and B; 
np.multiply(A,B) # elementwise multiply A by B
A*B
np.matmul(A,B)
