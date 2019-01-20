#Write your code here


import sys

class Calculator():
    """docstring for Calculator"""
    
    @staticmethod
    def power(n,p):
        if n < 0 or p < 0:
        	assert ('linux' in sys.platform), "This code runs on Linux only."
            raise Exception("n and p should be non-negative")
        else:
            return(n**p)



myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   