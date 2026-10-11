while True:
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("% to get Remainder")
    print("/ for Division")
    ch = input("\n Enter operation from (+,-,*,%,/) =")
    if(ch == "+"):
       result = num1+num2
       print(f"result:{num1} + {num2} ={result}")
    elif(ch == "-"):
        result = num1-num2
        print(f"result:{num1} - {num2} ={result}")
    elif(ch == "*"):
        result = num1*num2
        print(f"result:{num1} * {num2} ={result}")
    elif(ch == "%"):
        result = num1%num2
        print(f"result:{num1} % {num2} ={result}")
    elif(ch == "/"):
        if(num2 != 0):
            result = num1/num2
            print(f"result:{num1} / {num2} ={result}")
        else:
            print("Can not Divide becuase denominator is zero")
    else:
        print("Please Enter a vaild operation (+,-,*,%,/)")
    again =input("if you want to calculate again (yes/no) :")
    if again =="no":
        print("Thank You for using calculator")
        break
        