def logical_gate():
    print("Choose from these gates :\nAND, OR, XOR, NOT, NAND, NOR, XNOR")
    gate = input("Enter the name of the logic gate: ").upper()    
    A = input("Enter the first binary number :")
    B = ""
    
    if gate not in ["NOT"]:
        B = input("Enter the second binary number:")
        
        if len(A) != len(B):
            print("Error ,\nThe tow binary numbers must have the same length")
            return
    
    def is_binaery(n):
        for i in n:
            if i !=('0','1'):
                return False
        return True
    if is_binaery(A)=="False":
        print(f"{A} is not a binary number")
        return
    if is_binaery(B)=="False":
        print(f"{B} is not a binary number")
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
        print("Logic Gate is not found ")
        return
    
    print(f"The result of {gate} gate is : {result}")
print("Welcome to Logice Gate Program ")
while True:
    logical_gate()
    again = input("Do you want any other operations :\nYes \nNo\n")
    if again.lower() =="no":
        print("Thank you for using our program")
        break