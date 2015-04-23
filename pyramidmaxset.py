#By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

#        5
#      9  6
#    4   6  8
#  0   7  1   5

#I.e. 5 + 9 + 6 + 7 = 27.

import sys
import time


class PyramidGraph(object):

    # Parses line and returns an array of numbers 
    def GetNumbers(self,stringOfNumbers):
        nodeList = []
        if not stringOfNumbers:
            return nodeList
            
        numberStrs = stringOfNumbers.strip().split(" ")
        for numberStr in numberStrs:
            number = int(numberStr)
            nodeList.append(number)
        return nodeList
                
    
    def __init__(self,filePath):
        file = open(filePath,"r")
        str = file.read()
        file.close()
        self.lines = str.split("\n")
            
    # Evaluates pyramid from bottom and calculates the individual sum of each path possibility
    # as we move up tier by tier.
    # Example
    #
    def MaxSweep(self):
        maxVal = []
        lineindex = len(self.lines) - 1
        if lineindex == 0:
            maxVal = self.GetNumbers(self.lines[0])
            print "There is only one line"
        else:
            newSets = None
            while lineindex >= 0:
                tier = self.GetNumbers(self.lines[lineindex])
                start = time.time()
                newSets = self.EvaluateTiers(newSets,tier)
                end = time.time()
                print "Evaluation of tier",lineindex, end - start
                lineindex = lineindex - 1    
            print "Maximum total from top to bottom",max(newSets[0])
        return        
             
    def GetPathSum(self,number,sets):
        singleSet = []
        if sets is None: 
            singleSet.append(number)
        else:
            for currMax in sets[0]:
                singleSet.append(currMax+number)
            sets.remove(sets[0])
            for currMax in sets[0]:
                singleSet.append(currMax+number)
        
        return singleSet        
             
    def EvaluateTiers(self,sets,tier):
        newSets = []
        for number in tier:
            singleSet = self.GetPathSum(number,sets)
            newSets.append(singleSet)
        return newSets                

 
 
if len(sys.argv) == 1:
     print "Usage: pyramidmax.py <filecontainingnumbers>"
     print "Example of possible file contents:"
     print "5"
     print "9 6"
     print "4 6 8"
     print "0 7 1 5"
else:
    pyrData = PyramidGraph(sys.argv[1])
    pyrData.MaxSweep()
# print "The Maximum value in this pyramid is",pyrData.max