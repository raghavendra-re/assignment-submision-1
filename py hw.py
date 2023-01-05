n=int(input())
for i in range (0,n):
    for j in range (0,i+1):
        print("*",end="")
    print("")
for x in range (n,0,-1):
    for y in range (0,x-1):
        print("*",end="")
    print("")
print()
