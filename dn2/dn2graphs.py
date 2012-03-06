from matplotlib import pyplot as plt
import cPickle

FILE_NAMES = ["dump-500-0.05.pickled", "dump-100-0.05.pickled", "dump-100-0.01.pickled", "dump-100-0.0.pickled"]


for FILE_NAME in FILE_NAMES:
    PERM = FILE_NAME.split('-')[1]
    ALPHA = FILE_NAME.split('-')[2][2:4].replace('.', '')
    
    data = cPickle.load(open(FILE_NAME))
    
    attrs = [0]*2026
    max = 0
    
    for i in data:
        for j in i['i']:
            if j > max: max = j
            attrs[j] += 1
    
    plt.close()
    plt.yscale('log')
    plt.hist(attrs, 24, range=(0, 70))
    plt.xlabel("St. razredov")
    plt.ylabel("St. atributov")
    plt.title("St. razredov na posamezen atribut (alpha 0.%s)" % ALPHA)
    plt.savefig('report/attr-%s-%s.png' % (PERM, ALPHA))
  #  plt.show()
    plt.close()  
    
    
    hist = []
    for i in xrange(len(data)):
        hist.append(len(data[i]['i']))
    
    
    
    plt.close()
    plt.hist(hist, 24, range=(0, 1800))
    plt.xlabel("St. atributov")
    plt.ylabel("St. razredov")
    plt.title("St. atributov na posamezen razred (alpha 0.%s)" % ALPHA)
    plt.savefig('report/%s-%s.png' % (PERM, ALPHA))
   # plt.show()
    plt.close()
