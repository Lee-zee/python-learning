# class Student(object):
#     # 用来限制给实例添加的属性,只有tuple中的属性可以被添加到实例上
#     __slots__ = ('name', 'age', '__gender', '__birth')
#
#     def __init__(self, name, gender):
#         self.__birth = None
#         self.name = name
#         self.__gender = gender
#
#     # 对一个类属性,同时定义get,set方法,还有属性本身,很繁琐,可以使用property构造器自动创建getter,setter
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         self.__gender = gender
#
#     @property
#     def birth(self):
#         return self.__birth
#
#     @birth.setter
#     def birth(self, value):
#         self.__birth = value
#
#     @property
#     def age(self):
#         return 2023 - self.__birth
#
#
# class Animal(object):
#     @staticmethod
#     def run():
#         print('Animal is running')
#
#
# class Dog(Animal):
#     def run(self):
#         print('dog is running')
#
#     @staticmethod
#     def eat():
#         print('dog is eating')
#
#
# class Cat(Animal):
#     pass
#
#
# dog = Dog()
# dog.run()
#
#
# class Screen(object):
#     __slots__ = ('__width', '__height', '__resolution')
#
#     def __init__(self):
#         self.__height = 0
#         self.__width = 0
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         self.__width = value
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         self.__height = value
#
#     @property
#     def resolution(self):
#         return self.__height * self.__width


# 可迭代的类
# 斐波那契数列类
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __iter__(self):
        return self

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


for item in Fib():
    print(item)

# print(Fib()[3])

# 枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    # Jan = > Month.Jan, 1
