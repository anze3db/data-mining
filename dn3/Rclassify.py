class RClassify:
    def __init__(self, lightData, lightLabels):
        
        THRESH = 1500
        ERROR_THRESH = 0.05
        counter = []
        self.predictedClasses = {}
        
        for i in xrange(len(lightData[0])):
            # for each attribute:
            counter.append({})
            for j in xrange(len(lightData)):
                # for each example:
                for k in lightLabels[j]:
                    # for each class of the example:
                    if lightData[j][i] > 0:
                        # if lightData[j][i] is more than zero
                        if counter[i].has_key(str(k)): 
                            counter[i][str(k)]['sum'] += lightData[j][i]
                            counter[i][str(k)]['count'] += 1
                        else: counter[i][str(k)] = {'sum': lightData[j][i], 'count': 1}
                        
            for l in (sorted(counter[i].items(), key=lambda t: t[1], reverse=True)):
                if l[1]['sum'] < THRESH: break
                if not self.predictedClasses.has_key(str(i)):
                    self.predictedClasses[str(i)] = []
                self.predictedClasses[str(i)].append({'c':l[0], 'p':l[1]['sum'], 'n':l[1]['count']})# 'p':l[1]/float(allC)})
 #               allC = len([a for a,x in enumerate(lightLabels) if int(l[0]) in x])
                #print l[1]/float(allC)
  #              if l[1]/float(allC) > ERROR_THRESH:
   #                 if not self.predictedClasses.has_key(str(i)):
    #                    self.predictedClasses[str(i)] = []
                    #print self.predictedClasses[str(i)], str(i)
    def getClasses(self, row):
        counter = {}
        THRESH = 1000
        
        for i,x in enumerate(row):
            if x == 0: continue
            if not self.predictedClasses.has_key(str(i)): continue
            for y in self.predictedClasses[str(i)]:
                if not counter.has_key(str(y['c'])):
                    counter[str(y['c'])] = y['p']/float(y['n'])
                else:
                    counter[str(y['c'])] += y['p']/float(y['n'])
        theC = []
        #print "all: " + str(counter)
        for l in (sorted(counter.items(), key=lambda t: t[1], reverse=True)):
            #if l[1] < THRESH:
            #    break 
            if len(theC) > 3:
                break
            theC.append(int(l[0]))
            print l[1]
        if len(theC) == 0:
            return [40, 44, 18, 62, 41]
            
        #print theC[:THRESH] 
        return theC           
                