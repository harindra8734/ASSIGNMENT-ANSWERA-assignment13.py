'''6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
'''


Firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
#Firstlist.append(secondlist)
#print(Firstlist)
Firstlist.extend(secondlist)
print(Firstlist)