'''10. Write a Python script to create a list, where each element of the list is a digit of a
given number.'''
n=int(input("enter how many digit you want to store:"))
digit=[]
for i in range(1,n+1):
    digit.append(int(input("enter a digit")))
print("enter digit are:")
print(digit)