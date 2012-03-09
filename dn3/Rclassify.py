class RClassify:
    def __init__(self, lightData, lightLabels):
        
        counter = []
        self.predictedClasses = {}
        #lightData = [[500, 0, 200],[0, 100, 50], [0,0,20],[20,0,0]]
        #lightLabels = [[1,2,3], [1,5],[1,6],[7]]
        
        # initialize the counter variable
        for i in xrange(len(lightData[0])):
            # for each attribute:
            counter.append({})
            for j in xrange(len(lightData)):
                # for each example:
                for k in lightLabels[j]:
                    # for each class of the example:
                    if lightData[j][i] > 0:
                        # if lightData[j][i] is more than zero
                        if counter[i].has_key(str(k)): continue 
                        else: counter[i][str(k)] = {'sum': 0, 'count': 0, 'sumN': 0, 'countN':0}
            
        # insert actual data:
        for i in xrange(len(lightData[0])):
            # for each attribute:
            for j in xrange(len(lightData)):
                # for each example:
                added = False
                for k in lightLabels[j]:
                    # for each class of the example:
                    if lightData[j][i] > 0:
                        added = True
                        # if lightData[j][i] is more than zero
                        counter[i][str(k)]['sum'] += lightData[j][i]
                        counter[i][str(k)]['count'] += 1
                if added:
                    for k in counter[i].keys():
                        if(int(k) not in lightLabels[j]):
                            counter[i][k]['sumN'] += lightData[j][i]
                            counter[i][k]['countN'] += 1
#            
            for l in (sorted(counter[i].items(), key=lambda t: t[1]['sum'], reverse=True)):
                #print l[1]['sum']/(l[1]['count']+0.000001)-al[1]['sumN']/(l[1]['countN']+0.000001)
                #print l[1]['sumN'], l[1]['countN'], l[1]['sum'], l[1]['count'], l[1]['sumN']/(l[1]['countN']+0.000001),l[1]['sum']/(l[1]['count']+0.000001)
                #print l[1]['sum']*(l[1]['count']+0.000001)-l[1]['sumN']*(l[1]['countN']+0.000001)
                if not self.predictedClasses.has_key(str(i)):
                    self.predictedClasses[str(i)] = []
                self.predictedClasses[str(i)].append({'c':l[0], 'p':l[1]['sum'],'n':l[1]['count'], 'nN': l[1]['countN'],'pN':l[1]['sumN'] , 'r': l[1]['sum']/(l[1]['count']+0.000001)-l[1]['sumN']/(l[1]['countN']+0.000001)})# 'p':l[1]/float(allC)})
 #               allC = len([a for a,x in enumerate(lightLabels) if int(l[0]) in x])
                #print l[1]/float(allC)
  #              if l[1]/float(allC) > ERROR_THRESH:
   #                 if not self.predictedClasses.has_key(str(i)):
    #                    self.predictedClasses[str(i)] = []
                    #print self.predictedClasses[str(i)], str(i)
    def getClasses(self, row):
        counter = {}
        
        for i,x in enumerate(row):
            if x == 0: continue
            if not self.predictedClasses.has_key(str(i)): continue
            for y in self.predictedClasses[str(i)]:
#                if y['n'] - y['nN'] > 0:
#                    print y['c'], y['p'], y['n'], y['pN'], y['nN']
                if not counter.has_key(str(y['c'])):
                    counter[str(y['c'])] = y['p']
                else:
                    counter[str(y['c'])] += y['p']
                    
        print counter
        theC = []
        #print "all: " + str(counter)
        for l in (sorted(counter.items(), key=lambda t: t[1], reverse=True)):
            if len(theC) > 3:
                break
            theC.append(int(l[0]))
            #print l[1]
        if len(theC) == 0:
            return [40, 44, 18, 62, 41]
            
        #print theC[:THRESH] 
        return theC           
                