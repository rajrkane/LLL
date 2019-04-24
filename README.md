# LLL

An implementation of the LLL Algorithm, first described by Lenstra, Lenstra, and Lovasz in 1982. 

<h2>Requirements</h2>
A recent version of Python and NumPy.

<h2>To use</h2>
Run 
```
python LLL.py basis
```
where the n-dimensional basis, given by each i-th basis vector formatted as 
```
[basis[i][0],basis[i][1],...,basis[i][i-1]
```
, should be input as the following string: 
```
'[basis[0],basis[1],...,basis[n-1]]'
```
.
