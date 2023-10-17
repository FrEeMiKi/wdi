#pytamy uzytkownika o 2 liczby
x = float(input("Wprowadzona przez Ciebie pierwsza liczba to "))
y = float(input("Wprowadzona przez Ciebie druga liczba to "))
#podajemy dzialania na tych liczbach
if x < 0 and y < 0:
    exit
    print("Obie liczby są mniejsze od zera")
    exit
elif x < 0 or y < 0:
     x = abs(x)
     y = abs(y)
print("Suma tych liczb to", x+y)
print("Roznica tych liczb to", x-y)
print("Iloczyn tych liczb to", x*y)
if x*y == 10:
    print("Yay!")
print("Iloraz tych liczb to", x/y)
