import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

def construct_data(m=10, n=1, sigma=0.5, f=None):
    """Return data with m attributes and continuous class."""
    X = np.array([np.ones(m)] + [np.random.random(m) for _ in range(n)]).T
    if not f:
        theta = np.arange(n+1)
        y = X.dot(theta)
    else:
        y = np.array([f(x[1:]) for x in X])
    return X, y + np.random.normal(0, sigma, m)

def normal_lin_reg(X, y, lmbd=0.):
    """Parameters of linear regression by normal equation."""
    n = X.shape[1] - 1
    return np.linalg.inv((X.T.dot(X)) + lmbd*np.diag(np.append(np.zeros(1), np.ones(n)))).dot(X.T.dot(y))

def predict_lin_reg(X, theta):
    """Linear regression predictions for a data set"""
    return X.dot(theta)

def feature_extend(X, n_features=1):
    """Return data matrix with added columns of x1**n"""
    return np.column_stack([X] + [X[:,1]**(i+2) for i in range(n_features)])

nf = 5 # number of higher-order features
k = 50 # number of test examples
m = 10 # train data set size
lmbd = 0.000 # regularization, increase to 0.001 to see the effect

X, y = construct_data(m=m, sigma=0.05, f=lambda x: 1-(x[0]-0.5)**2)
X = feature_extend(X, n_features=nf)
T = np.array([np.ones(k)] + [np.linspace(min(X[:,1]), max(X[:,1]), k)]).T
T = feature_extend(T, n_features=nf)
theta = normal_lin_reg(X, y, lmbd=lmbd)
print "Normal eq.:", theta

plt.close()
plt.plot(X[:,1], y, "o")
plt.plot(T[:,1], predict_lin_reg(T, theta))
plt.xlabel("x1")
plt.ylabel("y")
plt.title("Polynomial regression (lambda=%.5f)" % lmbd)
plt.savefig("0.pdf")
plt.savefig("0.png")