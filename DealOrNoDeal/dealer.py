# Description:
#   The following class recieves the calculated
#   value for the user's case, presents the
#   information in the form of an offer,
#   and returns the user's decision.
#
# OOP Principles Used:
#   Inheritance
#   Polymorphism
#   Encapsulation
#   Abstraction
#
# Reasoning:
#   This class uses inheritance because
#   'Dealer' is a child of 'Calculator'.
#
#   This class uses polymorphism because
#   both the 'Dealer' and 'Calculator' classes
#   have a 'total' variable, but the value
#   is different for each one.
#
#   This class uses encapsulation because
#   both '__init__' and 'make_deal' are
#   class-specific methods that are
#   defined within the class itself.
#
#   This class uses abstraction because
#   'total' is found by using the
#   external 'calculate' method.


from calculator import Calculator

class Dealer(Calculator):
    def __init__(self, cash_left):
        self.total = self.calculate(cash_left)
    
    def make_deal(self):
        print("The dealer would now like to offer a price for your personal case.")
        print(f"Hey says that he is willing to offer ${self.total:,.0f}. 'Deal' or 'No Deal'? ")
        answer = ''
        while answer != 'deal' or answer != 'no deal':
            answer = input('> ').lower()
            if answer == 'no deal':
                return True
            elif answer == 'deal':
                return False
            else:
                print('That is not a valid answer. Try again!')
