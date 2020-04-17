
import time
from math import sqrt
def is_prime(n):
    assert n>0
    for factor in range(2, int(sqrt(n))+1):
        if n%factor == 0:
            return False
    return True if n !=1 else False

def main_write():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('error while writing files')
    finally:
        for fs in fs_list:
            fs.close()
    print('Done!')

def main_read():

    with open('file.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    
    with open('file.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('file.txt') as f:
        lines = f.readlines()
    print(lines)



def main_bin():
    # 二进制文件
    try:
        with open('1.bmp', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('2.bmp', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('file not found')
    except IOError as e:
        print('error while reading')
    print('end process')

import json

def main():
    # JSON
    mydict = {
        'name' : 'ryan',
        'age' : 28,
        'qq' : 30939,
        'friends' : ['dachui', 'yuanfang'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('finish save data')

# API调用
import requests

def main_api():
    api_website = 'www.api.com'
    resp = requests.get(api_website+'?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == '__main__':
    main()