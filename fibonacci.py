def big_fibonacci(n):
    a = 1
    b = 1
    c = 2

    if n == 1:
        print(1)
        return
    
    
    while(len(str(c)) != n):
        c = a + b
        a = b
        b = c 
    print (c)

big_fibonacci(20) 