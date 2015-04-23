import sys
import threading

class PyramidGraph(object):

    # Reads a line of nubers and returns a list of nodes
    def GetNodes(self,stringOfNumbers):
        nodeList = []
        if not stringOfNumbers:
            return nodeList

        numberStrs = stringOfNumbers.strip().split( " ")
        for numberStr in numberStrs:
            number = int(numberStr)
            node = {}
            node["data"] = number
            nodeList.append(node)
        return nodeList

    # Takes two nodelists connecting the children to the parents.
    # Each parent node adds a child node to its left and right
    # in the form of a connected graph
    def AddChildNodes(self,parentNodeList,childNodeList):
        if parentNodeList is not None:
            index = 0
            for parentNode in parentNodeList:
                parentNode["left"] = childNodeList[index]
                index += 1
                parentNode["right"] = childNodeList[index]

    def GetLines(self,filePath):
        file = open(filePath,"r")
        str = file.read()
        file.close()
        lines = str.split("\n")
        return lines

    # Reads a file with numbers arranged in pyramid as follows
    # and created a connected graph
    #           1
    #          2 2
    #         3 3 3

    def __init__(self,filePath):
        lines = self.GetLines(filePath)
        prevNodeList = None;
        prevNodeCount = 0; #Maintains a counter to check the number of nodes at a given line
        self.nodeCount = 0;

        for line in lines:
            nodeList = self.GetNodes(line)
            numberOfNodes = len(nodeList)
            if prevNodeCount ==  numberOfNodes - 1:  #Pyramid is growing correctly, continue adding nodes
                if prevNodeCount == 0:
                    self.rootNode = nodeList[0] #Begining of the pyramid
                prevNodeCount = numberOfNodes
                self.nodeCount = self.nodeCount + numberOfNodes
                self.AddChildNodes(prevNodeList,nodeList)
                prevNodeList = nodeList


    def MaxSweep(self):
        self.max = None
        self.Traverse(0,self.rootNode,0)

    #Forking off threads to continue job
    def Traverse(self,sumTillNow,node,nodeDepth):
         if node.get('left') is None and node.get('right') is None: #We reached a bottom node
             self.CalculateBottom(sumTillNow, node["data"])
         else:
            self.Traverse(sumTillNow +node["data"],node["left"],nodeDepth)
            self.Traverse(sumTillNow +node["data"],node["right"],nodeDepth)


    def CalculateBottom(self,sumTillNow,data):
        if self.max is None:
           self.max = sumTillNow + data
        elif self.max < sumTillNow + data:
           self.max = sumTillNow + data

if len(sys.argv) == 1:
     print "Please enter name of file containing the pyramid of numbers"

pyrData = PyramidGraph(sys.argv[1])
print "Number of Nodes",pyrData.nodeCount
pyrData.MaxSweep()
print "The Maximum value in this pyramid is",pyrData.max
