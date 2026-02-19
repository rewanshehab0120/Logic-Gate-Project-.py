import tkinter as tk
from tkinter import messagebox

def calculate_logic():
    # Retrieve user inputs and gate selection
    gate = gate_var.get()
    A = entry_a.get().strip()
    B = entry_b.get().strip()

    # Helper function to validate if the input string is purely binary
    def is_binary(n):
        return all(bit in ['0', '1'] for bit in n)

    # Validate that fields are not empty (B is ignored for NOT gate)
    if not A or (gate != "NOT" and not B):
        messagebox.showerror("Error", "Please enter binary numbers!")
        return

    # Ensure all inputs consist of 0s and 1s only
    if not is_binary(A) or (gate != "NOT" and not is_binary(B)):
        messagebox.showerror("Error", "Inputs must be binary (0 or 1)!")
        return

    # Ensure both binary strings have the same length for dual-input gates
    if gate != "NOT" and len(A) != len(B):
        messagebox.showerror("Error", "Binary numbers must have the same length!")
        return

    result = ""
    try:
        # Perform bitwise logical operations based on the selected gate
        if gate == "AND":
            result = "".join('1' if a == '1' and b == '1' else '0' for a, b in zip(A, B))
        elif gate == "OR":
            result = "".join('1' if a == '1' or b == '1' else '0' for a, b in zip(A, B))
        elif gate == "XOR":
            result = "".join('1' if a != b else '0' for a, b in zip(A, B))
        elif gate == "NOT":
            result = "".join('0' if a == '1' else '1' for a in A)
        elif gate == "NAND":
            result = "".join('0' if a == '1' and b == '1' else '1' for a, b in zip(A, B))
        elif gate == "NOR":
            result = "".join('0' if a == '1' or b == '1' else '1' for a, b in zip(A, B))
        elif gate == "XNOR":
            result = "".join('1' if a == b else '0' for a, b in zip(A, B))
        
        # Display the result in the label with a green color
        lbl_result.config(text=f"Result: {result}", fg="#00FF00")
    except Exception as e:
        # Catch and display any unexpected errors
        messagebox.showerror("Error", str(e))

# Initialize the main application window
root = tk.Tk()
root.title("Logic Gate Simulator - Rwan Shehab")
root.geometry("400x450")
root.configure(bg="#2c3e50") # Dark theme background

# Application Header
tk.Label(root, text="Logic Gate Simulator", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

# Gate Selection Dropdown
tk.Label(root, text="Select Logic Gate:", bg="#2c3e50", fg="white").pack()
gate_var = tk.StringVar(value="AND")
gates = ["AND", "OR", "XOR", "NOT", "NAND", "NOR", "XNOR"]
gate_menu = tk.OptionMenu(root, gate_var, *gates)
gate_menu.pack(pady=5)

# Input field for the first binary number
tk.Label(root, text="Enter First Binary (A):", bg="#2c3e50", fg="white").pack()
entry_a = tk.Entry(root, font=("Arial", 12), justify='center')
entry_a.pack(pady=5)

# Input field for the second binary number
tk.Label(root, text="Enter Second Binary (B):", bg="#2c3e50", fg="white").pack()
entry_b = tk.Entry(root, font=("Arial", 12), justify='center')
entry_b.pack(pady=5)

# Button to trigger the calculation logic
btn_calc = tk.Button(root, text="Calculate Result", command=calculate_logic, 
                     bg="#27ae60", fg="white", font=("Arial", 12, "bold"), width=20)
btn_calc.pack(pady=20)

# Label to display the final output
lbl_result = tk.Label(root, text="Result: ", font=("Courier", 14, "bold"), bg="#2c3e50", fg="#f1c40f")
lbl_result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
