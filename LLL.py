import numpy as np
from numpy import linalg as la

# Basis vectors will be in rows, not columns.
# Input will come from command line: b1, b2, so on. 
# B = np.array([[--b1--],
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
    for i in range(0, basis.shape[1]):
        for j in range(0, i):
            orthobasis[i] -= proj(orthobasis[j], basis[i])
    return orthobasis

def reduction(basis, orthobasis):
    '''Performs length reduction on a given set of basis vectors. Updates and re-orthogonalizes basis vectors.'''
    for basis_index in range(1, orthobasis.shape[0] + 1):
        for projection_index in range(basis_index - 1, 0, -1):
            m = round(projection_scale(orthobasis[projection_index - 1], basis[basis_index - 1]))
            basis[basis_index - 1] -= np.dot(m, basis[projection_index - 1])
            if basis.shape[0] > 2:
                gram_schmidt(basis)


# b1, b2, b3, .... vs basis[0], basis[1], basis[2], ....
def lovasz(basis, orthobasis):
    for basis_index in range(0, orthobasis.shape[0] - 1):
        a = projection_scale(orthobasis[basis_index], basis[basis_index + 1])
        b = np.dot(a, orthobasis[basis_index]) 
        c = np.add(b, orthobasis[basis_index + 1])
        print 'c adding to b by ', orthobasis[basis_index + 1]
        d = la.norm(c)
        e = d * d
        print 'a is ', a, ' b is ', b, 'c is ', c, ' d is ', d
        print 'e is ', e
        print 'criterion is ', DELTA * la.norm(orthobasis[basis_index]) * la.norm(orthobasis[basis_index])
        if e < DELTA * la.norm(orthobasis[basis_index]) * la.norm(orthobasis[basis_index]):
            print 'swapping ', basis[basis_index], basis[basis_index + 1]
            basis[[basis_index, basis_index + 1]] = basis[[basis_index + 1, basis_index]]
            # basis[basis_index], basis[basis_index + 1] = basis[basis_index + 1], basis[basis_index]
            gram_schmidt(basis)


gram_schmidt(basis)
print 'GS ', basis, orthobasis
reduction(basis, orthobasis)
print 'Reduction and GS ', basis, orthobasis
lovasz(basis, orthobasis)
print 'Lovasz and GS', basis, orthobasis
            


