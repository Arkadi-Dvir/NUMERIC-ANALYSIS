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

No we know that matrix A has a unique decomposition A=LU with L unit lower triangular and U non singular upper triangular if and only if all its principal sub matrices are non singular.

The Non singular function checks that. So the LU factarization algorithm is:

![image](https://user-images.githubusercontent.com/73054794/119590753-0e957f80-bdde-11eb-89f3-2fc42876f33d.png)
