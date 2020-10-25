import time
for i in range(0,4):

    def add(x,y,b):
        return x + y + b 


    def subtract(x,y,b):
        return x - y - b


    def multiply(x,y,b):
        return x * y * b


    def divide (x,y,b):
        return x/y/b


    def power(x,y,b):
        return pow(x,y,b)

    #take input from user
    print("Select operation.")
    print("1.Add")
    print("1.Subtract")
    print("1. Multiply")
    print("1.Divide")
    print("1.Power")
    choice=input("Enter choice 1/2/3/4/5:")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter a third number: "))



    if choice == '1':
        print(num1, "+", num2, "+", num3, "=", add(num1,num2,num3))

    elif choice == '2':
        print(num1, "-", num2, "-", num3, "=", subtract(num1,num2,num3))

    elif choice == '3':
        print(num1, "x", num2,"+", num3, "=", multiply(num1,num2, num3))

    elif choice == '4':

        print(num1, "/", num2, "/", num3, "=",  divide(num1,num2,num3))
    elif choice == '5':
        print(num1, "^", num2, "^", num3, "=", power(num1,num2,num3))



start_time = time.time()
time.sleep(3)
quit()


        
