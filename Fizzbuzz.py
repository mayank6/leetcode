class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a=[]
        def m35(x):
            if x%3 ==0 and x%5==0:
                return True
            return False
        def m3(x):
            if x%3 ==0:
                return True
            return False
        def m5(x):
            if x%5==0:
                return True
            return False
            
        for i in range(1,n+1):
            if m35(i):
                a.append("FizzBuzz")
            elif(m5(i)):
                a.append("Buzz")
            elif(m3(i)):
                a.append("Fizz")
            else:
                a.append(str(i))
        return a
