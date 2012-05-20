import scipy.optimize as opt

def log_reg(X, y, lambda_):

    def cost(thetas, X, y, lambda_):
        '''
        Compute cost for logistic regression
        '''
        return sum([(x1*thetas[1]+thetas[0]-y[i])**2 for i,x1 in enumerate(X)])*0.5/len(X)
            
    def grad(thetas, X, y, lambda_):
        pass
    
    thetas0 = []
    return opt.fmin_l_bfgs_b(cost, thetas0, grad, args=(X, y, lambda_))
