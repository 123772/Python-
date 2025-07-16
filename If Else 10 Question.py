# Question 1 guess the word
if __name__ ==  '__main__':
    a = int(input("guess the number between 1-10: "))
    if a == 7:
           print("correct")
    else:
           print("try again")
  # Question 2 positive or negative
if __name__ == '__main__':
      a = int(input("Enter the number: "))     
      if a < 0:
              print("negative")  
      elif a > 0:
              print("positive") 
      else:
              print("0")
# Question 3 sum of numbers
if __name__ == '__main__':
      number = int(input("Enter the positive integer number: "))   
      total = 0
      for i in range(1, number + 1):
              total += i
              print(total)
#question 4: count voul
word = input("Enter the word: ")
count = 0
for letter in word:
    if letter.lower() in "aeiou":
        count += 1
print( count)
# question 5 count even number
if __name__ == '__main__':
      number = int(input("Enter the number: "))   
      even = 0
      for i in range(1, number + 1):
            if  i % 2 == 0:
                print(i)

# question 6  Grade calculater  
if __name__ == '__main__':
      number = int(input("Enter a score (0-100): "))
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
# question 7 Multiplication Table (Extended)
if __name__ == '__main__':
      number = int(input("Enter the number: ")) 
      for i in range(1,  number + 1):
             for j in range(1, 11):
                  print(f"{i} × {j} = {i * j}")
# question 8 password cheker
if __name__ == '__main__':
      password = input("Enter the password: ")    
      correct_password = "secret123"
      if password == correct_password:
         print("Access granted")
      else:
          print("Access denied")
 # Question 9 star pyramid;
if __name__ == '__main__':
      num = int(input("Enter the positiv integer number: ")) 
 
      for i in range( num+1 ):
             star_pyramid = '*' * i
             print(star_pyramid)
#question 10: count down
n = int(input("Enter the number: "))
for i in range(n, 0, -1):
   print(i)
print("Blast off !")
                                       
                        