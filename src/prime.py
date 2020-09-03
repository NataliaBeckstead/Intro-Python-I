number = int(input("Please, enter the number: "))
if number > 1: 
    for i in range(2, number):
       if (number % i) == 0: 
            print("It is not a prime number") 
            break
    else: 
        print("It is a prime number") 
else:
    print("It is not a prime number")