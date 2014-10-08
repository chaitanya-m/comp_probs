#Given a function that can return a random integer between 1 and 5 included,
#write a function that will return a random integer between 1 and 7

import random

def getRandInt5():
    return random.randint(1,5)

def getRandInt7():
    r = getRandInt5()
    reNormalise = int(round(float(r)*7.0/5.0, 0))
    print r, reNormalise
    return reNormalise

def generate():
    for i in range(100):
        yield getRandInt7()

def analyse():
    count = 0
    for i in generate():
        #print i
        if i%7 > 5:
            count+=1
    print count

analyse()
