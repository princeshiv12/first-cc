a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = input("Enter choice (1-5): ")

if choice == '1':
    print("Result:", a + b)

elif choice == '2':
    print("Result:", a - b)

elif choice == '3':
    print("Result:", a * b)

elif choice == '4':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error! Division by zero.")

elif choice == '5':
    print("Result:", a % b)

else:
    print("Invalid choice")
