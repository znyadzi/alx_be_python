i = int(input("Enter the size of the pattern: "))
p = 0
while not p == i:
    for j in range(0,i):
        print("* ", end="")
    print()
    p+=1
