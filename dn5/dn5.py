'''
Created on Apr 5, 2012

@author: smotko
'''
from numpy import zeros, ones, array, linspace, logspace
from matplotlib import pyplot as plt

def get_data(file):
    """
    Gets data from a two column csv file (col1,col2)
    """
    f = open(file).readlines()
    x = [float(d.strip().split(',')[0]) for d in f[1:]]
    y = [float(d.strip().split(',')[1]) for d in f[1:]]
    return (x,y)


def plot_scatter(x, y):
    """
    Scatter plots the data and saves the result in raw.png 
    """
    plt.close()
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
    
    theta_0 = linspace(-12, 4, 20)
    theta_1 = linspace(-2, 4, 20)
    
    J = zeros(shape=(theta_0.size, theta_1.size))
    
    for i, t0 in enumerate(theta_0):
        for j, t1 in enumerate(theta_1):
            J[i, j] = cost_function(x, y, t0, t1)
    
    plt.contour(theta_0, theta_1, J.T, logspace(0, 2.5, 18))
    plt.xlabel("Theta 0")
    plt.ylabel("Theta 1")
    plt.title("Contuor plot podatkov")
    plt.savefig('contour.png')
    plt.show()

def gradient_descent(x, y, alpha, iterations):
    
    hist = zeros(shape=(iterations, 1))
    theta_0 = 0
    theta_1 = 0
    for i in xrange(iterations):
        pred = [(x1*theta_1+theta_0-y[i]) for i,x1 in enumerate(x)]
        e1 = pred * x
        # TODO: AAAAAAAA


def cost_function(x, y, theta0, theta1):
    '''
    Compute cost for linear regression
    '''
    return sum([(x1*theta1+theta0-y[i])**2 for i,x1 in enumerate(x)])*0.5/len(x)

if __name__ == '__main__':
    #x,y = get_data('data/dm.csv')
    x,y = get_data('data/ex1data1.txt')
    #plot_scatter(x,y)
    #plot_contour(x,y)
    
    
    
    