def forward_sub(L,b):
  x = [0] * len(L[0]) # Zero vector
  for i in range(len(L[0])):
    sum_num = 0
    for k in range(i): 
      sum_num = sum_num + L[i][k]*x[k]
    x[i] = (b[i] - sum_num)/L[i][i]
  return x
