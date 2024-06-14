import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n%i==0:
            return False
    return True
def plalindrome_prime(number):
    for i in range(0,number):
        if is_prime(i)==True and str(i)==str(i)[::-1]:
            print(i,end=' ')

positive_int = int(input())
plalindrome_prime(positive_int)