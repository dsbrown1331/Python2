def fib(n):
    """recursive function that returns the nth Fibonacci number
    where fib(0) = 0, fib(1) = 1 and fib(n) = fib(n-1) + fib(n-2)
    """
    #base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#TODO write code to print out recursion

#testing code
for i in range(0,11):
    print("The {}th Fibonacci number is {}".format(i, fib(i)))
