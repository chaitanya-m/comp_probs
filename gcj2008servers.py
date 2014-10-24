#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r' ) as inputFile:
    l = inputFile.read().splitlines()

numCases = int(l.pop(0))
case = 0

def passList(server, sendList):
    pass

def findSwitches(numServers, serverSet, queryList):

    numSwitches = 0
    sendList = []
    clashQuery = ''
    currentServers = set(serverSet)

    if len(serverSet) == 1:
        numSwitches = 0

    while len(queryList) > 0:

        query = str(queryList.pop(0))
        sendList.append(query)

        if query in currentServers:
            if len(currentServers) > 1:
                currentServers.remove(query)
            elif len(currentServers) == 1:
                sendList.pop()
                numSwitches += 1
                clashQuery = query
                passList(query, sendList)
                del sendList[:]               
                queryList.insert(0, query)
                currentServers = set(serverSet)
#            print currentServers
#            print queryList
    #No more switches required, pick an arbitrary server to send list to
    passList(currentServers.pop(), sendList)
    return numSwitches    
            


while len(l) > 0:
    case += 1
    serverSet = set()
    numServers = int(l.pop(0))
#    print numServers
    for i in range(numServers):
        serverSet.add(str(l.pop(0)))
#    print serverSet
    queryList = []
    numQueries = int(l.pop(0))
    for i in range(numQueries):
        queryList.append(str(l.pop(0)))
#    print queryList
    numSwitches = findSwitches(numServers, serverSet, queryList)
    print "Case #%d: %d" %(case, numSwitches)
