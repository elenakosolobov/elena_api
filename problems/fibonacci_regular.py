def fib(n):
    l = [0]
    a, b = 0, 1
    for i in xrange(n):
        l.append(b)
        a,b = b, a+b
    # while b <= n:
    #     l.append(b)
    #     a,b = b, a+b

    return l

print fib(8)