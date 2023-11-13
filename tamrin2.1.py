row = int(input("Enter the row: "))
col = int (input("Enter the column: "))

for i in range(row):
    for j in range(col):
        if (i + j) % 2 == 0:
                print("1", end=" ")  
        else:
                print("0", end=" ") 
    print()
