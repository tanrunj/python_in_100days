# # Practise 1: Water Flower Number
# for num in range(100,1000):
#     low = num % 10
#     mid = num//10 %10
#     high = num //100
#     if num == low**3 + mid**3 + high**3:
#         print(num)

# # Practice 2: Reverse Number
# num = int(input('num = '))
# rnum = 0

# while num>0:
#     rnum = rnum *10 + num%10
#     num //= 10
# print(rnum)

# Practice 3: Chicken Money

# for x in range(0,20):
#     for y in range(0,33):
#         z = 100 - x - y
#         if 5*x +3*y + z/3 == 100:
#             print('roosters: %d, hens: %d, chicks: %d' %(x,y,z))

# Practice 4: Craps Gambling
# from random import randint

# money = 1000
# while money > 0:
#     print('your asset are: %d' %money)
#     needs_go_on = False
#     while True:
#         debt = int(input('Plz bet:'))
#         if 0 < debt <= money:
#             break
#     first = randint(1,6) + randint(1,6)
#     print('the player get point %d' % first)
#     if first == 7 or first == 11:
#         print('the player win')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('the banker win')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1,6) + randint(1,6)
#         print('the player get point %d' % current)
#         if current == 7:
#             print('the banker win')
#             money -= debt
#         elif current == first:
#             print('the player win')
#             money += debt
#         else:
#             needs_go_on = True

# print('Game Over, you go bankrupt.')

# Practice 5: Fibbonaci 20 numbers

# fib = [1,1]
# for i in range(1,19):
#     fib.append(fib[i-1]+fib[i])
# print(fib)

# Practice 6: Perfect Number in 10000

# for num in range(1,10000):
#     sum = 0
#     for fac in range(1,num):
#         if num%fac ==0:
#             sum += fac
#     if sum == num:
#         print(' %d' %num, end='')

# Practice 7: Prime Number in 100
import math
for num in range(2, 100):
    if num ==2:
        print('%d ' %num, end='')
        continue
    is_prime = True
    for fac in range(2,int(math.sqrt(num))+1):
        if num%fac ==0:
            is_prime = False
            continue
    if is_prime:
        print('%d ' %num, end='')
print()