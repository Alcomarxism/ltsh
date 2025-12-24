
import numpy as np

X=np.array([
    [17,17,12],
    [11,9,13],
    [11,8,19]
    ]).transpose()
covmat=np.cov(X)
print("Covariance matrix:\n",covmat)
print("Generalized variance: ", np.linalg.det(covmat))
