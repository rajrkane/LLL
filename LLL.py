"""LLL.py: Implements the LLL Algorithm originally developed by Lenstra, Lenstra, Lovasz in 1982. Python 2.7."""

import sys
import json
import numpy as np
from numpy import linalg as la

__author__ = "Raj Kane"
__version__ = "Spring 2019"

basis = np.array(json.loads(sys.argv[1])).astype(float) # Initialize the basis as the user input.
orthobasis = basis.copy()   # Initialize the Gram-Schmidt basis.

k = 1 # Initialize the working index.
DELTA = 0.75   

def projection_scale(u, v):
    '''Computes <u,v>/<u,u>, which is the scale used in projection.'''
    return np.dot(u, v) / np.dot(u, u)

def proj(u, v):
    '''Computes the projection of vector v onto vector u. Assumes u is not zero.'''
    return np.dot(projection_scale(u, v), u)

def gram_schmidt(): 
    '''Computes Gram Schmidt orthoganalization (without normalization) of a basis.'''
    orthobasis[0] = basis[0]
    for i in range(1, basis.shape[1]):  # Loop through dimension of basis.
        orthobasis[i] = basis[i]
        for j in range(0, i):
            orthobasis[i] -= proj(orthobasis[j], basis[i])
    return orthobasis

def reduction():
    '''Performs length reduction on a basis.'''
    total_reduction = 0 # Track the total amount by which the working vector is reduced.
    for j in range(k-1, -1, -1):   # j loop. Loop down from k-1 to 0.
        m = round(projection_scale(orthobasis[j], basis[k]))
        total_reduction += np.dot(m, basis[j])[0]
        basis[k] -= np.dot(m, basis[j]) # Reduce the working vector by multiples of preceding vectors.
    if total_reduction > 0:
        gram_schmidt() # Recompute Gram-Scmidt if the working vector has been reduced. 

def lovasz():
    global k
    '''Checks the Lovasz condition for a basis. Either swaps adjacent basis vectors and recomputes Gram-Scmidt or increments the working index.'''
    c = DELTA - projection_scale(orthobasis[k-1], basis[k])**2
    if la.norm(orthobasis[k])**2 >= np.dot(c, la.norm(orthobasis[k-1]**2)): # Check the Lovasz condition.
        k += 1  # Increment k if the condition is met.
    else: 
        basis[[k, k-1]] = basis[[k-1, k]] # If the condition is not met, swap the working vector and the immediately preceding basis vector.
        gram_schmidt() # Recompute Gram-Schmidt if swap
        k = max([k-1, 1])

def main():
    while True:
        x = raw_input("Would you like to see the steps? Press [Y/N] and Enter. ")
        if x in ['Y','N', 'y', 'n']: break
        else: raw_input("Would you like to see the steps? Press [Y/N] and Enter. ")
    if x in ['Y', 'y']:
        gram_schmidt()
        steps = 0
        while k <= basis.shape[1] - 1:
            reduction()
            steps += 1
            print 'Step ', steps,'. After the reduction step, the basis is\n', basis
            raw_input("")
            lovasz()
            steps +=1
            print 'Step ', steps,'. After checking the Lovasz condition, the basis is\n', basis
            raw_input("")
        print 'LLL Reduced Basis:\n', basis
    else:
        gram_schmidt(basis)
        while k<= basis.shape[1] - 1:
            reduction()
            lovasz()
        print 'LLL Reduced Basis:\n', basis

if __name__ == "__main__":
    main()