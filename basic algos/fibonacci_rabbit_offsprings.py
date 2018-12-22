def fib(x):
    """ assume x an int >= 0
        returns Fibonacci of x """
        
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
    

print(fib(5))    


def fib_efficient(n,d):
    """ better recursive version with memoization method
    saving the calculated values So calc only once. """
    
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
    
d = {1:1,2:2}

print(fib_efficient(5,d))