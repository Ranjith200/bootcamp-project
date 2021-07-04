import hashlib

string=input('Enter your string: ')
#To get the value from user

hash=hashlib.md5(string.encode())
#encoding string using encode then sending to md5

print('\nThe hexadecimal equvalent of the entered string is: ')
print(hash.hexdigest())
#prints the hexadecimal value of string

print("\nThe byte equvalent of the entered string is: ")
print(hash.digest()) 
#prints the byte value of string