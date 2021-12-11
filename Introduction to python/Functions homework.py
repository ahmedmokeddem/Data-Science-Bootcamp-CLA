def is_palindrom(s):
    return s=="".join(reversed(s))
def is_prime(num):
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               return True
        return False
    else: return False
def is_InRange(num,a=20,b=30):
    return num in range(a,b)
def fact(n):
    if n>0: return n*fact(n-1)
    else: return 1
def reverse(s):
    return "".join(reversed(s))
def sum_num(list):
    return sum(element for element in list)
def max(x,y,z):
    if x>=y and x>=z: return x
    elif y>=x and y>=z: return z
    else: return z