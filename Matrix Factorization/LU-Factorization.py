import numpy as np
def lu_factorizing(A):
  n = len(A[0])
  U = np.zeros((n, n))
  U = U + A
  L = np.identity(n)
  for i in range(n-1):
      for j in range (i+1,n):
        L[j][i] = U[j][i]/U[i][i]
      for j in range (i+1,n):
        for k in range (i,n):
          U[j][k] = U[j][k] - L[j][i]*U[i][k]
      for j in range(i+1,n):
          U[j][i] = L[j][i]
  return U
