''' Definition von Funktionen

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def binary_noise(N=100, p=(0.5, 0.5)):
    """
    
    Args:
        N (int): Number of points to be sampled 
        p (1-D array-like, optional): The probabilities associated with 0 and 1 respectively.

    Returns:

    """
    numbers = np.random.choice([0, 1], size=(N,), p=p)
    return numbers


def multivariate_gaussian_noise(N=100, mean=(0, 0), covar=None):
    """Generate Multivariate Gaussian Noise
    
    Args:
        N (int): Number of points to be sampled 
        mean (1-D array-like, optional): Mean-Vector of the distribution 
        covar (2-D array-like, optional): Covariance Matrix of the distribution 
    
    Returns:
        Sampled Values
    """
    # Make a row vector from the mean
    mean = np.asarray(mean).reshape((1, -1))
    if covar is None:
        covar = np.eye(mean.shape[1])
    assert covar.shape[0] == mean.shape[1], 'Shapes of Mean and Covariance do not match.'
    gauss_uncorrelated = np.random.randn(N, covar.shape[0])
    A = np.linalg.cholesky(covar)
    gauss_correlated = gauss_uncorrelated@A.T
    gauss_correlated += mean
    return gauss_correlated

# Aufgabe 1: Generierung von binärem Rauschen
plt.figure()
plt.plot(binary_noise())
plt.ylabel('$y$')
plt.xlabel('Index $i$')
plt.show()


# Aufgabe 2: Sampeln aus multivariater Gaussverteilung
covar = np.array([[1, 0.8],
                  [0.8, 1]])
values = multivariate_gaussian_noise(N=1000, mean=(1, 0), covar=covar)
print('Mean of the MV-Gaussian:\n' + str(np.mean(values, axis=0)) + '\n')
print('Covariance of the MV-Gaussian:\n' + str(np.cov(values.T)))
plt.figure()
plt.scatter(values[:, 0], values[:, 1])
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.show()


