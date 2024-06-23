"""
Author: Jayce Hopia
Date: 06/23/2024
Class: 330
Description: This file contains the BankAccount class for the Banking DSL.
Pledge: This work is all my own with the help of Lucas.
"""

import random

class BankAccount:
    def __init__(self, first_name: str, last_name: str, balance: float = 0.0):
        self._first_name = first_name
        self._last_name = last_name
        self._balance = balance
        self._account_number = self._generate_account_number()

    def _generate_account_number(self) -> str:
        initials = self._first_name[0] + self._last_name[0]
        digits = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return initials + digits

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        return f"{self._first_name} {self._last_name}, Account: {self._account_number}, Balance: {self._balance}"
