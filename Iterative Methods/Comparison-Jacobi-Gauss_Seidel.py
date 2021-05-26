import matplotlib.pyplot as plt
A = [[-2,1,0,0,0],[1,-2,1,0,0],[0,1,-2,1,0],[0,0,1,-2,1],[0,0,0,1,-2]]
b= [1,0,0,0,0]
x0=[0,0,0,0,0]
x = np.arange(0, 100, 5) # You can change the scale and the range of iterations
y = [0]*len(x)
for i in range(len(x)):
  y[i] = jacobi(A,b,x0,x[i]) # x[i] is the number of iterations
plt.title('Jacobi:')
plt.plot(x,y)
plt.show()
for i in range(len(x)):
  y[i] = gauss_seide(A,b,x0,x[i])
plt.title('Gauss-Seide:')
plt.plot(x,y)
plt.show()
