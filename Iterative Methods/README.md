The iterative methods give us approximation of the requsted result for linear systems.

Ill show two methods here Jacobi and Gauss-Seidel.

Like many iterative methods we hope to have a smaller residual every iteration, but nothing insure us.

So how can we know that the iterative algorithm works?
In our case it's simple If A is diagonally dominant matrix then Jacobi’s and Gauss-Seidel methods converges, I made a simple function that checks that.

Jacobi iterative method, based on a splitting of the matrix A into its diagonal part and its off diagonal part:

![image](https://user-images.githubusercontent.com/73054794/119592721-b06a9b80-bde1-11eb-8c8a-e30f020c104d.png)

Gauss-Seidel iterative method, based on a splitting of the matrix A into its lower triangular part and the remainder:

![image](https://user-images.githubusercontent.com/73054794/119592820-ddb74980-bde1-11eb-9249-ff0bdc53499f.png)

Thats the algorithms that i was based on. Furthermore i made a comparison function to show the difference in the speed of convergence between this two.

This is only partial, for more information i suggest you to read more about iterative methods.

