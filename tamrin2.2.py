name = input("Enter ur name: ")
last = input("Enter ur last name: ")
age = input("Enter ur age: ")
while True:
    if not name:
        name = input("ENTER UR NAME!!\n")
    elif not last:
        last = input("ENTER UR LAST NAME!!\n")
    elif not age:
        age = input("ENTER UR AGE!!\n")
    else:
        break
print(name.upper(),last.upper())
print(name.count('a'))
print(last.replace('a','x'))