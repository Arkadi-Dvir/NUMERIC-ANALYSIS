def diagonally_dominant(A):
  n = len(A[0])
  for i in range(n):
    for j in range(n):
      if(abs(A[i][i]) < abs(A[i][j])):
        return 0
  return 1
