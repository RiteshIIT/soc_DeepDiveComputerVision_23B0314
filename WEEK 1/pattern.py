# Diamond pattern generator



def diamond(rows):
    midpoint=rows//2

    for i in range(1,midpoint+1):
        for j in range(midpoint-i):
            print(" ",end="")
        for j in range(i*2):
            print("*",end="")
        print()

    for i in range(midpoint,0,-1):
        for j in range(midpoint-i):
            print(" ",end="")
        for j in range(i*2):
            print("*",end="")
        print()

rows=int(input("Enter even number of rows for diamond : "))
diamond(rows)
        
            