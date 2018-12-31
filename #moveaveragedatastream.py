'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
'''


class Movingaverage:
    def __init__(self,size):
        self.size=size
        self.l=[]
        self.sum=0
    def next(self,val):
        if(len(self.l)==self.size):
            self.sum-=self.l.pop(0)
        self.l.append(val)
        self.sum+=val
        return self.sum/len(self.l)
x=Movingaverage(3)
print(x.next(1))
print(x.next(10))
print(x.next(3))
print(x.next(5))
