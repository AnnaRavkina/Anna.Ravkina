from prime import is_prime

def primes_below(n):
    output = []
    for i in range(2, n):
         if is_prime(i):  
             output.append(i)
    return output
 
print(primes_below(1234))
