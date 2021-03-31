## Simple Calculator ##

f_value = int(input("Enter First Value: "))
s_value = int(input("Enter Second value: "))

print("\nSelect Operations: ")
print("Press 1 for Addition.")
print("Press 2 for Subtraction.")
print("Press 3 for Multiplication.")
print("Press 4 for Division.")
operator = input("Select: ")

if operator == "1":
    print("\nAnswer:", f_value + s_value)
elif operator == "2": 
    print("\nAnswer:", f_value - s_value)
elif operator == "3":
    print("\nAnswer:", f_value * s_value)
elif operator == "4":
    print("\nAnswer:", f_value / s_value)
else:
    print("ERROR: Invalid Operator.")






input("Press enter to exit.")
