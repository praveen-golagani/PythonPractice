try:
    # taking input and converting it from string to integer
    first_num = int(input("Enter first number : "))
    second_num = int(input("Enter second number : "))
    third_num = int(input("Enter third number : "))

    # logic to find greater
    if first_num == second_num == third_num:
        print(" all are equal")
    elif first_num >= second_num and first_num >= third_num:
        print(f"{first_num} is greater")
    elif second_num >= third_num:
        print(f"{second_num} is greater")
    else:
        print(f"{third_num} is greater")
except Exception as ValueError:
    print("Invalid entry please enter numbers only")
except Exception as e:
    print(f"error occurred {e}")
