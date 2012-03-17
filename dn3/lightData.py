a = open("../filteredData.csv")
lightData = []
for line in a:
    if len([int(i) for i in line.strip().split("\t")]) < 900: continue
    lightData.append([int(i) for i in line.strip().split("\t")])
    
b = open("../filteredLabels.csv")
lightLabels = []
for line in b:
    lightLabels.append([int(i) for i in line.strip().split(",")])
#    for i in xrange((len(lightLabels))):
#        if i in labels:
#            lightLabels[i].append(1)
#        else:
#            lightLabels[i].append(0)
            
    
            
