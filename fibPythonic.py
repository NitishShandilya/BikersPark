"""
Generate fibonacci series of length n > 2
"""
def fibonacciSeries(n):
    fib = [0,1,1]
    for i in range(2,n):
        fib.append(fib[-1] + fib[-2])
    return fib

n = 10
print fibonacciSeries(n)