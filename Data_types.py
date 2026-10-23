x = 10 #int
y = 10.145 #float
z = "Hello" #str
print(type(x))
print(type(y))
print(type(z))

a = ["apple","banana","Orange","Grapes"] #list
print(type(a))

b = ("1","2","3","4") #tuple
c = ("Pink","Green","Blue","Red")
print(type(b))
print(type(c))

d = {"Hero","Yamaha","Suzuki","Bmw"} #set
print(type(d))

#making list
e = range(20)

print(list(e))

#dict
f = {"Name": "Ranvijay","Age":25}
print(f["Name"])
print(f["Age"])
print(type(f))

#bool
g = True
print(type(g))




num1 = int(input("Enter Your first number "))
num2 = int(input("Enter your srcond nu mumber"))

sum = num1 + num2
print("Sum of num1 & num2 is :-",sum)


numm =int(input("Enter yor number"))

if numm % 2== 0:
    print("The number is even")
else:
    print("The number is odd")


#Comparision

n1 = int(input"Enter Your Number : "))
n2 = int(input("Enter your Seconf Number : "))

if n1 > n2:
    print("The n1 is Greater then the number of n2")
else:
    print("The n2 is Greater theb the number of n1")


#positive and negative

num = int(input("Enter any Number : "))
   if num > 0:
       print("The Number is positive")
   elif num < 0:
       print("The number is Negative")
   else:
       print("The Number is Zero")