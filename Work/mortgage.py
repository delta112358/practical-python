# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 5*12+1
extra_payment_end_month = (extra_payment_start_month-1) + 4*12
extra_payment = 1000
current_month = 1
while principal > 0:
    principal = principal * (1+rate/12)
    cond1 = current_month >= extra_payment_start_month
    cond2 = current_month <= extra_payment_end_month
    if cond1 and cond2:
        payment_month = payment + extra_payment
    else:
        payment_month = payment

    if payment_month > principal:
        payment_month = principal

    principal     -= payment_month
    total_paid    += payment_month
    current_month += 1
    print(current_month, round(total_paid,2),round(principal,2))
print("Total paid ", round(total_paid,2))
print("Months", current_month)