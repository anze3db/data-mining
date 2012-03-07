class RClassify:
    def __init__(self, lightData, lightLabels):
        
        THRESH = 1500
        ERROR_THRESH = 0.05
        counter = []
        self.predictedClasses = {}
        
        for i in xrange(len(lightData[0])):
            counter.append({})
            for j in xrange(len(lightData)):
                for k in lightLabels[j]:
                    if lightData[j][i] > 0:
                        if counter[i].has_key(str(k)): counter[i][str(k)] += lightData[j][i]
                        else: counter[i][str(k)] = lightData[j][i]
                # TODO: odstej, druge...
            for l in (sorted(counter[i].items(), key=lambda t: t[1], reverse=True)):
                if l[1] < THRESH: break
                allC = len([a for a,x in enumerate(lightLabels) if int(l[0]) in x])
                if l[1]/float(allC) > ERROR_THRESH:
                    if not self.predictedClasses.has_key(str(i)):
                        self.predictedClasses[str(i)] = []
                    self.predictedClasses[str(i)].append({'c':l[0], 'p':l[1]/float(allC)})
                    #print self.predictedClasses[str(i)], str(i)
    def getClasses(self, row):
        counter = {}
        THRESH = 4
        
        for i,x in enumerate(row):
            if x == 0: continue
            if not self.predictedClasses.has_key(str(i)): continue
            for y in self.predictedClasses[str(i)]:
                if not counter.has_key(str(y['c'])):
                    counter[str(y['c'])] = 1
                else:
                    counter[str(y['c'])] += 1
        theC = []
        #print "all: " + str(counter)
        for l in (sorted(counter.items(), key=lambda t: t[1], reverse=True)):
            if l[1] > THRESH: 
                theC.append(int(l[0]))
            if len(theC) > 3:
                break
        if len(theC) == 0:
            return [40, 44, 18, 62, 41]
            
        #print theC[:THRESH] 
        return theC           
                