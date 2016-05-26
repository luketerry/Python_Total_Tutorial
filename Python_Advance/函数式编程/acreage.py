
from __future__  import print_function
Pi = 3
def acreage(r):
    global Pi
    Pi = 3.14
    return Pi*r**2
def perimeters(r):
    return Pi*r*2
def acreage1(r):
    Pi = 3.1
    return Pi*r**2

if __name__=='__main__':
    print(perimeters(2))
    print(acreage1(2))
    print(acreage(2))
    print(acreage1(2))
    print(perimeters(2))