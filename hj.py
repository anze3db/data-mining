'''
Created on Feb 20, 2012

@author: smotko
'''

import collections
from matplotlib import pyplot as plt

fname = "minidata/trainingData.csv"
f = file(fname)
#n = len(f.readlines())
#f.seek(0)
#m = len(f.readline().strip().split("\t"))
#print "%d instances, %d attributes" % n, m

x = [2,5,6]
c = collections.Counter(x)
c.update([2,1])
print c

ipi = [] # items per data instance

f.seek(0)
c = collections.Counter()
for line in f:
    ind = [i for i,x in enumerate(line.strip().split("\t")) if x != "0"]
    ipi.append(len(ind))
    c.update(ind)
    
print c[1], c[2], c[3]
plt.close()
plt.hist(ipi)
plt.show()



if __name__ == '__main__':
    pass