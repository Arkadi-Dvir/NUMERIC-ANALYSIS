import numpy as np
from time import perf_counter
def non_singular_matrix(A):
  if(np.linalg.det(A)):
    return True
  else: return False
