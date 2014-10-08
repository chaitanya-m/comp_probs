
#Given a circular list, what is the fastest way to find the smallest integer?

#Solution: Let us assume we do not know the size N.
#If we had two pointers traversing the list, one by one step and one by two,
#they will traverse (1, 2), (2, 4)... (N, 2N) steps. i.e. they will meet at N=2N (because the list is circular).
#when they meet, we know that the list has been traversed for sure. At this point, we can stop our search.

circular_list = [22, 52, 66, 82, 8, 12, 19]

class Node(object):
    #data members defined outside init are static (common to all objects)
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

class CircularList(object):

    def __init__(self, l):
        self.clist = []
        self.buildList(l)

    def buildList(self, l):
        lastIndex = len(l) - 1
        for i, e in enumerate(l):
            #print i, e
            n = Node(e)
            self.clist.append(n)
            if i != 0:
                self.clist[i-1].setNext(self.clist[i])
            else:
                pass
        self.clist[lastIndex].setNext(self.clist[0])
        self.currentNode = self.clist[0]

    def findMinInt(self):
        onePlus = self.currentNode.next
        twoPlus = self.currentNode.next.next
        minimum = self.currentNode.getValue()
        if onePlus.getValue() < minimum:
            minimum = onePlus.getValue()
        elif twoPlus.getValue() < minimum:
            minimum = twoPlus.getValue()
        else:
            pass

        while onePlus != twoPlus:
            onePlus = onePlus.next
            twoPlus = twoPlus.next.next

            if onePlus.getValue() < minimum:
                minimum = onePlus.getValue()
            elif twoPlus.getValue() < minimum:
                minimum = twoPlus.getValue()
            else:
                pass

        return minimum


if __name__ == "__main__":
    c = CircularList(circular_list)
    print c.findMinInt()
