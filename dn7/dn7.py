import scipy.optimize as opt

def log_reg(X, y, lambda_):

    def cost(thetas, X, y, lambda_):
        pass
        
    def grad(thetas, X, y, lambda_):
        pass
    
    thetas0 = []
    return opt.fmin_l_bfgs_b(cost, thetas0, grad, args=(X, y, lambda_))
