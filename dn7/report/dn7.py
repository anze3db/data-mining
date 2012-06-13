import Orange
import numpy as np
import scipy.optimize as opt

def k_fold(X, K):
    '''Compute k fold'''
    from random import shuffle
    X=list(X); shuffle(X)
    for k in xrange(K):
        training = [x for i, x in enumerate(X) if i % K != k]
        validation = [x for i, x in enumerate(X) if i % K == k]
        yield training, validation

def sigmoid(z):
    '''Compute the sigmoid function'''
    return 1.0 / (1.0 + np.exp(-z))

def logloss(x,y):
    """Return the log loss score"""
    return sum(x*np.log(y)+(1-x)*np.log(1-y))/x.size * -1 

def feature_extend(X):
    """Extend design matrix X with higher-order features."""
    return np.column_stack([X] + [X[:,1]*X[:,2]] + [X[:,1]**2] + [X[:,2]**2])

def log_reg(X, y, lambda_):
    
    m = X.shape[0]
    n = X.shape[1]
    thetas0 = np.zeros(n)
    

    def cost(theta, X, y, lambda_):
        '''Compute cost for logistic regression'''
        h_t = sigmoid(X.dot(theta))*0.9998 + 0.00001
        return -sum(y * np.log(h_t) + (1 - y) * np.log(1 - h_t))/m + lambda_ * sum(theta**2)
            
    def grad(thetas, X, y, lambda_):
        return (sigmoid(X.dot(thetas)) - y).dot(X)/m + lambda_*sum(2.0*thetas)
    
    return opt.fmin_l_bfgs_b(cost, thetas0, grad, args=(X, y, lambda_))

if __name__ == '__main__':
    
    data = Orange.data.Table("data/train.tab")
    X, y, _ = data.to_numpy()
    for a in [0.1, 0.01, 0.001, 0.0001, 0.0]:
        c = []
        for (t,v) in k_fold(range(len(X)),5):
            kX = np.array([X[i] for i in t])
            ky = np.array([y[i] for i in t])
            (thetas, _, _) = log_reg(kX,ky,a)
            
            kX = np.array([X[i] for i in v])
            ky = np.array([y[i] for i in v])
            c.append(logloss(ky,sigmoid(kX.dot(thetas))*0.9998 + 0.00001))
        print a, sum(c)/len(c)
