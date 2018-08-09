def factorial(n):
    """ recursive function to compute the factorial of the integer n
        Example: factorial(5) returns 5*4*3*2*1
    """
    #base case n = 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#TODO: write print lines to see every call and n value

#code to test factorial()
for i in range(1, 11d):
    print("{}! is {}".format(i, factorial(i)))
