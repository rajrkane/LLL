# LLL

An implementation of the LLL Algorithm, first described by Lenstra, Lenstra, and Lovasz in 1982. 

<h2>Requirements</h2>
A recent version of Python and NumPy.

<h2>To use</h2>
Run `python LLL.py basis` where the n-dimensional basis should be input as the following string:  `'[[basis[0][0],basis[0][1],...,basis[0][n-1]], [basis[1][0],...,basis[1][n-1]],...,[basis[n-1][0],...,basis[n-1][n-1]]'`. This only handles full rank lattices.
