from prime import is_prime

def palindrome_primes():
    output = []
    for i in range(10000,100000):
        if is_prime(i):
            if(str(i) == str(i)[::-1]): 
                output.append(i)
    return output
    
print(palindrome_primes())
 

   
    
    


