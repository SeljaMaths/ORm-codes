from datetime import date as dt
class Employee:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   # @staticmethod
   # def isAdult(age):
   #    if age > 18:
   #
   #       return True
   #    else:
   #       return False
   def age (self,age1):
      if age1 > 18:
         return True
      else:
         return False

   @classmethod
   def emp_from_year(cls, name, year):
      return cls(name, dt.today().year - year)
   def __str__(self):
      return 'Employee Name: {} and Age: {}'.format(self.name, self.age)
e1 = Employee('Dhiman', 25)
print(e1)
e2 = Employee.emp_from_year('Subhas', 1987)
print(e2)
print(Employee.isAdult(25))
print(Employee.isAdult(16))









# class car:
#     base_price = 100000
#     base_price1 = 100000
#
#     def __init__(self,winodws,doors,powers):
#         self.winodws=winodws
#         self.doors=doors
#         self.powers=powers
#
#     def what_base_price(self):
#         print('the base price is{}'. format(self.base_price))
#
#     @classmethod
#     def revise_base_class(cls, inflation):
#         cls.base_price = cls.base_price+cls.base_price*inflation
#
#     @classmethod
#     def revise_base_class1(cls, inflation):
#         cls.base_price1 = cls.base_price1 + cls.base_price1 * inflation
#
#
# x = car.revise_base_class(0.10)
# y = car.revise_base_class1(0.20)
# print(car.base_price)
# print(car.base_price1)
#














# def main_welcome(func):
#     def sub_welcome_class():
#         print('welcome to krish naik youtube channel')
#         func()
#         print('please subscribe')
#     return sub_welcome_class()
# @ main_welcome
# def channel_name():
#     print('this is a ')


# def main_welcome(func):
#     def sub_welcome_class():
#         print('welcome to krish naik youtube channel')
#         func()
#         print('please subscribe')
#     return sub_welcome_class()
#
# def channel_name():
#     print('this is a ')
#
# main_welcome(channel_name)
# class car:
#     base_price = 10000
#     def __init__(self,winodws,doors,powers):
#         self.winodws=winodws
#         self.doors=doors
#         self.powers=powers
#
#     def what_base_price(self):
#         print(f'the base price is {self.base_price}')
# car1 =car(2,5,300)
# print(car1.base_price)
# car1.what_base_price()

