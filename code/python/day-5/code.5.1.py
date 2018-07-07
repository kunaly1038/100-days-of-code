rate = int(input('\nEnter the rate % per annumm :'))
principal = int(input('\nEnter the principal :'))
time = int(input('\nEnter the time period :'))

rate =(1+ rate/100)
time = rate**time
amount = principal * time
print('\nThe amount is :', amount)
print('\nThe Compound Interest is :',amount-principal)

