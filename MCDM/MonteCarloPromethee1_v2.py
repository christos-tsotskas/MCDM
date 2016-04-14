'''
Created,on,Nov,19,,2015

@author:,christos
'''
import math

m=10;
n=10;

def calculateNormalisedDecisionMatrix(x):
    r = [[]]
    for i in range(n):
        r.append(10*[0])
    
    
    for j in xrange(n):
        sum = 0
        for i in xrange(m):
            sum += x[i][j]** 2
        
        for i in xrange(m):
            r[i][j] = x[i][j] / math.sqrt(sum)
    



def Promethee1():

    
    x=[]
    x.append([1.6,7.7,7.8,5.9,6.6,7.4,6.6,7.7,5.7,7.7])
    x.append([2,7.2,6.3,5.8,6.2,6.9,6.2,7.2,5.3,7])
    x.append([2.7,6.5,5.7,4.7,5.9,6.5,5.2,7.8,4.4,6.1])
    x.append([3.3,6.1,5,5,5.3,6.5,5.1,5.9,4.5,5.3])
    x.append([3.2,6.6,6.1,5.4,4.6,5,5.9,6.8,7,6.4])
    x.append([5.8,5.9,5.1,4.8,4.8,3.6,5.3,5.4,6.5,3.9])
    x.append([6.6,4.6,5.3,4.6,3.8,3.4,5.3,5.2,5.9,5.6])
    x.append([4.2,6.6,4.4,5.7,5.6,5.2,6,5.5,7.3,5])
    x.append([5.6,5.8,5.3,4.6,4.2,3.7,5.9,5.6,6.7,5.9])
    x.append([5.5,5.7,4.9,5,3.9,3.5,5.7,4.3,6.4,5.7])
    
    w=[0.11,0.085,0.087,0.126,0.124,0.076,0.074,0.092,0.126,0.1]
    a=[-1, 1, 1, -1, -1, -1, -1, 1, -1, 1]
    
    
    
if __name__ == "__main__":
    Promethee1()
