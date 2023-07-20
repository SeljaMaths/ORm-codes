class customer:
    def __init__(self,name,memebership_type):
        self.name =name
        self.memebership_type = memebership_type
        # print ( f'{self.name} got {self.memebership_type} medal')

    def  __str__(self):
        return f'{self.name} got {self.memebership_type} medal'
    #
    # def print_all_customers(customers):
    #     for cust in customers:
    #         print(cust)
    def __eq__ (self,other):
        if self.name == other.name and self.memebership_type == other.memebership_type:
            return True
        return False


    #
    # __hash__ = None
    #
    # __repr__ = __str__


customers = [customer('selja','gold'),customer('rajau','bronze')]
# # for i in customers:
# #     print(i)
# # print(customers[1])
#
# customer.print_all_customers(customers)

print(customers[0]==customers[1])
print(customers)



'''
def welcome():
    print('welcome to krish naik')

welcome()
wel = welcome()
wel
'''


'''def welcome():
    return 'welcome to krish naik'

wel = welcome()
print(wel)
del welcome
# welcome()
wel'''


'''def main_welcome(msg):
    def sub_welcome_class():
        print('welcome to krish naik youtube channel')
        print(msg)
        print('please subscribe')
    return sub_welcome_class()
main_welcome('krish')'''

'''def main_welcome(func):
    def sub_welcome_class():
        print('welcome to krish naik youtube channel')
        print(func('hi hello'))
        print('please subscribe')
    return sub_welcome_class()
main_welcome(len)'''

'''

def main_welcome(func):
    def sub_welcome_class():
        print('welcome to krish naik youtube channel')
        func()
        print('please subscribe')
    return sub_welcome_class()

def channel_name():
    print('this is a ')

main_welcome(channel_name)'''


'''def main_welcome(func):
    def sub_welcome_class():
        print('welcome to krish naik youtube channel')
        func()
        print('please subscribe')
    return sub_welcome_class()
@ main_welcome
def channel_name():
    print('this is a ')
'''

'''
class car:
    base_price = 10000
    def __init__(self,winodws,doors,powers):
        self.winodws=winodws
        self.doors=doors
        self.powers=powers

    def what_base_price(self):
        print('the base price is{}'. format(self.base_price))
car1 =car(2,5,300)
print(car1.base_price)'''



''''''''