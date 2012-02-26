'''
Created on Feb 20, 2012

@author: smotko
'''
import collections
from matplotlib import pyplot as plt

fname = "dn1/trainingData.csv"
f = file(fname)
n = len(f.readlines()) # primeri
f.seek(0)
m = len(f.readline().strip().split("\t")) # atributi
print "%d instances, %d attributes" % (n, m) # atributi so tipa int

ipi = [] # items per data instance

f.seek(0)
c = collections.Counter()

for line in f:
    ind = [i for i, x in enumerate(line.strip().split("\t")) if x != "0"]
    ipi.append(len(ind))
    c.update(ind)
    
print "%f ratio" % (sum(ipi) / float(n * m))
print "%d of zero attributes" % (m - len(c.keys()))
print c.most_common(1)


tLabels = open('dn1/trainingLabels.csv', 'r').read().strip().split("\n")
tUnique = set()
tLabelsCount = []
labelsCounter = collections.Counter()

for i in xrange(len(tLabels)):
    tUnique.update(set(tLabels[i].strip().split(",")))
    labelsCounter.update(tLabels[i].strip().split(","))
    tLabelsCount.append(len(tLabels[i].strip().split(",")))
    tLabels.append(tLabels[i].strip().split(","))
    
print labelsCounter.most_common(3)
print max(tLabelsCount)
print "%d unique labels" % (len(tUnique))

plt.close()
plt.hist(ipi)
plt.xlabel("Stevilo nenicelnih atributov")
plt.ylabel("Stevilo primerov")
plt.title("St. nenicelnih atributov za posamezen primer")
plt.savefig('dn1/report/examples.png')
plt.close()

plt.hist(c.values(), bins=20, range=(0, 100))
plt.xlabel("Stevilo nenicelnih vrednosti")
plt.ylabel("Stevilo atributov")
plt.title("Stevilo nenicelnih vrednosti")
plt.savefig('dn1/report/attributes.png')
plt.close()

plt.hist(tLabelsCount)
plt.xlabel("Stevilo oznak (razredov)")
plt.ylabel("Stevilo primerov")
plt.title("Razlicne oznake v primerih")
plt.savefig('dn1/report/labels.png')
plt.close()


if __name__ == '__main__':
    pass
