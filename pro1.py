print("temperature converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter choice (1 or 2) : ")

if choice == "1":
    celsius = float(input("Enter celsius : "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit : ", fahrenheit)

elif choice == "2":
    fahrenheit = float(input("Enter fahrenheit : "))
    celsius = (fahrenheit - 32) * 9/5 
    print("celsius : ", celsius)

else:
    print("invalid choice")