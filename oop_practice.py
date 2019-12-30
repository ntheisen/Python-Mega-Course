# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 08:41:23 2019

@author: the607
"""

class Account:
    
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amt):
        self.balance = self.balance - amt
        
    def deposit(self, amt):
        self.balance = self.balance + amt

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

#inheritance example

class Checking(Account):
    '''This class creates a checking account object'''
    
    type = 'checking'
    
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amt, fee=0):
        self.fee = fee
        self.balance = self.balance - amt - self.fee



checking = Checking('balance.txt')
checking.deposit(10)
print(checking.balance)
checking.transfer(120, fee=1)
checking.transfer(100)
print(checking.balance)
checking.commit()

print(checking.__doc__)

'''
account = Account('balance.txt')
print(account.balance)
account.withdraw(100)
account.deposit(200)
account.commit()
print(account.balance)
'''