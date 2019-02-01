import numpy as np
from numpy import linalg as la

# Basis vectors arranged in rows of basis, not columns.
# basis = np.array([[--b1--],
#               [--b2--], 
#               [--b3--]]) 

# dummy data
basis = np.array([[201, 37], 
                [1648, 297]]).astype(float)

orthobasis = basis.copy()

DELTA = 0.75

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
    for basis_index in range(1, orthobasis.shape[0] + 1):
        for projection_index in range(basis_index - 1, 0, -1):
            m = round(projection_scale(orthobasis[projection_index - 1], basis[basis_index - 1]))
            basis[basis_index - 1] -= np.dot(m, basis[projection_index - 1])
            if basis.shape[0] > 2:
                gram_schmidt(basis)

def lovasz(basis, orthobasis):
    '''Checks Lovasz condition on a given set of basis vectors. If condition is met, swaps adjacent basis vectors and re-orthogonalizes the basis.'''
    for basis_index in range(0, orthobasis.shape[0] - 1):
        mark = la.norm(np.add(np.dot(projection_scale(orthobasis[basis_index], basis[basis_index + 1]), orthobasis[basis_index]), orthobasis[basis_index + 1]))
        if mark * mark < DELTA * la.norm(orthobasis[basis_index]) * la.norm(orthobasis[basis_index]):
            basis[[basis_index, basis_index + 1]] = basis[[basis_index + 1, basis_index]]
            gram_schmidt(basis)

# testing
gram_schmidt(basis)
print 'GS ', basis, orthobasis
reduction(basis, orthobasis)
print 'Reduction and GS ', basis, orthobasis
lovasz(basis, orthobasis)
print 'Lovasz and GS', basis, orthobasis
reduction(basis, orthobasis)
print 'Reduction and GS ', basis, orthobasis 
lovasz(basis, orthobasis)
print 'Lovasz and GS ', basis, orthobasis
reduction(basis, orthobasis)
print 'Reduction and GS ', basis, orthobasis
lovasz(basis, orthobasis)
print 'Lovasz and GS ', basis, orthobasis
            


