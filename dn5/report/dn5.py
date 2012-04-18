from matplotlib import pyplot as plt
import numpy as np

def get_data(f):
    """
    Gets data from a two column csv file (col1,col2)
    """
    f = open(f).readlines()
    x = [float(d.strip().split(',')[0]) for d in f[1:]]
    y = [float(d.strip().split(',')[1]) for d in f[1:]]
    return (x,y)

def plot_scatter(x, y):
    """
    Scatter plots the data and saves the result in scatter.png 
    """
    plt.plot(x, y, marker='.', linestyle=' ', color='b')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Podatki iz ml-class.org")
    plt.savefig('scatter.png')
    plt.show()
    plt.close()
    
def plot_contour(x,y):
    """
    Plots a contour
    """
    
    theta_0 = np.linspace(-12, 4, 120)
    theta_1 = np.linspace(0, 3, 120)
    
    J = np.zeros(shape=(theta_0.size, theta_1.size))
    
    for i, t0 in enumerate(theta_0):
        for j, t1 in enumerate(theta_1):
            J[i, j] = cost_function(x, y, t0, t1)
    
    plt.contour(theta_0, theta_1, J.T, np.logspace(0, 2, 18))
    plt.xlabel("Theta 0")
    plt.ylabel("Theta 1")
    plt.title("Contuor plot podatkov")
    plt.savefig('contour.png')
    #plt.show()
    
def plot_line(x,y,theta, color):
    '''
    Plots a line calculated from the given theta
    '''
    x = list(np.linspace(min(x), max(x), 60))
    y = []
    
    for i in x:
        y.append(i*theta[1]+theta[0])
    
    plt.plot(x,y,linestyle='-', color=color)
    #plt.show()

def h(X, theta):
    return X * theta.T 

def gradient_descent(x, y, alpha, iterations, eps):
    '''
    Calculates and plots the gradient descent method
    
    Returns: Theta
    '''
    X = [np.ones(len(x)), x]
    X = np.matrix(X).T
    #y= [zeros(len(y)), y]
    Y = np.matrix(y).T
    theta = np.matrix([2, 2])
    hist = [[theta[:,0]], [theta[:,1]]]

    for _ in xrange(iterations):
        theta = theta - alpha * sum([(h(X[j,:], theta) - Y[j]) * X[j,:] for j in range(X.shape[0])])
        #print theta
        hist[0].append(theta[:,0])
        hist[1].append(theta[:,1])
        if abs(hist[0][-1]-hist[0][-2] + hist[1][-1]-hist[1][-2]) < eps:
            break
    
    hist = [np.array(hist[0]).flatten().tolist(), np.array(hist[1]).flatten().tolist()]
    plt.plot(hist[0], hist[1], marker='.', linestyle='-', color='b')
    plt.title('Paketna metoda')
    plt.savefig('batch.png')
    
    return np.array([hist[0][-1], hist[1][-1]]).flatten().tolist()

def gradient_descent_ana(x,y):
    '''
    Returns theta from the analitical gd method
    '''
    X = [np.ones(len(x)), x]
    X = np.matrix(X).T
    #y= [zeros(len(y)), y]
    Y = np.matrix(y).T
    theta = list((X.T*X).I*X.T*Y)
    return np.array(theta).flatten().tolist()
    
def gradient_descent_sto(x, y, alpha, iterations, eps):
    '''
    Calculate and plot stochastic gd method
    
    Returns: Theta
    '''
    X = [np.ones(len(x)), x]
    X = np.matrix(X).T
    #y= [zeros(len(y)), y]
    Y = np.matrix(y).T
    theta = np.matrix([2, 2])
    hist = [[theta[:,0]], [theta[:,1]]]
    for _ in xrange(iterations):
        for j in range(X.shape[0]):
            theta = theta - alpha * (h(X[j,:], theta) - Y[j]) * X[j,:]
            hist[0].append(theta[:,0])
            hist[1].append(theta[:,1])
    hist = [np.array(hist[0]).flatten().tolist(), np.array(hist[1]).flatten().tolist()]
    plt.plot(hist[0], hist[1], marker='.', linestyle='-', color='r')
    plt.title('Stohasticna metoda')
    plt.savefig('sto.png')
    #plt.show()
    return np.array([hist[0][-1], hist[1][-1]]).flatten().tolist()

def cost_function(x, y, theta0, theta1):
    '''
    Compute cost for linear regression
    '''
    return sum([(x1*theta1+theta0-y[i])**2 for i,x1 in enumerate(x)])*0.5/len(x)

if __name__ == '__main__':
    
    #x,y = get_data('data/dm.csv')
    x,y = get_data('data/ex1data1.txt')
    plot_contour(x, y)
    # Izracunamo thete razlicnih metod
    
    theta_gd  = gradient_descent(x, y, 0.0001, 1000, 10**-3)
    theta_gds = gradient_descent_sto(x, y, 0.0001, 1000, 10**-5)
    theta_a   = gradient_descent_ana(x, y)
    print theta_gd, theta_gds, theta_a    
    plt.show()

    
    # Izrisemo izracunane premice 
    plot_scatter(x, y)
    plot_line(x,y,theta_gd,'b')
    plot_line(x,y,theta_gds,'r')
    plot_line(x,y,theta_a,'y')
    plt.savefig('result.png')
    plt.show()
    exit()

    
    
    
    
