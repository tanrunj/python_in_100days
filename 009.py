class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing flying chess.' % self._name)
        else:
            print('%s is playing poker.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s is watching av.' % self._name)
        else:
            print('%s is only can watch catoon.' %self._name)

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s is learning %s.' %(self._grade, self._name, course))

class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s is teaching %s.' %(self._name, self._title, course))


from math import sqrt 

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a+b>c and b+c>a and a+c>b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half-self._a)*(half-self._b)*(half-self._c))

from time import time, localtime, sleep

class Clock(object):
    
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
            (self._hour, self._minute, self._second)


from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: wang wang wang...' %self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: miao miao miao...' %self._nickname)

    


# Study Case 1 : Ultraman Vs Monster

from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp>=0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass

class Ultraman(Fighter):

    __slots__ =('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        injury = randint(25,35)
        other.hp -= injury
        return injury

    def huge_attack(self, other):
        if self._mp >=50:
            self._mp -= 50
            injury = other.hp *3//4
            injury = injury if injury >=50 else 50
            other.hp -= injury
            print('造成了%d点伤害.' %injury, end='')
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >=20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    injury = randint(20,25)
                    temp.hp -= injury
                    print('对%s造成了%d点伤害.' %(temp.name, injury), end='')
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(10, 30)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s Ultraman ~~~\n' %self._name +\
            'hp: %d\n' % self._hp +\
            'mp: %d\n' %self._mp


class Monster(Fighter):

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        injury = randint(10, 20)
        other.hp -= injury
        return injury

    def __str__(self):
        return '~~~%s Monster ~~~\n' %self._name +\
            'hp: %d\n' %self._hp

def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main_study1():
     # Study Case 1 : Ultraman Vs Monsters
    u = Ultraman('Ryan', 200, 120)
    m1 = Monster('Sally', 200)
    m2 = Monster('Curry', 150)
    m3 = Monster('Tommy', 100)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('\n=====第%02d回合=====\n' %fight_round)
        m = select_alive_one(ms)
        skill = randint(1,10)
        if skill<=6:
            print('%s使用普通攻击打%s,造成了%d点伤害. ' %(u.name, m.name, u.attack(m)))
            
            print('%s的魔法值恢复了%d点.' %(u.name, u.resume()))
        elif skill<=9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' %u.name)
            else:
                print('%s使用魔法失败，该回合作废.' %u.name)
        else:
            if u.huge_attack(m):
                print('%s使用必杀技打了%s.' %(u.name, m.name))
            else:
                print('必杀技失败：%s使用普通攻击打了%s.' %(u.name, m.name))
                print('%s魔法值回复了%d点.' %(u.name, u.resume()))

        if m.alive > 0:
            print('%s 回击了　%s. 造成了%d点伤害' %(m.name, u.name, m.attack(u)))
        display_info(u, ms)
        fight_round +=1
    print('\n==========战斗结束==========\n')
    if u.alive >0:
        print('%s Ultraman wins!' %u.name)
    else:
        print('Monsters win!')

def main_practice():
   
    # Practice 1 : property
    person = Person('王大锤', 12)
    person.play()
    person._gender = 'male'

    # Practice 2 : Static Method
    # a, b, c = 3, 4, 5
    # if Triangle.is_valid(a, b, c):
    #     t = Triangle(a, b, c)
    #     print(t.perimeter())
    #     print(t.area())
    # else:
    #     print('cant make a triangle')

    # Practice 3 : Clock Class Method
    # clock = Clock.now()
    # while True:
    #     print(clock.show())
    #     sleep(1)
    #     clock.run()

    # Practice 4 : Inheritance
    # stu = Student('王大锤', 15, '初三')
    # stu.study('Math')
    # stu.watch_av()

    # t = Teacher('罗浩', 38, '砖家')
    # t.teach('python programing')
    # t.watch_av()

    # Practice 5 : Virtual Inheritance, abstractmethod
    # pets = [Dog('money'), Cat('catty'), Dog('Yellow')]
    # for pet in pets:
    #     pet.make_voice()

# Study Case 2　: Poker Game

import random

class Card(object):

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' %(self._suite, face_str)
    
    def __repr__(self):
        return self.__str__()

class Poker(object):

    def __init__(self):
        self._cards = [Card(suite, face)
            for suite in '♠♥♣♦' for face in range(1,14)
        ]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._current < len(self._cards)

class Player(object):

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        self._cards_on_hand.sort(key=card_key)

def get_key(card):
    return (card.suite, card.face)


def main_study2():
    p = Poker()
    p.shuffle()
    players =[Player('Ryan'), Player('Sally'), Player('Curry'), Player('Tommy')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
        
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)



# Study Case 3 : Salary System

class Employee(object, metaclass = ABCMeta):
    
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    
    def __init__(self, name, working_hour = 0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour>0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):
    
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self.sales
    
    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales>0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('boss 1'), Programmer('Ryan'),
        Manager('boss 2'), Salesman('Sally'),
        Salesman('Curry')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('%s working hours in this month:' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('%s sales amount in this month:' % emp.name))

        print('%s salary is : %s.' %(emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()