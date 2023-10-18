# Pytamy uzytkownika o dodatnia liczbę całkowitą.
while True:
    try:
        x = int(input("Podaj sumę ciągu Fibonacciego: "))
        if x > 0:
            break
        else: 
            raise(ValueError)
    except ValueError:
        print("Suma musi być liczbą całkowitą dodatnią.")
# y,z to kolejne wyrazy ciągu Fibonacciego, które początkowo wynoszą 1 i 1.
y = 1
z = 1
suma = 2
# Określamy za pomocą pętli while funkcję, która liczy sumę wyrazów ciągu Fibonacciego
# tak długo, az przekroczy wartość podaną przez uzytkownika.
while x > suma:
    # Liczenie wyrazów ciągu Fibonacciego
    z = z + y
    y = z - y
    suma = suma + z
# Zwracamy wyniki naszych obliczeń.
if suma == x:
    print(f"Istnieje podciąg ciągu Fibonacciego o sumie {x}")
else:
     print(f"Nie ma podciągu ciągu Fibonacciego o sumie {x}. Istnieją natomiast podciągi o wartościach {suma - z} i {suma}")
