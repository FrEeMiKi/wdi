import math
import random
x = int(input("Pierwsza liczba: "))
print("+ - dodawanie\n- - odejmowanie\n* - mnozenie\n/ - dzielenie\n# - pierwiastkowanie\n^ - potęgowanie\nx - losowanie liczby z zakresu")
o = str(input("Wybierz operację: "))
match o:
    case "+":
        y = int(input("Druga liczba: "))
        print("Odpowiedź to:",x+y)
    case "-":
        y = int(input("Druga liczba: "))
        print("Odpowiedź to:",x-y)
    case "*":
        y = int(input("Druga liczba: "))
        print("Odpowiedź to:",x*y)
    case "/":
        y = int(input("Druga liczba: "))
        print("Odpowiedź to:",x/y)
    case "#":
        print("Odpowiedź to:",math.sqrt(x))
    case "^":
        y = int(input("Do jakiej potęgi? :"))
        print("Odpowiedź to:",x**y)
    case "x":
        y = int(input("Druga liczba: "))
        print("Odpowiedź to:",random.randint(x,y))
        