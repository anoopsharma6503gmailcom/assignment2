# 1
#a
str1="Python is a case sensitive language"
print(len(str1))
#b
str1 = "Python is a case sensitive language"
print(str1[::-1]) 
#c
str1 = "Python is a case sensitive language"
str2 = str1[10:26]
print(str2)
#d
str1 = "Python is a case sensitive language"
print(str1.replace("a case sensitive", "object oriented"))
#e
str1 = "Python is a case sensitive language"
print(str1.find("a"))
#f
str1 = "Python is a case sensitive language"
#to replace white spaces we can replace spaces with blank
print(str1.replace(" ", "")) 
#2
inp_name = input("Hi Pecian, Please enter your name\n")
inp_SID = input("Please enter you SID[eg.2110XXXX]\n")
inp_course = input("Please enter your department[eg.CSE,ECE,ELE,etc.]\n")
inp_CGPA = input("Please enter your CGPA[eg.5.5,9.0,10.0]\n")


print("Hey,",inp_name, "Here!")
print("My SID is", inp_SID)
print("I am from", inp_course, "department and my CGPA is", inp_CGPA) 
#3
a=56
b=10
#3a
print(a&b)
#3b
print(a|b)
#3c
print(a^b)
#3d left shift both by 2
print(a<<2)
print(b<<2)
#3e right shift a by 2 and b by 4
print(a>>2)
print(b>>4) 

#4
inp_str = input("Enter your string\n")
#now find the string using 'in' function
if "name" in inp_str:
#print yes or no
    print("Yes")
else:
    print("NO") 
#5
a = int(input("Enter first length\n"))
b = int(input("Enter second length\n"))
c = int(input("Enter third length\n"))
#now check one by one that any of the three lengths is greater than the sum of the other two or not
if a+b<=c or a+c<=b or c+b<=a:
    print("No")
else:
    print("Yes") 
#6
a=int(input("enter the number:"))
b=int(input("enter the number:"))
num=a^b
count_flipped_bit=0
while(num !=0):
    num=num&(num-1)
    count_flipped_bit+=1
print(count_flipped_bit)
#SOLUTIONS
#1a
35

#1b
egaugnal evitisnes esac a si nohtyP

#1c
a case sensitive

#1d
Python is object oriented language

#1e
10

#1f
Pythonisacasesensitivelanguage

#2
Hi Pecian, Please enter your name
anoop
Please enter you SID[eg.2110XXXX]
21102032
Please enter your department[eg.CSE,ECE,ELE,etc.]
civil
Please enter your CGPA[eg.5.5,9.0,10.0]
9.9
Hey, anoop Here!
My SID is 21102032
I am from civil department and my CGPA is 9.9

#3
(a) 8
(b) 58
(c) 50
(d) 224
    40
(e) 14
    0


#4
hi, my name is anoop
Yes
hi, i am from pec
NO

#5
Enter first length
8
Enter second length
6
Enter third length
10
Yes

Enter first length
6
Enter second length
5
Enter third length
1
no 
