# Check Whether A Number Is Prime Or not
import math
from typing import List 
class Prime:
    def isPrime(self, num: int) -> bool:
        i:int = 2
        while i <= int(math.sqrt(num)):
            if num % i == 0:
                return False
            i += 1

        return True
    

    """
    The Sieve of Eratosthenes is an ancient algorithm used to find all 
    prime numbers up to a specified integer. 
    """
    def sieve(self, Nth: int) -> List[int]:
        # Create an array of length Nth
        primes: List[int] = [True] * (Nth + 1)
        primes[0] = False

        p: int = 2

        while p * p <= Nth:
            # If it is a prime number
            # then check all the multiple of this num
            if primes[p]:
                for j in range(p * 2, Nth + 1, p):
                    primes[j] = False
            
            p += 1

        all_primes: List[int] = []
        for i in range(Nth + 1):
            if primes[i]:
                all_primes.append(i)
        
        return all_primes



        
    
if __name__ == "__main__":
    prime = Prime()
    # for i in range(1, 22):
    #     print(str(i) + " -> " + str(prime.isPrime(i)))

    all_primes: List[int] = prime.sieve(40)
    print(all_primes)