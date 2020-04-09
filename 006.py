
# # Practice 1: Number of combinations C(M,N)

# def fac(num):
#     result = 1
#     for n in range(1, num+1):
#         result *= n
#     return result

# m = int(input('m = '))
# n = int(input('n = '))

# print(fac(m)//fac(n)//fac(m-n))


# Practice 2: functions
def gcd(x,y):
    (x,y) = (y,x) if x>y else (x,y)
    for factor in range(x, 0, -1):
        if x % factor ==0 and y%factor==0:
            return factor

def lcm(x,y):
    return x*y//gcd(x,y)

def is_prime(num):
    for factor in range(2, int(num** 0.5)+1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

def is_palindrome(num):
    temp = num
    total = 0
    while temp >0:
        total = total*10 + temp%10
        temp//= 10
    return total == num

def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200

