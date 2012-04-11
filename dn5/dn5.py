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
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Podatki iz ml-class.org")
    plt.savefig('scatter.png')
    plt.show()
    plt.close()
    
def plot_contour():
    """
    Plots a contour
    """
    pass


#Evaluate the linear regression
def criteria_function(x, y, theta):
    '''
    Compute cost for linear regression
    '''
    return 0.5/len(x) * ((x.dot(theta).flatten()-y)**2).sum()

if __name__ == '__main__':
    #x,y = get_data('data/dm.csv')
    x,y = get_data('data/ex1data1.txt')
    #plot_scatter(x,y)
    
    
    # Add a column of ones to X (interception data)
    it = ones(shape=(len(x), 2))
    it[:, 1] = x
    print it
    # Grid over which we will calculate J
    theta_0 = linspace(-10, 10, 100)
    theta_1 = linspace(-1, 3, 100)
    
    
    # initialize J_vals to a matrix of 0's
    J_vals = zeros(shape=(theta_0.size, theta_1.size))
    
    # Fill out J_vals
    for t1, element in enumerate(theta_0):
        for t2, element2 in enumerate(theta_1):
            thetaT = zeros(shape=(2, 1))
            thetaT[0][0] = element
            thetaT[1][0] = element2
            J_vals[t1, t2] = criteria_function(it, y, thetaT)
    
    # Contour plot
    J_vals = J_vals.T
    #Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
    plt.contour(theta_0, theta_1, J_vals, logspace(0, 2.5, 25))
    plt.show()
    