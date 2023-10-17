while True:
    try:
        x = int(input("Podaj liczbe "))
        break
    except ValueError:
        pass
for n in range(1,x+1):
    print(" "*(x-(n-1)),"*"*(n*2-1),sep="")
print(" "*(x), "U",sep="")