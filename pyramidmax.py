import sys

class PyramidGraph(object):


    # Reads a line of nubers and returns a list of nodes
    def GetNodes(self, numString):
        nodes = []
        if not numString:
            return nodes

        numberStrs = numString.strip().split(" ")
        for numberStr in numberStrs:
            node = {"data": int(numberStr)}
            nodes.append(node)
        return nodes

    # Takes two nodelists connecting the children to the parents.
    # Each parent node adds a child node to its left and right
    # in the form of a connected graph
    def AddChildren(self, parents, children):
        if parents :
            index = 0
            for parent in parents:
                parent["left"] = children[index]
                index += 1
                parent["right"] = children[index]

    def GetLines(self, filePath):
        with open(filePath, "r") as f:
            return f.read().split("\n")

    # Reads a file with numbers arranged in pyramid as follows
    # and created a connected graph
    #           1
    #          2 2
    #         3 3 3

    def __init__(self, filePath):
        lines = self.GetLines(filePath)
        prevNodeList = None
        for line in lines:
            nodes = self.GetNodes(line)
            if not prevNodeList:
                self.rootNode = nodes[0] #Begining of the pyramid
            self.AddChildren(prevNodeList, nodes)
            prevNodeList = nodes

    def MaxSweep(self):
        self.max = None
        self.memo = {}
        self.Traverse(0, self.rootNode, 0)

    # Forking off threads to continue job
    def Traverse(self, sumTillNow, node ,nodeDepth):
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
pyrData.MaxSweep()
print "The Maximum value in this pyramid is",pyrData.max
