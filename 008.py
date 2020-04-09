class Student(object):
    # __init__ is construct function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is studying %s.' %(self.name, course_name))

    # PEP 8 naming criterion
    def watch_movie(self):
        if self.age < 18:
            print('%s can only watch cartoon.' % self.name)
        else:
            print('%s can watch loving action movie.' % self.name)

def main1():
    stu1 = Student('ryan', 28)
    stu1.study('<python language>')
    stu1.watch_movie()

    print()
    stu2 = Student('sally', 15)
    stu2.study('<how to be adult>')
    stu2.watch_movie()

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main2():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test._Test__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test._Test__foo)


#Practice 1: Digital Clock Class
from time import sleep

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

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
        return '%02d:%02d:%02d' %(self._hour,self._minute,self._second)

def main3():
    clock = Clock(23,59,58)
    while(True):
        print(clock.show())
        sleep(1)
        clock.run()


# Practice 2: Distance between points
from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s , %s)' %(str(self.x),str(self.y))


def main():
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()