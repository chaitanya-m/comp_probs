#Reverse a string using iterative, recursive, library functions


l = []
s = raw_input()

r = s[::-1]
print "Python reverse iterator s[::-1] %s" %(''.join(r))


def recursiveReverse(s, reversed):
    
    if s == '':
        return ''
    elif len(s) == 1:
        return s[0]
    else:
        reversed+=recursiveReverse(s[1:], reversed)
        reversed += s[0]
        return reversed

print "Recursive reverse %s" %( recursiveReverse(s, ''))

def iterativeReverse(s):
    r = ''
    for i in range(1, len(s)+1):
        r+=s[-i]

    return r

print "Iterative reverse %s" % (iterativeReverse(s))

#Recursive string reverse:
#Base case:

