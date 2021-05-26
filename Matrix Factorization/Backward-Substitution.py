def backward_sub(U,b):
  n = len(U[0])
  x = [0] * n
  for i in range(n-1,-1,-1):
    sum_num = 0
    for k in range(i+1,n): 
      sum_num = sum_num + U[i][k]*x[k]
    x[i] = (b[i] - sum_num)/U[i][i]
  return x
