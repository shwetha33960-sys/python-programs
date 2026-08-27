#Create a string variable name with your full name. Print:

#The first character
#The last character
#The length of the string

'''name="Shwetha Nayak"
print(name[0])
print(name[-1])
print(len(name))'''

#Concatenate two strings: "Hello" and "World" with a space in between.
'''string1="hello"
string2="world"
print(string1+" "+string2)'''

#Given text = "Python Programming", do the following:

#Print the first 6 characters
#Print the last 6 characters
#Print every second character from the string
'''text="python programming"
print(text[:6])
print(text[-6:])
print(text[1:-1:2])'''

#Reverse the string text using slicing
'''text="program"
print(text[::-1])'''

#Take the string "  i love python programming  " and:

#Remove extra spaces from both ends
#Convert it to title case
#Count how many times "o" appears
'''text=" i love pythson programmimg "
print(text.strip())
print(text.title())
print(text.count("o"))'''

# Check if the string "123abc" is alphanumeric.
'''text="123abc"
print(text.isalnum())'''

#Using format(), create a sentence:
#"My name is John and I am 25 years old."
#by passing "John" and 25 as variables.
'''name="john"
age=25
print("my name is {} and I am {} years old".format(name,age))'''

#Do the same using f-strings.
'''name="john"
age=25
print(f"my name is {name} and i am {age} years old")'''

#Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
'''sentence="coding in python is fun"
print(sentence.replace("fun","awesome"))'''

#Find the index of the word "Python" in sentence.
'''sentence=" i love python"
print(sentence.index("python"))'''

#Convert the entire sentence to uppercase and print it.
'''sentence=" i love python"
print(sentence.upper())'''

#Write a program that counts how many vowels are in a given string.
sentence=" i love python"
sum=0
vowels=['a','e','i','o','u']
for char in sentence.lower():
    if(char in vowels):
        sum+=1
print(f"there are {sum} of vowels in sentence")

#Take a user input string and check if it is a palindrome (same forwards and backwards).
text=input("enter a string")
reversed_text=text[::-1]
if(text==reversed_text):
    print(f"{text} is a palindrome")
else:
    print("not a palindrome")

