# Vending-Machine-Simulation-Using-DFA-NFA-and-Python


## Objective: 
The purpose of this assignment is to design and implement a vending machine simulator using the concepts of Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA). You will apply formal language concepts to represent the machine's behavior and simulate its operations using Python. 
You are tasked with designing a vending machine that sells the following items: 
![image](https://github.com/user-attachments/assets/c0324fbb-8b6d-403a-a011-492f4c53ade5)
## Machine Behavior: 
• The machine only accepts values of RM0.5 and RM1. 
• All other values (RM5, RM10, RM20, RM50, RM100) are rejected and returned to the user. 
• If the inserted amount matches the item price, the item is dispensed. 
• If the inserted amount exceeds the price, the machine will: 
❖ Dispense the item 
❖ Return the excess money as change 
• The user can select a new item after each purchase. (This point in code implementation only) 
## The vending machine's behavior can be described using formal language concepts as follows: 
• Alphabet (Σ): 
Σ={0.5,1, Invalid}  
Where: 
0.5 represents RM0.5 value, 1 represents RM1 value, Invalid represents values like RM5, 
RM10, RM20, etc.
