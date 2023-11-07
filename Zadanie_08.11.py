lista = []
lista2 = []
while True:
     try:
          for _ in range(5):
               _ = int(input(f"Podaj {_ + 1} liczbę całkowitą: "))
               lista.append(_)
          break
     except ValueError:
          print("Podaj liczby całkowite!")

for i in range(len(lista)-1):
     liczba1 = lista[i]
     liczba2 = lista[i+1]
     if liczba1 < liczba2:
          for x in range(liczba2-liczba1):
               lista2.append(liczba1 + x)
     else:
          for x in range(liczba1-liczba2):
               lista2.append(liczba1 - x)
lista2.append(lista[-1])
print(lista2)
     
