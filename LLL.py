import numpy as np

# Basis vectors will be in rows, not columns.
# Input will come from command line: b1, b2, so on. 
# B = np.matrix([[b1],
#               [b2], 
#               [b3]])

B = np.array([[3, 1], 
                [2, 2]])

def proj(u, v):
    '''Computes the projection of vector v onto vector u.'''
    print 'u is ', u 
    print 'v is ', v
    mu = np.dot(u, v) / np.dot(u, u)
    print 'mu is ', mu
    return np.dot(mu, u)

def gram_schmidt(B): 
    '''Computes Gram Schmidt orthoganalization without normalization of a set of basis vectors.'''
    B = 1.0 * B
    O = B.copy()
    for i in range(0, B.shape[1]):
        for j in range(0, i):
            print 'O is ', O
            O[i] -= proj(O[j], B[i])
            print 'O[i] is ', O[i]
    return O

# def reduction(matrixA):


# def lovasz(matrixA):


# def lll_reduction(matrixA):

print gram_schmidt(B)
