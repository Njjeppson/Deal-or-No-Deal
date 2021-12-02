# Description:
#   The following class runs each aspect of the
#   program in the appropriate order according to
#   the steps of the game.
#
# OOP Principles Used:
#   Abstraction
#
# Reasoning:
#   This class uses abstraction because the majority
#   of its complex actions are executed by calling
#   methods established in seperate classes.


from cases import Cases
from dealer import Dealer
personal_case = {}
# Creates an instance of 'Cases'
cases = Cases
# Randomly fills the cases with cash
cases.fill_cases(cases)

# Refreshes the case keys that are left
cases.refresh(cases)

# Lets the player pick their personal case
print('The following cases are available:')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(cases.case_keys)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Please pick your personal case. This is the one you will either keep or sell throughout the rest of the game.')
personal_case_num = int(input('> '))
print(f'Your personal case is #{personal_case_num}.')

# Sets the personal case and removes it from the options
personal_case = cases.cases[personal_case_num]
del cases.cases[personal_case_num]
cases.refresh(cases)

# Continually runs through each round until the player accepts the deal
deal = True
round = 1
while deal and len(cases.cases) > 1:
    if round == 1 or round == 2:
        num = 5
    elif round == 3:
        num = 4
    elif round == 4 or round == 5:
        num = 2
    else:
        num = 1
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Cases left:')
    print(cases.case_keys)
    print('Cash left:')
    print(cases.cash_left)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'You may now open {num} case(s).')
    for i in range(num):
        case = int(input('> '))
        if case not in cases.cases:
            while case not in cases.cases:
                print('That case is not available. Try again.')
                case = int(input('> '))

        print(f'There was ${cases.cases[case]:,.0f} in case #{case}')
        cases.remove(cases, case)
        cases.refresh(cases)
    
    dealer = Dealer(cases.cash_left)
    deal = dealer.make_deal()
    round += 1

# Reveals how much cash was in the personal case.
print("Let's see what was inside of your personal case...")
print(f'${personal_case:,.0f}')