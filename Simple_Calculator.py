## Simple Calculator ##
#Input two values, select operator and it will show the result.

def s_calculator(f_input,s_input):
    if operator == "1":
        return f_input + s_input
    elif operator == "2": 
        return f_input - s_input
    elif operator == "3":
        return f_input * s_input
    elif operator == "4":
        return f_input / s_input
    else:
        print("ERROR: Invalid Operator.")

f_value = int(input("Enter First Value: "))
s_value = int(input("Enter Second value: "))

print("\nSelect Operations: ")
print("Press 1 for Addition.")
print("Press 2 for Subtraction.")
print("Press 3 for Multiplication.")
print("Press 4 for Division.")
operator = input("Select: ")

print("\nAnswer: ",s_calculator(f_value,s_value))


input("Press enter to exit.")
