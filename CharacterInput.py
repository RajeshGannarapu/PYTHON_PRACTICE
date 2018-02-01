#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year 
#that they will turn 100 years old.


#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#(Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


import datetime
name = input("Please enter your name: ")
age = input ("Please enter your age: ")

result = "Hello %s , You will turn 100 year at %d \n" %(name, 100- int(age)+ datetime.date.today().year)

num = input ("How many time you want to print the summary: ")

print(result * int(num))


