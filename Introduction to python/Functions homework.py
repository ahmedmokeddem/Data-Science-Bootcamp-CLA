def is_palindrom(s):
    return s.replace(" ","")=="".join(reversed(s)).replace(" ","")
def is_prime(num):
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               return False
        return True
    else: return False
def is_InRange(num,a=20,b=30):
    return num in range(a,b)
def fact(n):
    if n>0: return n*fact(n-1)
    else: return 1
def reverse(s):
    return s[::-1]
def sum_num(liste):
    s=0
    for elem in liste:s+=elem
    return s
def max(x,y,z):
    if x>=y and x>=z: return x
    elif y>=x and y>=z: return z
    else: return z
