x = int(0)
pin = int(input("Ustal swój nr PIN: "))
def autoryzacja():
    if int(input("Podaj swój nr PIN: ")) == pin:
        pass
    else:
        ValueError
    


while True:
    try:
        print("Jaką operację chcesz wykonać?\na) wpłata\nb) wypłata\nc) saldo konta\nd) wyjście")
        wybor = input("Wybór: ")
        if wybor == "a":
            autoryzacja()
            x = x + int(input("Kwota wpłaty: "))
        elif wybor == "b":
            autoryzacja()
            x = x - int(input("Kwota wypłaty: "))
        elif wybor == "c":
            autoryzacja()
            print("Saldo:", x, "zł")
        elif wybor == "d":
            print("Do Widzenia!")
            False
    except ValueError:
        pass
    
    
    