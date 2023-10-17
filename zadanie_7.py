while True:
    try:
        x = int(input("Podaj pierwsza liczbe "))
        y = int(input("Podaj druga liczbe "))
        przedzial = [x,y]
        break
    except ValueError:
        pass
if abs(x-y) <= 20:
    for n in range(min(x,y),max(x,y)):
        print(n)
else:
    z = int(round((x+y)/2,0))
    print(z-3,z-2,z-1,z+1,z+2,z+3, sep="\n")
    