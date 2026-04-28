# 🏦 Python OOP Banking System (Mini Project)

A simple **Object-Oriented Programming (OOP)** project in Python that demonstrates core OOP concepts using a banking system simulation.

---

## 📌 Features

- 🧾 Create bank accounts with name, account number, and balance  
- 💰 Deposit money  
- 💸 Withdraw money with balance validation  
- 📈 Interest calculation for savings account  
- 🚫 Overdraft support for current account  
- 🏧 Abstract banking service structure  

---

## 🧠 OOP Concepts Used

### 🔒 Encapsulation
- Private attribute `__balance`
- Access controlled via methods like `get_balance()`, `deposit()`, `withdraw()`

---

### 👨‍👩‍👧‍👦 Inheritance
- `SavingAccount` inherits from `Account`
- `CurrentAccount` inherits from `Account`

---

### 🎭 Abstraction
- `BankService` is an abstract base class
- Defines `transaction()` method structure

---

### 🔁 Method Overriding
- `withdraw()` method is overridden in `CurrentAccount`

---

## ⚙️ Classes Overview

### 🏦 Account (Base Class)
- Stores user account details  
- Manages deposit and withdraw operations  
- Keeps balance private  

---

### 💰 SavingAccount
- Adds interest calculation feature  
- Uses balance from parent class  

---

### 💳 CurrentAccount
- Supports overdraft limit  
- Overrides withdraw logic  

---

### 🏧 BankService (Abstract Class)
- Defines structure for banking services  
- Contains abstract method `transaction()`  

---

### 🏧 ATM / VisaCard
- Implements `transaction()` method  
- Represents different banking service types  

## 👨‍💻 Author

**Sadia Afsana**
