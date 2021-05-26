import numpy as np
from numpy import linalg as LA
def gauss_seide(A,b,x0,num_iter):
  n = len(A[0])
  for k in range(num_iter):
    y = [0] * n
    for i in range(n):
      sumvec = 0
      for j in range(n):
        if j != i:
          sumvec = sumvec + (A[i][j] * x0[j])
      x0[i] = (1/A[i][i])*(b[i] - sumvec)
  vec = np.dot(A,x0)
  return (LA.norm(np.subtract(vec, b)))
