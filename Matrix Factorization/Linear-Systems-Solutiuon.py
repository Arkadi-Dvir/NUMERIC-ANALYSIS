import numpy as np
def linear_systems_solutiuon(A,b):
  M = lu_factorizing(A)
  n = len(M[0])
  L = np.identity(n)
  for i in range(1,n):
    for j in range(i):
        L[i][j] = M[i][j]
  y = forward_sub(L, b)
  for i in range(0,n):
    for j in range(i,n):
      U[i][j] = M[i][j]
  x = backward_sub(U, y)
  return(x)
