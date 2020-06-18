##fib1.py

def fib(n):
    
    prev = 1
    nxt = 1

    for i in range(2, n):

        res = prev + nxt
        prev, nxt = nxt, res
    return nxt


def fib1(n):
    #create a while loop
    pass

def fib2(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def main(n):

    print('fib', fib(500000))
    #print('fib1 '+'you should create yourself')
    print('fib2', fib(500000))

if __name__ == '__main__':
    main(8)
