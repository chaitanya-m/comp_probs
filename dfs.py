#Implement depth first search
#Also a tree generator
#Let children be between 0 and 3

import random, math

class Node(object):

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def setParent(self, parent):
        self.parent = parent

    def nodeValue(self):
        return self.value


class Tree(object):

    def __init__(self, depth):
        self.nodePath = []
        self.depth = depth
        self.TreeGen(self.depth)

    def TreeGen(self, depth):
        print "Generating tree..."
#        r = random.Random()
#        root = Node(r.random())
        self.root = Node(random.randint(pow(10,5), pow(10,6)))
        print self.root.nodeValue()

        parents = []
        newParents = []
        parents.append(self.root)

        for i in range(depth):
            print("\n")
            for j in parents:

                print("||"),

                numChildren = random.randint(1,3)

                for k in range(1, numChildren+1):
                    n = Node(random.randint(1, pow(3,i+1)))
                    print n.nodeValue(),
                    j.addChild(n)
                    n.setParent(j)
                    newParents.append(n)
                print("||"),


            parents = list(newParents) #list(): otherwise it's just a softcopy in Python
            newParents = []

    def getRoot(self):
        return self.root

#is it any more efficient to return early if the node is found?
class dfs(object):

    def __init__(self, tree):
        self.tree = tree
        self.root = tree.getRoot()
        self.path = []
        self.nodeFound = False

    def dfs(self, value, node = None):
        if node is None:
            node = self.root
            self.nodeFound = False

        if node.getValue() == value:
            self.nodeFound = True
            p = node
            self.path.append(p)
            while p != self.root:
                p = p.parent
                self.path.append(p)
            print "Node FOUND. Path is %s" % ('->'.join([str(i.nodeValue()) for i in self.path]))

            return

        for i in node.getChildren():
            if self.nodeFound == False:
                self.dfs(value, i)
            else:
                break
        return


t = Tree(3)
d = dfs(t)

while 1 > 0:
    s = raw_input()
    if s:
        d.dfs(int(s))
    else:
        break
