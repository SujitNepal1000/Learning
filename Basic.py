Car = "Ford mustang 1969"
name = "Jhon Wick"

print(name + " owns " + Car)

#function creation

def addition():
    a = 4
    b = 5
    c = int(input("enter the value of c"))
    print(a + b + c)


addition()

#arguments

def user_info(name, age, address):
    print("Hello i am {}, i am {} years old and i live in {}".format(name, age, address))


user_info("Jhon", 25, "kathmandu")


def greet(name):
    print("hello," + name + " " + "good morning")


greet("Jhon")

# condition

print(1 > 0)
print(1 <= 0)

number = int(input("enter a number"))
if number > 10:
    print("number is greater than 10")
elif 5 < number <= 10:
    print("number is less or equals to 10 and greater than 5")
else:
    print("number is less than 5")

#loops

# for loop

name = ["jhon","sam","jhonny"]

for i in name:
    print("Hello my name is {}".format(i))

# while loop

number = int(input("Enter any number"))

#nested loop

rows=int(input("enter the number of rows"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

while number > 17:
    print("The range of numbers {} are".format(number))
    number -= 1
    if number == 17:
        break
for number in range (10,20):
    if number == 17:
        print("skip number 17")
        continue
    print("The numbers are {}".format(number))

# list
fruits = [ "apple", "banana", "mango"]

print(fruits)

fruits.append("orange")
print(fruits)

fruits.extend(["grapes", "watermelon"])
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.insert(2, "kiwi") 
print(fruits)

number = [99,95,45,69,83]
number.sort()
print(number)

#QUE find the sum of numbers in the list

def sum(num):
    total = 0
    for i in num:
        total += i
    return total

num = [1,2,3,4,5,6,7,8,9,10]
print("The sum of number in the list is : ",sum(num))

#dictionary

student = {'name': 'John', 'age': 21,'city': 'Kathmandu'}
new_student = {'name': 'Sam', 'age': 22,'city': 'Lalitpur'}

print(student)

print(student['name'])

#add data to dictionary 
student['address'] = 'Kirtipur'
print(student)

#update value of a key in dictionary
student['age']=22
print(student)

#using get method
print(student.get('name')) 

#using items method
print(student.items())

#using keys method
print(student.keys())

#using values method
print(student.values())

#using pop method
print(student.pop('address'))
print(student)

student.update(new_student)
print(student)
