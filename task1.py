while True:
    inputNumber = input("Enter a number: ")

    if inputNumber.isdigit() or (inputNumber.startswith('-') and inputNumber[1:].isdigit()):
        num = int(inputNumber)
        break
    else:
        print("Invalid input! Please enter only numbers.")

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
