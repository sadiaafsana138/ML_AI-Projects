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
-│
-├── Bank System - Mini Project Using OOP.py        # All classes and execution code

## ⚙️ Classes Overview

---

### 🏦 Account (Base Class)
- Stores account details  
- Handles deposit & withdraw operations  
- Keeps balance private for security  

---

### 💰 SavingAccount
- Adds interest calculation feature  
- Inherits from Account class  

---

### 💳 CurrentAccount
- Supports overdraft facility  
- Overrides withdraw method for extra flexibility  

---

### 🏧 BankService (Abstract Class)
- Defines `transaction()` method  
- Acts as a blueprint for banking services  

---

### 🏧 ATM / VisaCard
- Implements transaction methods  
- Provides different ways to perform banking operations  

---

## 🎯 Learning Outcome

- Real-world banking system logic  
- Strong understanding of OOP design principles in Python  
- Code reusability and modular architecture  
- Data security using encapsulation  

---

## 👨‍💻 Author

**Sadia Afsana**
