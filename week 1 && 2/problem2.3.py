balance = 999999
annualInterestRate = 0.18


mr = annualInterestRate/12.0
lower = balance/12.0
upper = balance* (1+mr)**12 / 12.0
indicator = 0
base = balance
precision = 0.001
while indicator == 0:
    mp = (lower + upper)/2.0
    for i in range(1, 13):
        Ub = balance - mp
        balance = Ub + annualInterestRate/12 * Ub
    if balance >= precision:
        lower = mp
        balance = base
    elif balance <= -precision:
        upper = mp
        balance = base   
    else:
        indicator = 1
    
print('Lowest Payment: ' + str(round(mp, 2)))




