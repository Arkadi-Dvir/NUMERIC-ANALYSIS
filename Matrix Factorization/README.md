Matrix Factorization:

The basic algorithm for matrix factorization is a reprsentation of a “simpler” matrices.

So let's define L as lower triangular 

![image](https://user-images.githubusercontent.com/73054794/119589460-80b89500-bddb-11eb-9071-1a1998fef790.png)

Then the linear system Lx=b can easily be solved using forward substitution:

![image](https://user-images.githubusercontent.com/73054794/119589557-b65d7e00-bddb-11eb-8206-ddb9392cb34d.png)

Now let's define U the upper diagonal:

![image](https://user-images.githubusercontent.com/73054794/119589681-f9b7ec80-bddb-11eb-8072-783737a7308d.png)

Then the linear system Ux=b can be solved using backward substitution:

![image](https://user-images.githubusercontent.com/73054794/119589734-1bb16f00-bddc-11eb-886d-f6bdc5df04e9.png)

So thats what the forward substitution and the  backward substitution functions do.
