
# Generator Function
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a

# def main():
#     for val in fib(20):
#         print(val)

# Practice 1 : Marquee
import os
import time
def main():
    content ='北京欢迎你'
    while True:
        os.system('clear')
        print(content)

        time.sleep(0.2)
        content = content[1:] + content[0]

# Practice 2: Verify Code
import random
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) -1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

# Practice 3: postfix name of files
def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0< pos < len(filename)-1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

# Practice 4: two biggest num in a list
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else(x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2

# Practice 5: the exact day of the year
def is_leap_year(year):
    return year%4==0 and year%100!=0 or year%400==0

def which_day(year, month, day):
    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ]
    total = 0
    for index in range(month-1):
        total += days_of_month[is_leap_year(year)][index]
    return total + day

# Practice 6: Pascal's triangle
def pascal_triangle(num):
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end='\t')
        print()
    
# Practice 7: Union Lotto
from random import randrange, randint, sample

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls)-1:
            print('|', end=' ')
        print('%02d' %ball, end=' ')
    print()

def random_select():
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

# Practice 8: Joseph Circle
def joseph_circle():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

# Practice 9: # gaming
import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

# Future work: check input validity and add winning rules
def gaming():
    init_board= {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('it\'s %s turn, please input the location:' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('another game?(yes|no)')
        begin = choice == 'yes'



if __name__ == '__main__':
    # print(get_suffix('img.jpg', has_dot=True))
    
    # print(max2([1,2,3,4,55,3]))
    
    # print(which_day(1980,11,28))
    
    # pascal_triangle(5)

    # n = int(input('times for beting:'))
    # for _ in range(n):
    #     display(random_select())
    
    # joseph_circle()

    gaming()