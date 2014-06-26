balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total = 0
for i in range(1, 13):
    month = i
    Mmp = monthlyPaymentRate * balance
    total = total + Mmp
    Ub = balance - Mmp
    balance = Ub + annualInterestRate/12 *Ub
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(Mmp, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))

print('Total paid: ' + str(round(total, 2)))
print('Remaining balance: ' + str(round(balance, 2)))




