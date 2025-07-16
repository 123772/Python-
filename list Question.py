#Exercise 3.1
friend_name = ['sadiya' ,'khewlet' ,'mehbuba']
print(friend_name[0])
print(friend_name[1])
print(friend_name[2])
#Exercise 3.2
message = "Aselamu Alykum werahmetulahi weberekatu"
print(f"{message} {friend_name[0]}")
print(f"{message} {friend_name[1]}")
print(f"{message} {friend_name[2]}")
#Exercise 3.3
transportation = ['car' , 'motor cycle' ,'Airplane']
message = f"I would like to own a honda {transportation[1].title()}."
print(message)
#Exercise 3.4
guests = [ 'meryem'  , 'halima'  , 'kedija' ]
message = "you're invited to dinner"
print (f"{message} {guests[0]}")
print (f"{message} {guests[1]}")
print (f"{message} {guests[2]}")

#Exercise 3.5
print("kedija can't make a dinner ") 
guests[2] = 'hayat'

print (f"{message} {guests[0]}")
print (f"{message} {guests[1]}")
print (f"{message} {guests[2]}")
#Exercise 3.6
print("i found a bigger table ")
guests.insert(0, 'Eman')
guests.insert(2, 'rahma')
guests.append('husniya')
print (f"{message} {guests[0]}")
print (f"{message} {guests[1]}")
print (f"{message} {guests[2]}")
print (f"{message} {guests[3]}")
print (f"{message} {guests[4]}")
print (f"{message} {guests[5]}")
#Exercise 3.7

print("I can invite only to people for dinner ")
remove_guest1 = guests.pop(0)
remove_guest2 = guests.pop(0)
remove_guest3 = guests.pop(0)
remove_guest4 = guests.pop(0)

message = "sorry i can't invite you to dinner"
print (f"{message} {remove_guest1}")
print (f"{message} {remove_guest2}")
print (f"{message} {remove_guest3}")
print (f"{message} {remove_guest4}")
message = "your are still invited "
print (f"{message} {guests[0]}")
print (f"{message} {guests[1]}")
del guests[1]
del guests[0]
print(guests)
#Exercise 3.8
location = ['jaban' , 'America' , 'china']
print(location )
print(sorted(location ))
print(location)
location.reverse()
print(location)
location_sorted = sorted(location)
location_sorted.reverse()
print(location_sorted)
print(location)
location.sort()
print(location)
print(location)
location.reverse()
print(location)
#Exercise 3.'10
letter = ['j' ,'A' ,'c']
print(letter)
letter.insert(1, 'g')
print(letter)
letter.append('f')
print(letter )
print("length of the letter :",len(letter))
#Execise 3.11
# index_error 
print(letter[-1
])
