def nfibonacci(n):
    if n == 1:
        return [1]
    elif n <= 0:
        return []
    else:
        fib = [1,1]

        for x in range(n-2):
            fib.append(fib[x] + fib[x+1])
        return fib

n = int(input("Number: "))

for num in nfibonacci(n):
    print(num)
