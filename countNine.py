
from random import randint

def countValsofNine():

    lst = []
    for i in range(1000):
        lst.append(randint(1,15))

    print(lst.count(9))

countValsofNine()
