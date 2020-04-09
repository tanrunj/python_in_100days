# # Practice 1: Prime number
# from math import sqrt

# num = int(input('input an positive integer:'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end+1):
#     if num % x == 0:
#         is_prime = False
#         break

# if is_prime and num!=1:
#     print('%d is prime number' %num)
# else:
#     print('%d is not prime number' %num)


# # Practice 2: Biggest common divisor    SCM: Smallest common Multiple
# x = int(input('x= '))
# y = int(input('y= '))

# if x >y:
#     x,y = y,x

# for factor in range(x,0,-1):
#     if x %factor==0 and y%factor==0:
#         print('%d and %d with BCD is %d' %(x,y,factor))
#         print('%d and %d with SCM is %d' %(x,y, x*y//factor))
#         break

# Practice 3: Draw Triangle

row = int(input('input rows number:'))
for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row-i-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()

for i in range(row):
    for _ in range(row-i-1):
        print(' ', end='')
    for _ in range(2*i-1):
        print('*', end='')
    print()