import sys
import json
import numpy as np
from numpy import linalg as la

# Dummy data for testing
basis = np.array([[201, 37], 
                [1648, 297]]).astype(float)

# basis = np.array(json.loads(sys.argv[1])).astype(float) # Initialize the basis as the user input.
orthobasis = basis.copy()   # Initialize the Gram-Scmidt basis.

k = 1 # Initialize the working index.
DELTA = 0.75   

# Need functions for determining whether data is fed correctly. (Dimensions, linear independence, syntax) 


def projection_scale(u, v):
    '''Computes <u,v>/<u,u>, which is the scale used in projection.'''
    return np.dot(u, v) / np.dot(u, u)

def proj(u, v):
    '''Computes the projection of vector v onto vector u. Assumes u is not zero.'''
    return np.dot(projection_scale(u, v), u)

def gram_schmidt(basis): 
    '''Computes Gram Schmidt orthoganalization (without normalization) of a basis.'''
    orthobasis[0] = basis[0]
    for i in range(1, basis.shape[1]):  # Loop through dimension of basis.
        orthobasis[i] = basis[i]    # Initialize the current vector being orthogonalized to the corresponding basis vector.
        for j in range(0, i):
            orthobasis[i] -= proj(orthobasis[j], basis[i])
    return orthobasis

def reduction(basis, orthobasis):
    '''Performs length reduction on a basis.'''
    total_reduction = 0 # Track the total amount by which the working vector is reduced.
    for j in range(k-1, -1, -1):   # j loop. Loop down from k-1 to 0.
        m = round(projection_scale(orthobasis[j], basis[k]))
        total_reduction += np.dot(m, basis[j])[0]
        basis[k] -= np.dot(m, basis[j]) # Reduce the working vector by multiples of preceding vectors.
    if total_reduction > 0:
        gram_schmidt(basis) # Recompute Gram-Scmidt if the working vector has been reduced. 

def lovasz(basis, orthobasis):
    global k
    '''Checks the Lovasz condition for a basis. Either swaps adjacent basis vectors and recomputes Gram-Scmidt or increments the working index.'''
    c = DELTA - projection_scale(orthobasis[k-1], basis[k])**2
    if la.norm(orthobasis[k])**2 >= np.dot(c, la.norm(orthobasis[k-1]**2)): # Check the Lovasz condition.
        k += 1  # Increment k if the condition is met.
    else: 
        basis[[k, k-1]] = basis[[k-1, k]] # If the condition is not met, swap the working vector and the immediately preceding basis vector.
        gram_schmidt(basis) # Recompute Gram-Schmidt if swap
        k = max([k-1, 1])

def main():
    gram_schmidt(basis)
    print 'Performed Gram Schmidt. Basis: ', basis, " , Orthobasis: ", orthobasis
    raw_input("")
    while k <= basis.shape[1] - 1:
        reduction(basis, orthobasis)
        print 'Performed Reduction. Basis: ', basis, " , Orthobasis: ", orthobasis
        raw_input("")
        lovasz(basis, orthobasis)
        print 'Checked Lovasz Condition. Basis: ', basis, " , Orthobasis: ", orthobasis
        raw_input("")
    print 'LLL Reduced Basis: ', basis

if __name__ == "__main__":
    main()