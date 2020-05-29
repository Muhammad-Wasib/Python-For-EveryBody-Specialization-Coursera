# Python For Everybody Specilization 5 courses Coursera:

# Getting started with python

# name= input("Enter file: ")
# handle= open(name,'w')
# counts= dict()

# for line in handle:
#    words=line.split()
#    counts[words]=counts.get(word,0)+1
# bigcount=None
# bigword=None
# for word,count in list(counts.items()):
#    if bigcount is None or count > bigcount:
#        bigword=word
#        bigcount=count
# print (bigword,bigcount)

# 1
# name=input("Enter your name: ")
# print('hello',name)

# 2:
# hours=input("Enter hours: ")
# if hours.isdigit():
#    hours = float(hours)
#    rate = 3.50
#    gross_pay = hours * rate
#    print(gross_pay, '$')
# else:
#    print("Enter Hours in integers")

# 3:
# cel_temp=input("Enter Celsius Temperature: ")
# formula= 9.0/5.0 * float(cel_temp) + 32
# print("Celsius Temperature Converted To Fahrenheit", formula)

# 4:

# cel_temp=input("Enter Celsius Temperature: ")
# try:
#    formula = 9.0 / 5.0 * float(cel_temp) + 32
#     print("Celsius Temperature Converted To Fahrenheit", formula)

# except:
#    print("Enter invalid input")

# 5:
# a=input("Enter integer positive or negative: ")
# a=int(a)
# if a < 0:
#    print("negative")
# elif a > 0:
#    print("positive")


# Import math library and run book progrmae
# import math
# signal_power=float(input("Enter signal power value: "))
# noise_power=float(input("Enter noise power value: "))
# ratio=signal_power/noise_power
# decibels=10 * math.log10(ratio)
# print("raatio: ", ratio)
# print("decibels: ", decibels)
# radians=0.7
# height=math.sin(radians)
# print("heigth: ", height)

# import random

# for i in range(100):
#    x=random.random()
#    print(x)


# for i in range(100):
#    a = random.randint(1,500)
#    print(a)

# random is a built-in function and random it slef have some sub functions:
# list=[1,2,3,4,5,6,7,8,9,10]
# a=random.choice(list)
# print(a)

# functions:
# import math
# def print_twice():
#    print(math.pi)
#    print(math.pi)
# a=print_twice()

# a=float(input("Enter number: "))
# if  a>=0.9 :
#    print("Your grade is 'A'")
# elif a>=0.8 :
#    print("Your grade is 'B")
# elif a>=0.7 :
#    print("Your grade is 'C")
# elif a>=0.6 :
#    print("Your grade is 'D")
# elif a< 0.6:
#    print("You are failed")
# else:
#    print("Enter valid number integer value only")

# iteration:

# for i in range(100):
#    a=(input("Enter table number you want to print: "))
#    if a.isdigit():
#        a=int(a)
#        count = 1
#        for j in range(10):
#            b=a*count
#            print(f"{a} * {count} =  {b} ")
#            count = count + 1
#    elif a.isalpha():
#        if a=="stop":
#            print("Tabel machine print has been stoped")
#            break
#        else:
#            print("Enter valid integer ")
#    else:
#        pass

# do same as while loop
# abhi baki hai thek karna hai isaay thora issue hai
# while True:
#    a = input("Enter table number you want to print: ")
#    if a.isalpha():
#        a.islower()
#        if a == "stop":
#            break
#    else:
#        if a.isdigit():
#            while True:
#                a = int(a)
#                count = 1
#                while count < 11:
#                    t = a * count
#                    print(f"{a}  * {count}  =  {t}")
#                    count = count + 1
#        else:
#            pass

# count 5 for loop
# j = 0
# for i in range(20):
#    print(j)
#    j=j+1

# count 5 while loop
# i=0
# while i < 6:
#    print(i)
#    i=i+1

# i = 1#1,2
# while i < 600:
#  print(i)#1,2
#  i += 1#2,3
# else:
#  print("i is no longer less than 6")

# book programe
# n=10
# while True:
#    print(n,end=" ")
#    n=n-1
#    if n==0:
#        print("\ndone")
#        break

# book programe using continue(skip the current iteration)
# while True:
#    a=input("> ")
#    if a[0]=="#":
#        continue
#    elif a=="done":
#        break
#    print(a)
# print("done")


# definte loops;
# friends=["wasib","saif","laiba"]
# for friend in friends:
#    print("Happy New Year",friends
# print("Done!")


# counting and summing loops:
# count=0
# for itervar in [3.41,12,9,74,15]:
#    count=count+1
#    print("Count: ",count)

# greater number print:
# count=0
# big_none=0
# for itervar in [3,41,12,9,74,15]:
#    if itervar > big_none:
#        big_none=itervar
#        print(big_none)
#    else:
#        pass


#
# total=0
# for itervar in [3,41,12,9,74,15]:
#    total=total+itervar
#   print("Total: ",total)

# progrme book largest number
# largest=None
# print("Before: ",largest)
# for itervar in [3,41,12,9,74,15]:
#    if largest is None or itervar > largest:
#        largest=itervar
#    print("Loop: ",itervar,largest)
# print("Largest",largest)


# book programe smallest number
# smallest=None
# print("Before: ",smallest)
# for itervar in [3,41,12,9,74,15]:
#    if smallest is None or itervar < smallest:
#        smallest=itervar
#    print("Loop: ",itervar,smallest)
# print("Smallest",smallest)


# function smallest number
# def min(value):
#    smallest=None
#    for value in value:
#        if smallest is None or value <smallest:
#            smallest=value
#            return smallest


# Exercise chapter 5:
# total=0
# count=0
# while True:
#    a=input("Enter input: ")
#    if a.isdigit():
#        a=int(a)
#        if a>0:
#            total=total+a
#        else:
#            print("Your number is negative")
#        count+=1
#    elif a=="done":
#        print("Count: ", count,"\nTotal: ",total)
#        break
#    else:
#        try:
#            print(x)
#        except:
#            print("Invalid input")
#            continue


# Exercise chapter 5 finhal
# list=[]
# while True:
#    a=int(input("Enter Interger input: "))
#    var=list.append(a)
#    try:
#        if a=="done" or "Done":
#            break
#    except:
#        print("Enetr valid input: ")
#        continue
# print(var)

# a=[]
# while True:
#    b = input()
#    if b=="done":
#        break
#    else:
#        c = a.append(b)
# print(a)
# min=0
# max=0
# for i in a:
#    if i > min:


# ---------->
# hrs = input("Enter Hours:")
# h = float(hrs)
# hourly_rate=float(10.50)
# if h>0 and h<=40:
#    gross_pay=h*hourly_rate
#    print(gross_pay)
# elif h>40:
#    bonus=(h-40)*1.5
#    pay=40*hourly_rate
#    gross_pay=pay+bonus
#    gross_pay=str(gross_pay)
#    print(gross_pay)
# else:
#    print("Input in invalid")

# ----->
# score = input("Enter Score: ")
# try:
#   scr=float(score)
# except:
#    print("invalid input please enter score")
# if scr>=0.9:
#   print("A")
# elif scr>=0.8:
#   print("B")
# elif scr>=0.7:
#   print("C")
# elif scr>=0.6:
#   print("D")
# else:
#   print("F")


# Python for Data Structure Course 2:----------------------------------------------------->
# Week: 1
# example 1:

# string length
# a="banana"
# print(len(a))

# index and string counting:
# fruit="banana"
# index=0
# while index < len(fruit):
#    letter=fruit[index]
#    print(letter,index)
#    index=index+1

#
# fruit=input("Enter string: ")
# index=3
# while index<len(fruit):
#    letter=fruit[index]
#    print(index,letter)
#    index=index+1

# for loop while loop same work
# fruit="banana"
# index=0
# while index<len(fruit):
#    for letter in fruit:
#        x = fruit[index]
#        print(letter, x)
# print("\n")
# fruit="banana"
# index=0
# while  index < len(fruit):
#     letter=fruit[index]
#     print(letter,index)
#     index=index+1
# print("\n")
# for i in fruit:
#     print(i)

# counting in string
# word='banana'
# count=0
# for letter in word:
#    if letter=='a':
#        print(letter,count)
#        count=count+1
# print(count)


# a="Wasib"
# b="wasib"
# for i in a:
#     a=a[0]+1

# matching two` strings:
# count=0
# a="wasib"
# b="saif"
# for i in a:
#     for i2 in b:
#         if i ==i2:
#             letter=i
#             count=count+1
#             print(i,count)
#         else:
#             pass
#

# Traversal through a string with a lopp:
# fruit="banana"
# index=0
# while index < len(fruit):
#    letter=fruit[index]
#    print(letter,index)
#    index=index+1

# exercixe book reverse string:

# fruit="banana"
# for char in fruit[::-1]:
#    print(char)

# String Slices:
# s="Monty Python"
# print(s[0:5])
# print(s[6:12])
# print(s)

# strings are immutable:

# error
# greeting="Hello World "
# greeting[0]="j"
# print(greeting)

# right method:
# greeting="Hello World "
# new_greeting= 'j' + greeting[1:]    # it's always better to create new string
# print(new_greeting)

# exercise 3:
# def count(a):
#     a=word
#     counta  =0
#     countb = 0
#     countc = 0
#     countd = 0
#     counte = 0
#     countf = 0
#     countg = 0
#     counth=  0
#     counti = 0
#     countj = 0
#     countk = 0
#     countl = 0
#     countm = 0
#     countn = 0
#     counto = 0
#     countp = 0
#     countq = 0
#     countr=  0
#     counts = 0
#     countt = 0
#     countu = 0
#     countv = 0
#     countw = 0
#     countx = 0
#     county = 0
#     countz = 0
#
#     for letter in word:
#         if letter=="a":
#             counta=counta+1
#             print(letter,counta)
#         elif letter == "b":
#             countb=countb+1
#             print(letter,countb)
#         elif letter == "c":
#             countc = countc + 1
#             print(letter, countc)
#         elif letter == "d":
#             countd = countd + 1
#             print(letter, countd)
#         elif letter == "e":
#             counte = counte + 1
#             print(letter, counte)
#         elif letter == "f":
#             countf = countf + 1
#             print(letter, countf)
#         elif letter == "g":
#             countg = countg + 1
#             print(letter, countg)
#         elif letter == "h":
#             counth = counth + 1
#             print(letter, counth)
#         elif letter == "i":
#             counti = counti + 1
#             print(letter, counti)
#         elif letter == "j":
#             countj = countj + 1
#             print(letter, countj)
#         elif letter == "k":
#             countk = countk + 1
#             print(letter, countk)
#         elif letter == "l":
#             countl = countl + 1
#             print(letter, countl)
#         elif letter == "m":
#             countm = countm + 1
#             print(letter, countm)
#         elif letter == "n":
#             countn = countn + 1
#             print(letter, countn)
#         elif letter == "o":
#             counto = counto + 1
#             print(letter, counto)
#         elif letter == "p":
#             countp = countp + 1
#             print(letter, countp)
#         elif letter == "q":
#             countq = countq + 1
#             print(letter, countq)
#         elif letter == "r":
#             countr = countr + 1
#             print(letter, countr)
#         elif letter == "s":
#             counts = counts + 1
#             print(letter, counts)
#         elif letter == "t":
#             countt = countt + 1
#             print(letter, countt)
#         elif letter == "u":
#             countu = countu + 1
#             print(letter, countu)
#         elif letter == "v":
#             countv = countv + 1
#             print(letter, countv)
#         elif letter == "w":
#             countw = countw + 1
#             print(letter, countw)
#         elif letter == "x":
#             countx = countx + 1
#             print(letter, countx)
#         elif letter == "y":
#             county = county + 1
#             print(letter, county)
#         elif letter == "z":
#             countz = countz + 1
#             print(letter, countz)
#         else:
#             print("Enter only Alphabets Invalid input")
#
# word=input("Enter input in string: ")
# b=count(word)
# print(b)
#

# String Comparison:
# word="Pineapple"
# if word=="banana":
#     print("All right, banana")
#
# if word < "banana":
#     print('your word,' + word + "comes before banana")
# elif word > "banana":
#     print('your word,' + word + "comes before banana")
# else:
#     print("All right, bananas.")

# Manipulating string: 6.2
# fruit='banana'
# a='n' in fruit
# print(a)

# strings methods:
# stuff='hello world'
# type(stuff)
# a=dir(stuff)
# for i in a:
#     print(i)


# find function for searching string index value:
# a='wasib'
# b=a.find('b')
# print(b)


# function startswith():
# a='Please have a nice day'
# b=a.startswith('Please')
# c=a.startswith('P')
# d=a.startswith('p')
# print(b,c,d)


# find function index:
# word="banana"
# a=word.find("na")
# b=word.find("na",3) # where it should star from
# print(a)
# print(b)

# function split and strip:
# line="here we go"
# new_line=line.strip()
# check=type(new_line)
# print(new_line,check)
# new_line=line.split()
# check2=type(new_line)
# print(check2,new_line)

# parsing string:
# data="From stephen.marquard@uct.ac.za Sat Jan 5 09 :14:16 2006"
# atpos=data.find('@')
# print(atpos)
# sppos=data.find(" ",atpos)
# print(sppos)
# host=data[atpos+1:sppos]
# print(host)


# format operaor:
# camels=42
# a="%d" % camels
# print(a)

# right my-method
# text = "X-DSPAM-Confidence:0.8475"
# b=type(text)
# find1=text.find(':')
# a=text[19:25]
# f=float(a)
# print(f)
# check=type(f)
# print(check)


# right
# text = "X-DSPAM-Confidence:0.8475"
# t = text.find('0')
# x=text[t:]
# c=float(x)
# print(c)
# check2=type(c)
# print(check2)

# Mcqs auestion
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+8])

# week 2
# Chapter 7 Files:

# 7.2`
# bok programe file not found
# try:
#     fhand=open("stuff.txt")
# except:
#     print("there is no such file exsist")


# 7.3: Text files and Line:

# stuff='hello\nWorld'
# print(stuff)
#
# stuff='X\nY' #-------> there charcter because of \n
# a=len(stuff)
# print(a)


# ------------> C...append input into textfile and read it.
# fhand=open("newfile.txt","w")
# while True:
#     a=input("--> ")
#     if a=="done":
#         break
#     else:
#         wr = fhand.write(a)
# reader=fhand.read()
# print(reader)


# assignmem : 1
# ffname=input("file name input: ")
# ffhandler=open(ffname)
# reader=ffname.read()
# print(reader)

# assignment: 2
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking
# for lines of the form:X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating point values from each of
# the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or
# a variable named sum in your solution.You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when
# you are testing below enter mbox-short.txt as the file name.

# my solution of program
# fname = input("Enter file name: ")
# fh = open(fname)
# total = 0
# count = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     else:
#         s = line.rstrip()
#         print(line)
#         count = count + 1
#         t = line.find('0')
#         x = line[t:]
#         c = float(x)
#         total += float(line[line.find(":") + 1:])
# print("Average spam confidence:", total / count)

# mbox-short.txt

# internet solution ------------------> ? ? ? ? ?/ / / / / / / //
# fname = input("Enter file name: ")
# fh = open(fname)
# total = 0.0
# count = 0.0
# for line in fh:
#     if line.startswith("X-DSPAM-Confidence:"):
#         total += float(line[line.find(":") + 1:])
#         count += 1
#     else:
#         continue
#
# print("Average spam confidence:", total / count)

#practice remaining questions of book


# Week 4:
# List:
# sunday

print(python)