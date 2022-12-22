from math import sqrt

# Number to be checked for prime
def isPrime(n):
    if n > 1:
    	for i in range(2, int(n/2)+1):
    		if (n % i) == 0:
    			return False
    		break
    	else:
    		return True
    # If the number is less than 1, its also not a prime number.
    else:
    	return False

def SecondLargestPrime():
    i = 99999999
    found = 0
    while(found != 2):
        if(isPrime(i)):
            found+= 1
        else:
            i -= 1
    return i

def SecondSmallestPrime():
    i = 10000000
    found = 0
    while(found != 2):
        if(isPrime(i)):
            found+= 1
        else:
            i += 1
    return i


    

def findChars(str1):
    n = len(str1)
    SecondSmallestPrime = SecondSmallestPrime()
    SecondLargestPrime = SecondLargestPrime()
    small_pos = (SecondSmallestPrime / n) + 1
    large_pos = (SecondLargestPrime / n) + 1
    print(small_pos, large_pos)
    return small_pos, large_pos
    
    
str1 = "GREYBIANSROCK"

    
# print(SecondLargestPrime())
