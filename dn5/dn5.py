'''
Created on Apr 5, 2012

@author: smotko
'''

from matplotlib import pyplot as plt

def get_data(file):
    f = open(file).readlines()
    a = [int(x.strip().split(',')[0]) for x in f[1:]]
    b = [float(x.strip().split(',')[1]) for x in f[1:]]
    return (a,b)


def plot_raw(x, y):
    plt.close()
    plt.plot(x, y, marker='.', linestyle=' ', color='b', label='Pogodbe')
    plt.legend()
    plt.xlabel("St. obrokov")
    plt.ylabel("Vrednost pogodbe")
    plt.title("Vrednost pogodbe glede na stevilo obrokov")
    plt.savefig('pogodbe.png')
    plt.show()
    plt.close()


if __name__ == '__main__':
    x,y = get_data('dm.csv')
    plot_raw(x,y)