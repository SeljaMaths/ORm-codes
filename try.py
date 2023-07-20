# import mysql.connector
#
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   database="customer_data",
#   password=""
# )
#
# print(mydb)
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE customer_data")

# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# a = [1, 6, 4]
# c = 0
# for i in a:
#     c += 1
# print(c)

a = input("Enter : ")
b = a[::-1]
m = int(len(a)/2)
n = len(a)
s = a[:m]
e = a[m:]
f = e[::-1]
if a == b and e == f:
    print("given string is palindrome and symmetrical")
elif a == b:
    print("given string is palindrome")
else:
    print("given string is not polindrome and symmetrical")


