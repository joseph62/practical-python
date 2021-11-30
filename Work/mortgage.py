# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_of_payments = 0
extra_payment = 1_000
extra_payment_start_month = 60
extra_payment_end_month = 108


def month_in_range(month):
    return month >= extra_payment_start_month and month < extra_payment_end_month


while principal > 0:
    total_payment = (
        (payment + extra_payment) if month_in_range(number_of_payments) else payment
    )
    principal = principal * (1 + rate / 12)
    if total_payment > principal:
        total_payment = principal
    principal = round(principal - total_payment, ndigits=2)
    total_paid = total_paid + total_payment
    number_of_payments += 1
    print(
        f"{number_of_payments:<5} {total_paid:10.2f} {total_payment:10.2f} {principal:10.2f}"
    )


print(f"Total paid {total_paid:0.2f}")
print("Total monthly payments", number_of_payments)
