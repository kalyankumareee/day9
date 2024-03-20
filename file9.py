1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# 2.)Find the uncommon words from 2 strings
# # s1 = "Hello how are you"
# s2 = "Hello how is"
s1 = "Hello how are you"
s2 = "Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
if val not in s2:
print(val)
for val in s2:
if val not in s1:
print(val)
'''
# 3.)Wrire a code print the 8th fibanochi number
#0,1,2,3,4,5,8
num=8
n1=0
n2=1
for val in range(num):
ans=n1+n2
n1=n2
n2=ans
print(ans)
#constructors
#eg:2
#unparametarised constructor
class profile:
def __init__ (self):
print("hello world")
obj =profile()
obj.__init__()
#eg:3
#parameter constructor
class profile:
def __init__(self,id,name,age):
print(id,name,age)
obj=profile(1,"sid",29)
'''
a=5
b=3
c=a**b
print(c)
if a > b:
print("a is greater than b")
x=4
if 3 < x < 5:
print("x is between 3 and 5")
if a != True:
print("a is not True")
# ! Eg:2
class c1:
def __init__(self):
print("Iam constructor from parent class")
class child1(c1):
pass
obj = child1()
#multilevel inheritance
eg:1
class voice:
def sound(self):
print("All the animals have their own voices")
class dog(voice):
def dog_voice(self):
print("bark")
class cat(dog):
def cat_voice(self):
print("meow")
class parrot(cat):
def parrot_voice(self):
print("speak")
all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
class honda_city:
def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
print(cc, Hp, torque, fuel_type, num_of_piston)
def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
print(cc, Hp, torque, fuel_type, num_of_piston)
class amaze(honda_city):
def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
print(cc, Hp, torque, fuel_type, num_of_piston)
def amaze_body_specs(self, color, weight, height, length):
print(cc, Hp, torque, fuel_type, num_of_piston)
# Multiple Inheritance
#? It has multiple parent and 1 child
class while_pertol:
def function_w(self):
print("used to Airplans")
class Organic_petrol:
def function_o(self):
print("used for Bike, cars")
class premium_petrol:
def function_p(self):
print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
def defanition(self):
print("Petrols types")
       
        































    

