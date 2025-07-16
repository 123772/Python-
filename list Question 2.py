#Exercise 4.1
animals =  ['cat','dog', 'goat']
for animal in animals:
    print(f"{animal.title()}, I love animals!")
print (f"sheep also animal")
#Exercise 4.2
animals  =  ['chicken', 'tiger', 'goat']
for animal in animals:
    print(animal)
print(f"{animals[0]}, is eat maize")
print(f"{animals[1]}, is eat meat")
print(f"{animals[2]}, is eat leaf") 

print("all are animal")
#Exercise 4.3
for value in range(21):
  print(value)
#Exercise 4.4
numbers = list(range(1,1000001))
print(numbers )
#Exercise 4.5
print(min(numbers ))
print(max(numbers ))
print(sum(numbers ))
#Exercise 4.6
odd_numbers = list(range(21,2))
print(odd_numbers)
#Exercise 4.7
multiple_three = list(range(3,30,3))
print(multiple_three)
#Exercise 4.8
cubes =  [ ]
for value in range(1, 10):
    cubes.append(value**3)
print(cubes)
#Exercise 4.9
cubes = [value**3 for value in range(1,10)]
print(cubes)
#Exercise 4.10
animals =  ['cat','dog','goat','sheep','cow','chicken', 'hen']
#first three number
print(animals[:3])
#middle number
print(animals[2:5])
#last three number
print(animals[-3:])
#Exercise 4.11
my_foods = ['pizza ', 'falafel','carrot cake']
friend_pizzas  = my_foods
my_foods.append('cream cake')
for my_foods in 
print(my_foods)
friend_pizzas.append('kkk')
friend_pizzas.append('odddd')
print(friend_pizzas)