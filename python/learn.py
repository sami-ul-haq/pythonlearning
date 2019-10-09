# 50
# While Loop Practice
# i= 1
# while i<=10:
#     print(f"Sami ul Haq {i}")
#     i = i + 1

#51
# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i += 1

# print(total)

# n= input("Enter Number: ")
# total = 0
# i = 0
# while i < len(n):
#     total += int(n[i])
#     i += 1
# print(total)

# # class 56
# name = input("Enter Your Name: ")
# temp = ""
# i = 0
# while i < len(name):
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i += 1

# while True:
#     print("Sami ul Haq")

# total = 0
# for i in range(1,11):
#     total += i

# print(total)

# num = input("Enter Number: ")
# total = 0
# for i in range(0 , len(num)):
#     total += int(num[i])

# print(total)

# name = input("Enter Name: ")
# # temp =""
# for i in range(0 , len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#         temp += name[i]

# name = input("Enter Name: ")
# i = 0
# while i < len(name):
#     print(name.count(name[i]))
#     i += 1

# num = int(input("Enter Number: "))
# win_num = 50
# guess = 1
# game_over = False
# while not game_over:
#     if num == win_num:
#         print(f"You Won & You Guessed In {guess} Times")
#         game_over = True
#     else:
#         if num < win_num:
#             print("Too Low")
#         else:
#             print("Too High!")
#     guess += 1
#     num = int(input("Enter Again: "))    

# for i in range(10 , 0 , -1):
#     print(i)  

# name = "Sami ul Haq"
# for i in range(len(name)):
#     print(name[i])

# name ="Sami ul HAq"
# for i in name:
#     print(i)

# def add_two(a,b):
#     if a > b :
#         return a
#     else:
#         return b

# a = input("Enter NUmber 1 : ")
# b = input("Enter NUmber 2 : ")
# total = add_two(a,b)
# print(f"{total} is Bigger")

# fruits = ["Sami","ul","Haq"]
# print(" " .join(fruits))

# cat = input("Enter Name: ")

# if cat == "miawon" :
#     print("WOW")
# if cat != "miawon" :
#     print("NOT WOW")

# fruit = ["Apple", "Banana", "Orange", "Kivi", "Grapes"]

# for i in fruit:
#     print(i)

# i = 0
# while i < len(fruit):
#     print(fruit[i])
#     i += 1

# fruit1 = ["Apple", "Banana", "Orange", "Kivi", "Grapes"]

# fruit2 = ["aam", "kela", "seeb"]

# fruit1.extend(fruit2)

# print(fruit1)

# numbers = [[1,2,3],[4,5,6],[7,8,9]]

# for i in numbers:
#     for sublist in i:
#         print(sublist)

# s = "Sami"
# m = 24

# print(type(s))
# print(type(m))

# numbers = list(range(1,11))
# numdel = numbers.pop()
# num = numbers + numdel
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square
# print(square_list(num))

# def rev_list(l):
#     r_list = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         r_list.append(popped_item)
#     return r_list

# print(rev_list(num))

# name = "sami"
# weight = 34
# weight = weight + 21
# print(f"My Name Is {name} ANd My Weight Is {weight}")


# mylist = ["abc" , "def" , "ghi"]

# def re_list(l):
#     mylist = []
#     for i in l:
#         mylist.append(i[::-1])
#     return mylist


# print(re_list(mylist))

# num_list = [ 1, 2, 3, 4, 5, 6, 7, 8]

# def even_odd(l):
#     e_list = []
#     o_list = []
#     for i in l:
#         if i % 2 == 0:
#             e_list.append(i)
#         else:
#             o_list.append(i)
#     output = [e_list,o_list]
#     return output

# print(even_odd(num_list))

# list1 = [1,2,3,4,5,6]
# list2 = [1,3,5,7,8,9]

# def two_list(l1, l2):
#     com_list = []
#     for i in l1:
#         if i in l2:
#             com_list.append(i)
#     return com_list
# print(two_list(list1,list2))

# mylist = [1,2,3 , [4,5,6] , [7,8,9]]

# def li_count(l):
#     count = 0
#     for i in l:
#         if type(i) == list :
#             count += 1
#     return count

# print(li_count(mylist))

# TUPLES

# mixed = ( 1, 2, 3, 4, 5)
# for i in mixed:
#     print(i, end=" ")

# num = (1)
# print(type(num))

# mixed[5].pop()
# print(mixed)

# print(sum(mixed))

# def func(int1 , int2):
#     add = int1 + int2
#     multi = int1*int2
#     return add , multi

# add, multi = func(2,3)
# print(add)
# print(multi)

# num = 300
# num += 200
# print(num)

# a = (12*2)/4+1
# print(a)

# name = "Sami ul Haq"
# age = 34
# print(f"My Name Is {name} And My Age IS {age}")
# print("My Name Is " + name + " And My Age Is " + str(age))

# name , age = input("Input Name And Age ").split(" ")

# print(f"My Name Is {name} & My Age {age}")

# mixed = (2,3,4,5,6,7)
# print(min(mixed))

# def fucn(num1,num2):
#     add = num1 + num2
#     multi = num1*num2
#     return add , multi

# add, multi = fucn(2,9)
# print(add)

# nums = list(range(1,10))
# print(nums)

# nums1 = tuple(range(1,18))
# print(nums1)

# intro to dictionaries 
 
# user = {"Name" : "Sami ul Haq" , "Age" : 24 }
# print(user)
# print(type(user))

# user = dict(name="Sami ul Haq" , age=23)
# print(user["name"])

# user = {}
# user["name"] = "Sami ul Haq"
# user["age"] = 24

# print(user)

# user_info = {
#     'name' : 'Sami ul Haq' ,
#     'age' : 24 ,
#     'fav_mov' : ['Robot' , 'Fantom']
# }

# if 24 in user_info.values():
#     print("Yes")
# else:
#     print("No")

# for i in user_info.values():
#     print(i)

# user_values = user_info.values()
# print(user_values)

# user_info = {
#     "name" : "sami",
#     "age" : 24,
#     "fav" : [1,2,3,4],
#     "mov" : ["robot" , "salam"]

# }

# for i, j in user_info.items():
#     print(f"Key Is {i} & Value is {j}" )

# info = {}
# info["name"] = "Sami ul Haq"
# info["age"] = 24

# wah = info.popitem()
# print(wah)

# user_info = {
#     "name" : "Sami ul Haq" ,
#     "age" : 24
#     "country" : "pakistan" ,
#     "State" : "Sindh"
# }

# more_info = {
#     "country" : "pakistan" ,
#     "State" : "Sindh"
# }

# user_info.update(more_info)
# print(user_info)

# d = dict.fromkeys(range(1,11) , "unknown")
# print(d)
# di = user_info.copy()
# print(di)

# if user_info.get("names"):
#     print("Present")
# else:
#     print("Not Present")

# user_info = {
#     "name" : "Sami ul Haq" ,
#     "age" : 24 ,
#     "country" : "pakistan" ,
#     "State" : "Sindh"
# }

# print(user_info.get("namea","Not Found"))



# def cube_find(n):
#     cubes = {}
#     for i in range(1,n+1):
#         cubes[i] = i**3
#     return cubes

# print(cube_find(10))

# def word_counter(s):
#     count = {}
#     for i in (s):
#         count[i] = s.count(i)
#     return count
# print(word_counter("SamiulHaq"))


# user_info = {}
# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# fav_movie = input("Your FAv Movies: ").split(",")
# fav_songs = input("Your FAv Songs: ").split(",")

# user_info["Name"] = name
# user_info["Age"] = age
# user_info["Fave_Movies"] = fav_movie
# user_info["Fav_Songs"] = fav_songs

# for key,value in user_info.items():
#     print(f"{key} : {value} ")

# s2 = {1,2,3,3,4,5,56,6,6,6}
# s2.add(34)
# s2.remove(1)
# print(s2)

# s1 = {1,2,3,4,5,5,5}
# s2 = {2,3,4,5,6,7}
# union = s1 | s2
# inter = s1 & s2
# print(union)
# print(inter)

# square = []
# for i in range(1,11):
#     square.append(i**2)

# print(square)

# square1 = [i**2 for i in range(1,11)]
# print(square1)
# negative = [-i for i in range(1,11)]
# print(negative)

# new_list = []
# names = ["Sami" , "Haq" , "Gilgit"]
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# def rev_str(l):
#     return [name[::-1] for name in l]

# print(rev_str(["sami","junaid","huzaifa"]))

# OOP Learnings

# class Student():
#     def __init__(self,f_name,m_name,l_name,age):
#         self.f_name = f_name
#         self.m_name = m_name
#         self.l_name = l_name
#         self.age = age

# info = Student("Sami" , "ul" , "Haq" , 19)

# print(info.f_name)
# print(info.m_name)
# print(info.l_name)

# # def reverselist(l):
#     return [name[::-1] for name in l]

# print(reverselist(["sami" , "ul" , "Haq"]))

# numbers = list(range(1,11))

# nums = [i for i in numbers if i%2==0]

# print(nums)

# mylist = [True , False , [1,2,3] , 1 , 1.0 , 3 ]

# def numtostr(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]

# print(numtostr(mylist))

# nums = [1,2,3,4,5,6,7,8,9,10]

# new_list = []
# for i in nums:
#     if i%2 == 0 :
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

# new_list2 = [i*2 if (i%2 == 0) else (-i) for i in nums]
# print(new_list2)

# new_list = [[i for i in range(0,4)] for j in range(3)]
# print(new_list)

# square = { f"Square Of {i} is ":i**2 for i in range(1,11)}
# for k,v in square.items():
#     print(f" {k} : {v}")

# name = "Sami ul Haq"
# word_counter = {char:name.count(char) for char in name}
# print(word_counter)

# even_odd = { i : ("Even " if i%2 == 0 else "Odd") for i in range(1,11)  }
# for k,v in even_odd.items():
#     print(f"{k} : {v}" )

# num = int(input("Enter Number: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# def total(*args):
#     return args

# print(total(1,2,3,4,5,6))

# class Person:
#     def __init__(self,firstname,lastname,age,gender):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.gender = gender
    
# p1 = Person("Sami", "Haq" , 18 , "Male")
# print(p1.firstname)

# class Laptop:
#     def __init__(self, name , Model_name , price):
#         self.name = name
#         self.Model_name = Model_name
#         self.price = price
#         self.complete = name + " " + Model_name

# lap1 = Laptop("Dell" , "Logistic" , 32000)
# lap2 = Laptop("HP" , "EliteBook" , 35000)
# print(lap2.complete)

# l = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# list.append(l2 , 2)
# print(l2)


# class Laptop:
#     def __init__(self, name , Model_name , price):
#         self.name = name
#         self.Model_name = Model_name
#         self.price = price
#     def disc(self,num):
#         off_prize = (num/100)*self.price
#         return self.price - off_prize

# st = Laptop("HP" , "Elitebook" , 35000)
# print(st.disc(10))

# def multi(num , *args):
#     multiply = 1
#     print(num)
#     print(args)
#     for i in args:
#         multiply *= i
#     return multiply
# print(multi(2))

# def multi(*args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply
# num = (1,2,3,45)
# print(multi(num))

# def my(num , *args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "Beta Kiya Ker Rahe Ho"

# nums = [2,3,4,5,6]
# print(my(4, *nums))


# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
# dic = {"name" : "Sami" ,"age " : 23}
# print(func(**dic))

# add2 = lambda a,b : a+b
# mul2 = lambda a,b : a*b
# print(add2(2,3))
# print(mul2(2,3))
 

# gg = lambda s : True if len(s) > 2 else False
# print(gg("SamiulHaq")) 


# class Laptop():
#     def __init__(self, name , brand , price):
#         self.name = name
#         self.brand = brand
#         self.price = price
#         self.laptop_name = name + " " + brand 

#     def apply_dis(self,num):
#         off = (num/100)*self.price
#         return self.price - off


# ob = Laptop("Hp" , "EliteBook" , 33000)
# print(ob.name)
# print(ob.laptop_name)
# print(ob.price)
# print(ob.apply_dis(50))

# class Laptop():
#     discount = 10
#     def __init__(self, name , brand , price):
#         self.name = name
#         self.brand = brand
#         self.price = price
#         self.laptop_name = name + " " + brand 

#     def apply_dis(self):
#         off = (self.discount/100)*self.price
#         return self.price - off


# ob = Laptop("Hp" , "EliteBook" , 33000)
# print(ob.apply_dis())

# print(ob.__dict__)


# class Person():
#     countint = 0
#     def __init__(self,f_name , l_name , age , gender):
#         Person.countint += 1
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
#         self.gender = gender

# p1 = Person("Sami" ,"Haq" , 18 , "Male")
# p14 = Person("Sami" ,"Haq" , 18 , "Male")

# p4 = Person("Sami" ,"Haq" , 18 , "Male")

# p33 = Person("Sami" ,"Haq" , 18 , "Male")

# p3 = Person("Sami" ,"Haq" , 18 , "Male")

# print(Person.countint)



# # add2 = lambda a,b : a+b

# # print(add2(2,3))

# # iseven = lambda a:a%2==0

# # print(iseven(6))


# # func = lambda s : Ture if len(s) > 4 else False


# # Without Enumerate Function

# names = ["sami" , "khalid" , "Wase" , "usma"]
# # pos = 0
# # for name in names:
    
# #     print(f"{pos} : {name}")
# #     pos += 1

# # print(names)

# #With Enumerate
# def find_pos(l,target):
#     for pos,name in enumerate(l):
#         if name == target:
#             return pos
#     return -1

# print(find_pos(names, "sami"))


# names = ["abc" , "abcd" , "abcde" ]
# length = list(map(len , names))
# print(length)

# func = lambda s : True if len(s) > 5 else False

# print(func("Samiulhaq"))
# name = ["abc" , "abcd" , "abcde" ]
# for pos,name in enumerate(name):
#     print(f"{pos}----> {name`}")

# num = [1,2,3,4,5]

# square = list(map(lambda a:a**2,num))
# print(square)

# even = []
# for i in numbers:
#     if i%2==0:
#         even.append(i)

# print(even)
# numbers = [3,4,2,1,5,6,9,8,10]
# def is_even(a):
#     return a%2==0
# even = list(filter(is_even,numbers))
# print(even)

# for i in even:
#     print(i)

# user_id = ["user1","user2","user3","user4"]
# names = ["Sami","Khalid","Hassan","Nisar"]
# combo = dict(zip(user_id,names))
# print(combo)

# l = [(1,2),(3,4),(5,6),(7,8)]
# l1,l2 =list(zip(*l))
# print(l1)
# print(l2)
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# zipped = tuple(zip(l1,l2))
# print(zipped)

# def avg_fin(*arg):
#     ave = []
#     for pair in zip(*arg):
#         ave.append(sum(pair)//len(pair))
#     return ave

# print(avg_fin([1,2,3],[4,5,6],[7,8,9]))

# def my_sum(*args):
#     if all([(type(arg)==int or type(arg)==float) for arg in args]):
#         total = 0
#         for num in args:
#             total += num
#         return total
#     else:
#         return "Wrong Info"
# print(my_sum(1,2,3,4,5,6,7 , "Sami"))

# names = ["Sami" ,"Khalid" ,"Junaidi","Mesam"]
# def func(item):
#     return len(item)
# print(max(names , key= func))

# names = ["Sami" ,"Khalid" ,"Junaidi","Mesam"]
# print(min(names , key= lambda item: len(item)))

# cars = [
#     {"Model":"Carolla" , "Price":640000},
#     {"Model":"Caroll" , "Price":740000},
#     {"Model":"Caroa" , "Price":840000},
#     {"Model":"Carla" , "Price":940000}
# ]

# print(sorted(cars, key= lambda item : item["Price"], reverse=True))

# print(sum.__doc__)

# l = [1,2,3,4,5,6]

# def my_func(func,l):
#     mylist = []
#     for item in l:
#         mylist.append(func(item))
#     return mylist

# print(my_func(lambda a : a**3 , l))

# def outer():
#     def inner():
#         print("This Is Inner Function")
#     return inner
# var = outer()
# var()

def to_power(power):
    def calc_power(number):
        return number**power
    return calc_power
ans = to_power(3)
print(ans(2))