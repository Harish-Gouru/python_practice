from abc import ABC, abstractmethod

#abstract class
class ATM(ABC):
    
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
    @abstractmethod
    def checkbalance(self):
        pass
    
  
  
  # Hiding class (Background process)  
class ATMWorking(ATM):
    
    def __init__(self , balance):
        self.balance = balance
    
    def  deposit(self , amount):
        self.balance += amount
        print(f"Amount Deposited Rs.{amount} : Available Balance is : {self.balance} ")
        print("=========================")
        
    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawed Rs.{amount} : Available Balance is : {self.balance} ") 
            print("===============================") 
        else:
            print("Insufficient Balance")
            print("===============================")      
        
    def checkbalance(self):
        print(f" Your available balance is : {self.balance}")
    
    
atm = ATMWorking(10000)
atm.deposit(2000)
atm.withdraw(2000)
atm.checkbalance()    
    
    
    