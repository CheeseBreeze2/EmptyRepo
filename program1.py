#Author: Isaac Martinec
#This program says hello and asks for the user's name

print('Hello World')
yourName = input('Please enter your name: ') # ask for their name
print('It is good to meet you, ' + yourName + '.')
#Now count the number of characters in yourName variable
#and convert the result to string so it can be concatenated to another string
print('The length of your name is : ' + str(len(yourName)))
