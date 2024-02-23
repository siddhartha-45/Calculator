def switch():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    print("please select your Arithmetic operation: \nPress 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
    option = int(input("Enter your option: "))
    if option == 1:
        result = a+b
        print("Addition of a + b = : ", result)
    elif option == 2:
        result = a-b
        print("Subtraction of a - b = : ",result)
    elif option == 3:
        result = a*b
        print("Multiplication of a * b = : ", result)
    elif option == 4:
        result = a/b
        print("Division of a / b = : ",result)
    else:
        print("Invalid Value")
switch()
