'''Create a list fruits = ["apple", "banana", "cherry"].

Print the first fruit.
Replace "banana" with "orange".
Print the length of the list.'''

fruits=["apple","banana","cherry"]
print(fruits[0])
fruits[1]="orange"
print(len(fruits))
print(fruits)

'''Create a list of numbers from 1 to 10.

Print the first three numbers using slicing.
Print the last three numbers using slicing.'''

numbers=list(range(1,11))
print(numbers)
print(numbers[7:10])

'''Start with numbers = [5, 2, 9, 1, 7] and do the following:

Sort the list in ascending order.
Append the number 10 to the list.
Remove the number 2 from the list.'''
print(" ******************** ")
number=[5,2,9,1,7]
print(number)
number.sort()
print(number)
number.append(10)
print(number)
number.remove(2)
print(number)

'''Create a list names = ["Alice", "Bob", "Charlie"] 
and use the insert() method to add "David" at index 1.'''

names=["alice","bob","charlie"]
print(names)
names.insert(1,"David")
print(names)

#Tuples and Operations on Tuples
'''Create a tuple coordinates = (10, 20) and print both elements.'''
print("*****Tuples and Operations on Tuples******")
coordinates=(10,20)
print(coordinates)

'''Convert the tuple to a list, 
change its first element to 50, and convert it back to a tuple.'''
print("********************")
my_tuple=(1,3,5,'a','b')
print(my_tuple)
my_list=list(my_tuple)
my_list[0]=50
my_tuple=tuple(my_list)
print(my_tuple)

#Sets and Set Methods
print("********Sets and Set Methods********")
'''Create a set my_set = {1, 2, 3, 3, 4}
 and print it. (What happens to duplicate 3?)'''

my_set={1,2,3,3,4}
print(my_set) # the number 3 is printed only once
 
'''Add 5 to the set, remove 2, and check if 4 is in the set.'''
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
if 4 in my_set:
    print("yes")
else:
    print("no")

'''Create two sets:

a = {1, 2, 3}

b = {3, 4, 5}
Find their:

Union

Intersection

Difference (a - b)'''

a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Dictionaries and Dictionary Methods
print("Dictionaries and Dictionary Methods")
"""Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:

Print the value of "name".
Change "grade" to "A+".
Add a new key "city" with value "Delhi"""

student={"name": "john",
         "age":"20",
         "grade":"A"}

print(student["name"])
student["grade"]="A+"
print(student)
student["City"]="delhi"
print(student)

'''Create a dictionary of three friends and their phone numbers. Use:

keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them'''

friends={ "shwetha" :7736525852,
         "shruthi" :989952535,
         "krithi":8746535241}
print(friends.keys())
print(friends.values())
print(friends.items())

'''Write a program that takes a list of numbers and removes
 all duplicates using a set.'''

list1= [1,2,5,6,1,1,8,9,0]
print(list1)
myset =set(list1)
print(myset)

'''Given a dictionary of products and their prices,
 find the product with the highest price.'''

products={"pen" :10,
          "notebook": 59,
          "bag": 1000}
max_product=max(products,key=products.get)
max_price = products[max_product]

print(f"The product with the highest price is {max_product} at ${max_price}.")

#Write a program that merges two dictionaries into one

dict1={"name":"shwetha",
       "age" :20}

dict2={"height" :5.1}

merged=dict1.copy()
merged.update(dict2)
print(merged)
