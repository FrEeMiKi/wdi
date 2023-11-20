# Zadanie 9.
# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n x n wypełnioną liczbami
# naturalnymi. Dla danej tablicy należy napisać funkcję, która zwraca wiersz i kolumnę dowolnego
# elementu, dla którego iloraz sumy elementów w kolumnie w którym leży element do sumy elementów wiersza
# w którym leży element jest największa. Wymiar tablicy powinien być definiowany przez użytkownika.


from random import randint

def matrix():       # Funkcja generująca macierz
    while True:
        try:    
            n = int(input("Size: "))
            if not 0 < n < 1000:
                print("Size must be higher than 0 and lower than 1000")
                raise ValueError
            break
        except ValueError:
            pass 
    res = [[randint(0,9) for i in range(n)] for i in range(n)]
    return res

def dzban(inp): # Funkcja, która kazdej wartości w macierzy przyporządkowuje wynik dzialania opisanego w poleceniu
    res = [row[:] for row in inp]
    l = len(inp)
    for row in range(l):
        for col in range(l):
            res[row][col] = sum(inp[i][col] for i in range(l)) * sum(inp[row][j] for j in range(l))
    return res    

########## y matri

x = matrix()
y = dzban(x)

print("Your matrix:")
for row in x:
    print(row)

# Dla zobrazowania działania kodu wypisujemy macierz dzban(x)

print("Matrix dzban(x):")
for row in y:
    print(row)
    
# Szukamy, gdzie znajduje się największa wartość

max_value = max(max(row) for row in y)
max_row_col = [(i + 1, j + 1) for i, row in enumerate(y) for j, value in enumerate(row) if value == max_value]

print("Maximum value is", max_value")
print("Maximum value's row and column:", max_row_col)
