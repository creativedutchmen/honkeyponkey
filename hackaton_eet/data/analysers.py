import numpy as np
import matplotlib.pyplot as plt

def get_correlation(X, y, names_X, names_y):
    """
    This function returns the correlation coefficients for all the features with the target signals. Will also plot
    the results.

    :param X: feature matrix
    :param y: target vector
    :param names_X: names of all features
    :param names_y: names of targets
    :return: (cr1, cr2) cr1 and cr2 are correlation coeffecient numpy arrays for both target signals (afnemen,
    indienen?)
    """
    cr1 = np.zeros(X.shape[1])
    cr2 = np.zeros(X.shape[1])

    for i in np.arange(X.shape[1]):
        cr1[i] = np.corrcoef(X[:, i], y[:, 0])[1, 0]
        cr2[i] = np.corrcoef(X[:, i], y[:, 1])[1, 0]

    ## plot correlation results of best 100 features
    idx = np.argsort(np.abs(cr1))
    idx = idx[-1:0:-1]

    M = 100

    # plt.subplot(122)
    idxm = M - np.arange(M)
    plt.barh(idxm, np.abs(cr2[idx[:M]]), label=names_y[1])
    plt.barh(idxm, np.abs(cr1[idx[:M]]), height=.5, label=names_y[0])
    plt.yticks(idxm, names_X[idx[:M]], fontsize=8)
    plt.grid()
    plt.xlabel('Absolute correlation coeff w. target $|\\rho|$')
    plt.tight_layout()
    plt.legend()

    return cr1, cr2