import sys
import json
import numpy as np
from numpy import linalg as la

# Dummy data for testing
# basis = np.array([[201, 37], 
#                 [1648, 297]]).astype(float)

basis = np.array(json.loads(sys.argv[1])).astype(float)
orthobasis = basis.copy()

working_index = 1 # at least 2 basis vectors
DELTA = 0.75
ordered = False

def increment_working_index():
    '''Continue to the next basis vector. Called when all previous vectors have been reduced and ordered.'''
    if working_index < orthobasis.shape[0]:
        global working_index 
        working_index += 1
    else: 
        global ordered
        ordered = True

def projection_scale(u, v):
    return np.dot(u, v) / np.dot(u, u)

def proj(u, v):
    '''Computes the projection of vector v onto vector u. Assumes u is not zero.'''
    return np.dot(projection_scale(u, v), u)

def gram_schmidt(basis): 
    '''Computes Gram Schmidt orthoganalization (without normalization) of a set of basis vectors.'''
    orthobasis[0] = basis[0]
    for i in range(1, basis.shape[1]):
        orthobasis[i] = basis[i] - proj(orthobasis[i - 1], basis[i])
    return orthobasis

def reduction(basis, orthobasis):
    '''Performs length reduction on a given set of basis vectors. Updates and re-orthogonalizes the basis.'''
    for projection_index in range(working_index - 1, -1, -1):
        m = round(projection_scale(orthobasis[projection_index ], basis[working_index ]))
        basis[working_index] -= np.dot(m, basis[projection_index ])
        if basis.shape[0] > 2:
            gram_schmidt(basis)

def lovasz(basis, orthobasis):
    '''Checks Lovasz condition on a given set of basis vectors. If condition is met, swaps adjacent basis vectors and re-orthogonalizes the basis.'''
    for basis_index in range(0, orthobasis.shape[0] - 1):
        mark = la.norm(np.add(np.dot(projection_scale(orthobasis[basis_index], basis[basis_index + 1]), orthobasis[basis_index]), orthobasis[basis_index + 1]))
        if mark * mark < DELTA * la.norm(orthobasis[basis_index]) * la.norm(orthobasis[basis_index]):
            basis[[basis_index, basis_index + 1]] = basis[[basis_index + 1, basis_index]]
            gram_schmidt(basis)
        else:
            increment_working_index()

def main():
    gram_schmidt(basis)
    print 'Gram Schmidt. Basis: ', basis, " , Orthobasis: ", orthobasis
    raw_input("")
    while ordered == False:
        reduction(basis, orthobasis)
        print 'Reduction and Gram Schmidt. Basis: ', basis, " , Orthobasis: ", orthobasis
        raw_input("")
        lovasz(basis, orthobasis)
        print 'Lovasz and Gram Schmidt. Basis: ', basis, " , Orthobasis: ", orthobasis
        raw_input("")
    print 'LLL Reduced Basis: ', basis

if __name__ == "__main__":
    main()