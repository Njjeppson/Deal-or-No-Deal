# Description:
#   The following class randomly assigns
#   each cash value within a list to 26
#   distinct cases. Additonally, the
#   class removes any cases that
#   have been eliminated from the
#   game and refreshes the list
#   of available cases that is
#   shown to the player.
#
# OOP Principles Used:
#   Encapsulation
#
# Reasoning:
#   This class uses encapsulation because
#   '__init__', 'fill_cases', 'refresh',
#   and 'remove' are class-specific methods
#   that are defined within the class itself.


from random import *

class Cases:
    def __init__(self):
        self.cases = {}
        self.cash_list = []
        self.case_keys = []

    def fill_cases(self):
        self.cases = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '', 16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: ''}
        self.cash_list = [1, 5, 10, 15, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        self.cash_left = [1, 5, 10, 15, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        for i in self.cases:
            random_cash = randint(0, len(self.cash_list) - 1)
            self.cases[i] = self.cash_list[random_cash]
            del self.cash_list[random_cash]
        
    def refresh(self):
        self.case_keys = list(self.cases.keys())

    def remove(self, case):
        self.cash_left.remove(self.cases[case])
        del self.cases[case]