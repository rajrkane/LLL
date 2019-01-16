import numpy as np

# Basis vectors will be in rows, not columns.
# Input will come from command line: b1, b2, so on. 
# B = np.array([[--b1--],
#               [--b2--], 
#               [--b3--]]) 

# dummy data
basis = np.array([[3, 1], 
                [2, 2],
                [5, 4],
                [7, 1]]).astype(float)

orthobasis = basis.copy()

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
    for basis_index in range(2, orthobasis.shape[0]):
        print 'pass ', basis_index
        for projection_index in range(basis_index - 1, 0, -1):
            m = round(projection_scale(basis[basis_index], orthobasis[projection_index]))
            basis[basis_index] -= np.dot(m, basis[projection_index])
            gram_schmidt(basis)
