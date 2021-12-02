# Description:
#   The following class calculates a
#   reasonable offer for the Dealer
#   class to retrieve and present.
#   This offer is based on both the
#   number of cases left and the
#   cash values left in those cases.
#
# OOP Principles Used:
#   Polymorphism
#   Encapsulation
#
# Reasoning:
#   This class uses polymorphism because
#   both the 'Calculator' and 'Dealer' classes
#   have a 'total' variable, but the value
#   is different for each one.
#
#   This class uses encapsulation because
#   both '__init__' and 'calculate' are
#   class-specific methods that are
#   defined within the class itself.


class Calculator():
    def __init__(self):
        self.total = 0
    
    def calculate(self, cash_left):
        total = 0
        for i in cash_left:
            total += i / len(cash_left)
        return total