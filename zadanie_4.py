name = "Mikolaj"
fname = "Majcherek"
age = 19
favdish = "Schabowy"
favpet = "Pies"
k = 5/7
#a
print("a)", end = " ")
print(name)
print(fname)
print(age)
print(favdish)
print(favpet)
print(k)


#b
print("b)", end = " ")
print(name,fname,age,favdish,favpet,k, sep=", ")

#c
print("c)", end = " ")
print("5 podzielone przez 7 to:", round(k,1), round(k,3), round(k,5), round(k,10), sep="\n")

#d - wersja bez zmiennych

#a
print("a)", end = " ")
print("Mikolaj")
print("Majcherek")
print(19)
print("Schabowy")
print("Pies")
print(5/7)


#b
print("b)", end = " ")
print("Mikolaj","Majcherek",19,"Schabowy","Pies",5/7 , sep = ", ")

#c
print("c)", end = " ")
print("5 podzielone przez 7 to:", round(5/7,1), round(5/7,3), round(5/7,5), round(5/7,10), sep="\n")
