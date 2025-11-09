#Write a program to print the numbers in reverse order beginning from the number 
# entered by the user.
num=int(input("Enter a number"))
for i in reversed (range (num)):
    print(i)