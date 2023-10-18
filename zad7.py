while True:
    try:
        x = int(input("Type a number: "))
        if x > 10000000:
            print("The number is too big.")
            False
        elif x < 1:
            print("The number must be positive.")
            False
        else:
            break
    except ValueError:
        print ("It is not a number.")
    
        
    
    

for n in range(1,x+1):
    if x % n == 0:
        print(int(x/n), end = ", ")
print()

                
            

