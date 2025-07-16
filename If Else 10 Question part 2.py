# Exercise 1: chek even or odd
n = list(map(int, input("Enter the list:").split(',')))
even = [ ]
odd  = [ ]
for num in n:
      if num % 2 == 0:
             even.append(num)
      else:
          odd. append(num)
print("odd: ", odd)
print ("even:", even)
#Exercise:2 chek positive, negative and zero
num = list(map(int, input ("Enter the list numbers: ").split()))
positive = [ ]
negative = [ ]
zero = [ ]
for n in num:
    if n > 0:
       positive.append(n)
    elif n < 0:
        negative. append(n)
    else: 
         zero. append (n)
print("positive", positive)
print("negative", negative)
print("zero", zero)
#Exercise:3 count even number
n = list(map(int, input("Enter the list:"). split()))
even = 0
for i in n:
       if i % 2 == 0:
           even += 1
print(even)   
#Exercise: 4 find largest number
n = eval(input("Enter the list:"))
largest = 0
for i in n:
    if i > largest:
        largest = i
print(largest)
#Exercise:5 check number greater than 20 in list
n = list(map(int, input("Enter the list:"). split()))
num = [ ]
for i in n:
    if  i >= 20:
        num.append(i)
print("num", num)
#Exercise:6 check for specific number
n = list(map(int, input("Enter the list:"). split()))
request_num = 42
if request_num in n:
    print("yes you are correct the number is inside the list")
else:
    print ("you are rong the number is not found")
#Exercise:7check the grade
n = list(map(int, input("Enter the list:"). split()))
for number in n:
   if number >= 90 and number <= 100:
          print("A") 
   elif number >=80 and number < 90:
           print("B")
   elif number >= 70 and number < 80:
            print("C")   
   elif number >= 60 and number < 70:
             print("D")      
   elif number < 60 and number > 0:
           print("F")   
   else:
          print("the number you enter is not correct")   
#Exercise: 8 sum of the posetive 
n = list(map(int, input("Enter the list:"). split()))
total = 0
for number in n:
    if number > 0:
        total += number
print("total", total) 
#Exercise: 9 change all negative to zero
n = list(map(int, input("Enter the list:"). split()))
number = [ ] 
for i in n:
    if i < 0 :
        number. append(0)
    else:
        number.append(i)  
print(number)    
#Exercise: 10 count range 
n = list(map(int, input("Enter the list:"). split()))
range = 0
for i in n:
    if i >= 10 and i <= 50:
        range += 1
print(range)            