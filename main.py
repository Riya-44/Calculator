print("THIS THIS IS A CALCULATOR")
history = []
while True:
    try:

        print("Select operation:\n 1. +\n2. -\n3. *\n4. /\n5. Exit\n6. History")
        c=input("Enter choice(1/2/3/4/5/6):")
        if c=="5":
            print("Exiting the calculator.")
            break
        if c=="6":
            print("history:")
            for item in history:
                print(item)
            continue
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        match c:
            case "1":
                result=a+b
                op="+"
            case "2":
                result=a-b
                op="-"
            case "3":
                result=a*b
                op="*"
            case "4":
                if b != 0:
                    result=a/b
                    op="/"
                else:
                    print("Cannot divide by zero.")
                    continue
            case _:
                print("Invalid input.")
                continue
            
        print(f"result:= {result}")
        history.append(f"{a}{op}{b}={result}")
    
    except ValueError:
        print("Invalid input.")
    

        