 

import re

 #　验证ＱＱ号, match
def main1():
    username = input('input username:')
    qq = input('input qq number:')

    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username) # 不带转义
    if not m1:
        print('plz input valid username.')
    
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('plz input valid qq number.')

    if m1 and m2:
        print('valid username and qq')

# 手机号　compile, findall, finditer, group, search
def main2():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事说8130123456789遍，我的手机号是135123456789这个靓号，
    不是15600998765，也是110或119，王大锤的手机才是15600998765。
    '''

    mylist = re.findall(pattern, sentence)
    print(mylist)
    for temp in pattern.finditer(sentence):
        print(temp.group())
    
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

# 和谐
def main3():
    sentence = '你丫是傻叉吗？我操你大爷的。Fuck you.'
    purified = re.sub('[操艹]|fuck|shit|傻[比逼叉缺吊]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)

# 分句
def main():
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    main()