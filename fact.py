##fact.py

def fact(num):

    n = num - 1
    while n > 1:
        num = num * n
        n -= 1
    return num

def fact1(num): #5

    for i in range(1, num): #(1,2,3,4)
        num = num * i
    return num

def fact2(num):

    if num == 1:
        return num

    else:
        return num * fact2(num-1)

def main():
    #print('fact is', fact(5))
    #print('fact1 is ' + str(fact1(9999)))
    print('fact2 is', fact2(9999))
    

if __name__ == '__main__':
    main()
