#22. **Fibonacci Series (Function)**
#    Print the first `n` Fibonacci numbers using a function.
def printFibonacci(n):
    theSeries = [0,1]
    for x in range(2,n):
        next_sum = theSeries[x-1] + theSeries[x-2]
        theSeries.append(next_sum)
    return theSeries[:n]

print(printFibonacci(10))
        