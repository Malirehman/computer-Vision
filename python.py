#dictiona   ry ik key value pair ko sstore karta hai
"""
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict) """

#accessing values
#
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}   
#print(my_dict["name"]) 

#opertors in python
#arithmetic operators
"""
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
"""
"""
fruits = ["apple", "banana", "cherry"]

print(fruits[1])
#banana

# ye create kiya hamne or acces karke print kardia


# ab ham cars k leye banaeinge

cars = ["BMW", "Audi", "Toyota"]
print(cars[1])
print(cars[2])


cars = cars + ["Mercedes"]
print(cars)


cars[1]= "Honda"
print(cars)

print("**")
print(cars[0:2]) # ye slicing hai bmw or honda print krega

print(cars[-1]) # ye last element print krega

print(cars[:3]) # ye start se 3rd index tak print krega


more_cars = ["Ford", "Chevrolet"]
all_cars = cars + more_cars
print(all_cars)
print(cars)

new_cars = ["tesla"]
print(new_cars)
cars.append(new_cars[0]) # ye append method hai jo list k end me element add krega
print(cars)
# ham ik list k ander ik or list add kar sakte hai append method se

cars = ["BMW", "Honda", "Toyota", "Mercedes"]
cars.append("Audi")
print(cars)

new_carss = ["Lexus", "Infiniti"]
cars.extend(new_carss) # ye extend method hai jo ik list k ander dusri list k elements add krega
print(cars)

cars = ["BMW", "Honda", "Toyota", "Mercedes"]
cars.insert(1, "Audi") # ye insert method hai jo ik specific index pr element add krega
print(cars)

cars.remove("Honda") # ye remove method hai jo ik specific element ko list se remove krega
print(cars)

lasrt_car = cars.pop() # ye pop method hai jo last element ko remove karke return krega
print(lasrt_car)
#ab ham list ko clear karenge 

#ye permanently list ko clear kardaiga
cars.clear()
print(cars)

# hamare kisi list ma frequency check karna ho to ham count method use karenge
cars = ["BMW", "Honda", "Toyota", "Mercedes", "BMW"]
print(cars.count("BMW")) # ye count method hai jo ik specific element ki frequency check`` krega
# output 2 aayega kyunki BMW 2 baar list ma hai

# ham kisi list item ko index b check karsakte hai
print(cars.index("Toyota")) # ye index method hai jo ik specific element ka index return
# output 2 aayega kyunki Toyota 2nd index pr hai

cars = ["BMW", "Honda", "Toyota", "Mercedes", "BMW"]
print(cars.count("BMW")) # ye count method hai jo ik specific element ki frequency check krega
# output 2 aayega kyunki BMW 2 baar list ma hai
print(cars.index("Toyota")) # ye index method hai jo ik specific element ka index return krega
# output 2 aayega kyunki Toyota 2nd index pr hai
cars.clear()
print(cars)

#ab ham sorting karenge e lisgt ma elemsnmt ko ascending order ma
cars = ["BMW", "Honda", "Toyota", "Mercedes", "Audi"]
cars.sort() # ye sort method hai jo list k elements ko ascending order ma sort krega
print(cars)

cars.sort(reverse=True) # ye sort method hai jo list k elements ko descending order ma sort krega
print(cars)
# iski samaj nahi ayee to aap mujhe puch sakte ho
# ye reverse method hai jo list k elements ko reverse krega
cars.reverse()
print(cars)
# revers or descending ma fark hai
# descending ma largest element pehle aata hai or reverse ma last element pehle aata
cars = ["BMW", "Honda", "Toyota", "Mercedes", "Audi"]
new_cars = cars.copy() # ye copy method hai jo ik list ki copy banata hai
new_cars.append("Lexus")
print(new_cars)
print(cars)

cars.sort(reverse=True) # ye sort method hai jo list k elements ko descending order ma sort krega
print(cars)
cars.reverse()
print(cars)

cars = [
    ["BMW", "M5 CS", "M3"],
    ["Audi", "RS7", "A8"],
    ["Toyota", "Supra", "Corolla"]
]
 
cars[1][2] = "q7"
print(cars)"""
"""
Garage = []

while True:
    print("\n === car garage Manager ===")
    print("1. Add a car")
    print("2. Remove a car")
    print("3. View all cars")
    print("count all cars")
    print("5. Exit")

    choice = input("Enter your chioce (1-5):")

    if choice == "1":
        car = input("enter car name to add:")
        Garage.append(car)
        print(f"{car} has been added to the garage.")

    elif choice == "2":
        car = input("enter car name to remove:")
        if car in Garage:
            Garage.remove(car)
            print(f"{car} has been removed from the garage.")
        else:
            print(f"{car} is not found in the garage.")
    elif choice == "3":
        if Garage :
            print("cars in the garage:", Garage)

    elif choice == "4":
        print("Total number of cars in the garage:", len(Garage))

    elif choice == "5":
        print("Exiting the Car Garage Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
"""
# tuples
# ye list ki tarah hi hota hai but ye immutable hota hai yani iske elements ko change nahi kar sakte
# ye round brackets ma banta hai
"""
cars = ("BMW", "Honda", "Toyota", "Mercedes")
print(cars)
print(cars[1]) # ye 1st index pr element print krega

#cars[1] = "Audi" # ye error dega kyunki tuples immutable hota hai
#print(cars)
# ye error dega kyunki tuples immutable hota hai
# tupls ham len , count , index method use kar sakte hai
print(len(cars)) # ye len method hai jo tuples k elements ki length return krega
print(cars.count("BMW")) # ye count method hai jo ik specific element ki frequency check krega
print(cars.index("Toyota")) # ye index method hai jo ik specific element ka index return

# ham set ki jaga tuples use kar sakte hai jab hame data ko change nahi karna hota

myset = {"apple", "apple","banana", "cherry"}
print(myset)

cars  = {"bmw","audi","toyota"}
cars.add("honda") # ye add method hai jo set me ik element add krega
print(cars)
#{} se start hota hai set lekan add karne k leye () use karte hai

cars.remove("audi") # ye remove method hai jo set me ik specific element ko remove krega
print(cars)

num1 = {1,2,3,4,5,6}
num2 = {3,4,5,6,7}

un = num1.union(num2) # ye union method hai jo do sets ko combine krega without duplicates
print(num1.intersection(num2)) # ye intersection method hai jo do sets ke common elements ko return krega
print(num1.difference(num2)) # ye difference method hai jo pehle set ke elements me se dusre set ke elements ko remove krega
print(num1.symmetric_difference(num2)) # ye symmetric difference method hai jo do sets ke unique
print(un)

for car in cars:
    print(car)

for index , car in enumerate(cars):
    print(index, car)

fruits = ("apple", "banana", "cherry")
for index , fruit in enumerate(fruits):
    print(index, fruit)

cars = ["BMW", "Honda", "Toyota", "Mercedes"]
for index , car in enumerate(cars):
    print(index, car)
    #enumarte 2 values return krta hai

print("zaidullah")
cars = [ "Audi", "Toyota", "Honda","BMW"]

search = "BMW"

for car in cars:
    if car == search:
        print(search, "mil gayi!")
        break
else:
    print(search, "list me nahi hai.")


marks =[33,4,0,55,66]
total =0

for m in marks:
    total +=m

average= total/len(marks)

print(total,"total")
print(average,"average")   

text = "articfica   l intelligence is future"

vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count +=1

print("number of vowels:", count)



# ab function karte hai

def greet(name):
    print("hello", name)

greet("zaidullah")


def intro(name,age):
    print("my name is ",name ,"and my age is ",age)

intro("ali" , 25)

def add(a,b):
    return a+b

sum = add(5,12)

print("sum is", sum)

def average_marks(m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3
    return avg ,total
average = average_marks(85, 90, 95)
print("Average Marks:", average)
print("total marks:", total)


# ab function ma list or loop 

def list_sum(numbers):
    total =0
    for n in numbers:
        total +=n
        avg = total / len(numbers)
    return total , avg

marks = [65,44,33,55]

total, average = list_sum(marks)
print("total:", total)
print("average:", average)

def sum(numbers):
    total =0
    for n in numbers:
        total +=n
    avg = total / len(numbers)
    return total , avg

marks = []

sub = int(input("enter number of subjects:"))

for i in range(sub):
    mark = int(input(f"enter marks for subject {i+1}:"))
    marks.append(mark)

sum, average = sum(marks)
print("total:", sum)
print("average:", average)"""
"""
# ab ham default parameters karenge

#jab function ma koi arg nahi hota to default value kaam karti hai ye value ham khod deltehia 

def greet(name="Guest"):
    print("hello", name)

greet()# yaha per adefault value lagiigi
greet("zadullah") #yaha per hamne value di hai to ye value print hogi
"""
"""
file = open("test.txt", "a")
file.write("i am writing and read at same time")

file.close()

file = open("test.txt", "r")
content = file.read()
file.close()
print(content)

file = open("test.txt", "w")
file.close()
file = open("test.txt","w")
file.write("hello  this is the fresh start by muhammad " \
"ali and from room of islamia hostel")
file.close()

file = open("test.txt", "a")
file.write("\n this is the second line added to the file")
file.close()# ye append mode hai jo file k end me content add krega

#ab ham new file banayenge or usme content add karenge
file = open("newfile.txt", "w")
file.write("this is a new file created by python")
file.close()

file = open("newfile.txt", "r")
content = file.read()
file.close()

#ab ham test ma new file ka content add karenge

file = open("test.txt", "a")
file.write(content)
file.close()
"""
"""
with open("test.txt", "w") as f:
    f.write("XXXXXXXXXXXX ")
    f.close()

    with open("test2.txt","w") as f2:
        f2.write("this is test2 file ")
        f2.write("and this is second line of test2 file")
        f2.write("\n this is third line of test2 file")
        f2.close()

with open("test2.txt", "r") as f2:
    content = f2.read()
    print(content)
    f2.close()

with open("test2.txt","r") as f2:
    print(f2.readline()) # ye ik line read krega
    print(f2.readline()) # ye ik line read krega
    f2.close()

with open("test2.txt","r") as f2:
    lines = f2.readlines() # ye sari lines ko list ma read krega
    print(lines)
    f2.close()'
    """
"""
with open("userData.txt", "a") as f:
     name = input("enter your name:")
     age =  input("enter your age:")
     f.write(f"\nname: {name}, age: {age}")
     f.close()

with open("userData.txt", "r") as f:
    content = f.read()
    print(content)
    f.close()
    """
