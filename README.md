# 🖥️ Logic Gates Simulator (Python)

A lightweight, interactive Python tool designed to simulate fundamental digital logic gates. This project processes binary strings of any length, making it a perfect resource for understanding **Boolean Algebra** and **Digital Logic**.



[Image of logic gate symbols and truth tables]


## 🌟 Key Features
* **Full Logic Support:** Includes AND, OR, XOR, NOT, NAND, NOR, and XNOR.
* **Multi-bit Processing:** Handles binary sequences of any length (e.g., `10101`).
* **Input Validation:** Ensures inputs are strictly binary and matching in length.
* **Interactive CLI:** User-friendly interface with a continuous execution loop.

## 🛠️ Logic Gates Summary

| Gate | Logic Description |
| :--- | :--- |
| **AND** | `1` only if both inputs are `1`. |
| **OR** | `1` if at least one input is `1`. |
| **NOT** | Inverts the input (`0` ↔ `1`). |
| **XOR** | `1` if inputs are different. |
| **NAND** | Inverse of AND. |
| **NOR** | Inverse of OR. |
| **XNOR** | `1` if inputs are identical. |

## 🚀 Usage
Run the script using:
```bash
python logic_gates.py
Enter the name of the logic gate: XOR
Enter the first binary number: 1010
Enter the second binary number: 1100
The result of XOR gate is: 0110
