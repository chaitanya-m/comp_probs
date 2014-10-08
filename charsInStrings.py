#Given two strings, print their intersection ordered by the first string

import collections

print "String1:"
string1 = raw_input()

print "String2:"
string2 = raw_input()

#Solution 1: use Python set() 
s1 =set(string1)
s2 =set(string2)
ints1s2 = s1 & s2

print ints1s2

result = ''

for i in string1:
    if i in ints1s2:
        ints1s2.remove(i)
        result+=i

print result


#Solution 2: N*N brute force

result = ''
s3 = set()
for i in string1:
    for j in string2:
        if i==j and i not in s3:
            s3.add(i)
            result += i
print result

#Solution 3: N- use an ordered dictionary

d = collections.OrderedDict()
for i in string1:
    d[i] = 0
for i in string2:
    if i in d.keys():
        d[i] += 1

print d
