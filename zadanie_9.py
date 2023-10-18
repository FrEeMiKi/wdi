x = int(0)
pin = int
print("Witamy w banku KKO!")
while True:
    while pin not in range(1000,9999):
        try:
            pin = int(input("Ustal swój czterocyfrowy nr PIN: "))
        except ValueError:
            pass
    try:
        if int(input("Powtórz swój nr PIN: ")) == pin:
            break
        else:
            pin = 0
    except ValueError:
        pass
        

    
def autoryzacja():
    n = int(0)
    for _ in range(3):
        if int(input("Podaj swój nr PIN: ")) == pin:
            break
        elif _ == 2:
            print("Wpisano nieprawidłowy PIN 3 razy. Konto zostało zablokowane.")
            raise(SystemExit)
        
        
while True:
    try:
        print("Jaką operację chcesz wykonać?\na) Wpłata\nb) Wypłata\nc) Saldo konta\nd) Wyjście")
        wybor = input("Wybór: ")
        if wybor == "a":
            autoryzacja()
            x = x + int(input("Kwota wpłaty: "))
        elif wybor == "b":
            autoryzacja()
            x = x - int(input("Kwota wypłaty: "))
        elif wybor == "c":
            autoryzacja()
            print("\n###############\nSaldo:", x, "zł\n###############\n")
        elif wybor == "d":
            print("Do Widzenia!")
            break
    except ValueError:
        pass
    except SystemExit:
        break
    
    
    