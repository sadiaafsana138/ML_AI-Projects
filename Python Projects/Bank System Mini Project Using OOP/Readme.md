# 🏦 Python OOP Banking System

A simple **Object-Oriented Banking System** built using Python to demonstrate core OOP concepts like:

- Encapsulation 🔒  
- Inheritance 👨‍👩‍👧‍👦  
- Abstraction 🎭  
- Method Overriding 🔁  

---

## 📌 Features

- 🧾 Create bank accounts  
- 💰 Deposit money  
- 💸 Withdraw money with validation  
- 📈 Interest calculation for savings account  
- 🚫 Overdraft support for current account  
- 🏧 ATM & Visa card abstraction system  

---

## 🧠 OOP Concepts Used

### 🔒 Encapsulation
- Private balance (`__balance`)
- Controlled access using methods

### 👨‍👩‍👧‍👦 Inheritance
- `SavingAccount` and `CurrentAccount` inherit from `Account`

### 🎭 Abstraction
- `BankService` abstract class defines transaction structure

### 🔁 Polymorphism
- `withdraw()` method is overridden in `CurrentAccount`

---

## 📂 Project Structure
Bank System Mini Project Using OOP/
│
├── Bank System - Mini Project Using OOP.py        # All classes and execution code

⚙️ Classes Overview
🏦 Account (Base Class)
Stores account details
Handles deposit & withdraw
Keeps balance private
💰 SavingAccount
Adds interest calculation feature
💳 CurrentAccount
Supports overdraft facility
🏧 BankService (Abstract Class)
Defines transaction() method
🏧 ATM / VisaCard
Implements transaction methods


🎯 Learning Outcome

This project helps you understand:

Real-world banking system logic
OOP design principles in Python
Code reusability and modular structure
Data security using encapsulation

👨‍💻 Author
Sadia Afsana
