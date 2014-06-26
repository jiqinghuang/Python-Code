balance = 4773
annualInterestRate = 0.2


Mp = 0
indicator = 0
base = balance
while indicator == 0:
    Mp = Mp + 10
    for i in range(1, 13):
        Ub = balance - Mp
        balance = Ub + annualInterestRate/12 * Ub
    if balance > 0:
        balance = base
    else:
        indicator = 1
    
print('Lowest Payment: ' + str(Mp))













