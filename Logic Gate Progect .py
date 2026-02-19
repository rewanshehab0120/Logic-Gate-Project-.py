def logical_gate():
    print("\nChoose from these gates: AND, OR, XOR, NOT, NAND, NOR, XNOR")
    gate = input("Enter the name of the logic gate: ").upper()    
    A = input("Enter the first binary number: ")
    B = ""
    
    if gate != "NOT":
        B = input("Enter the second binary number: ")
        if len(A) != len(B):
            print("Error: The two binary numbers must have the same length.")
            return

    def is_binary(n):
        for i in n:
            if i not in ['0', '1']:
                return False
        return True

    if not is_binary(A):
        print(f"Error: {A} is not a binary number.")
        return
    if gate != "NOT" and not is_binary(B):
        print(f"Error: {B} is not a binary number.")
        return
    
    result = ""
    if gate == "AND":
        for a, b in zip(A, B):
            result += '1' if a == '1' and b == '1' else '0'
    elif gate == "OR":
        for a, b in zip(A, B):
            result += '1' if a == '1' or b == '1' else '0'
    elif gate == "XOR":
        for a, b in zip(A, B):
            result += '1' if a != b else '0'
    elif gate == "NOT":
        for a in A:
            result += '0' if a == '1' else '1'
    elif gate == "NAND":
        for a, b in zip(A, B):
            result += '0' if a == '1' and b == '1' else '1'
    elif gate == "NOR":
        for a, b in zip(A, B):
            result += '0' if a == '1' or b == '1' else '1'
    elif gate == "XNOR":
        for a, b in zip(A, B):
            result += '1' if a == b else '0'
    else:
        print("Error: Logic Gate not found.")
        return
    
    print(f"The result of {gate} gate is: {result}")

print("--- Welcome to Logic Gate Simulator ---")
while True:
    logical_gate()
    again = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if again == "no":
        print("Thank you for using our program. Goodbye!")
        break
