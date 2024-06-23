"""
Author: Jayce Hopia
Date: 06/23/2024
Class: 330
Description: This file contains the BankAccount class for the Banking DSL.
Pledge: This work is all my own with the help of Lucas.
"""

import random

###################################
#####    BANK ACCOUNT CLASS   #####
###################################

class BankAccount:
    def __init__(self, first_name: str, last_name: str, balance: float = 0.0, account_number: str = None):
        # Initializes a new bank account with the given first name, last name, and balance.
        # Generates an account number based on the first and last name if not provided.
        self._first_name = first_name
        self._last_name = last_name
        self._balance = balance
        self._account_number = account_number if account_number else self._generate_account_number()

    def _generate_account_number(self) -> str:
        # Generates an account number using the first initials of the first and last name
        # followed by six random digits.
        initials = self._first_name[0] + self._last_name[0]
        digits = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return initials + digits

    @property
    def first_name(self):
        # Returns the first name of the account holder.
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        # Sets the first name of the account holder.
        self._first_name = value

    @property
    def last_name(self):
        # Returns the last name of the account holder.
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        # Sets the last name of the account holder.
        self._last_name = value

    @property
    def balance(self):
        # Returns the current balance of the account.
        return self._balance

    @balance.setter
    def balance(self, value):
        # Sets the current balance of the account.
        self._balance = value

    @property
    def account_number(self):
        # Returns the account number of the account.
        return self._account_number

    def deposit(self, amount: float):
        # Deposits the given amount into the account.
        self._balance += amount

    def withdraw(self, amount: float):
        # Withdraws the given amount from the account.
        # Raises a ValueError if the amount exceeds the current balance.
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        # Returns a string representation of the bank account.
        return f"{self._first_name} {self._last_name}, Account: {self._account_number}, Balance: {self._balance}"