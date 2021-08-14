from sympy import *

if __name__ == '__main__':	
    res=solve('x**2/4+y**2-1','y')
    for i in range(len(res)):
        print(res[i].evalf(subs={'x':1},n=10))