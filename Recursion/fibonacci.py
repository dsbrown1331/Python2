def fib(n):
    """recursive function that returns the nth Fibonacci number
    where fib(0) = 0, fib(1) = 1 and fib(n) = fib(n-1) + fib(n-2)
    """
    print("calling fib({})".format(n))
    #base cases
    if n == 0:
        print("returning 0")
        return 0
    elif n == 1:
        print("returning 1")
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(4)
#testing code
#for i in range(0,11):
#    print("The {}th Fibonacci number is {}".format(i, fib(i)))
