import argparse
from math import log
from math import ceil
from math import pow


def mth_diff_payment(p, n, i, m):
    return ceil((p / n) + i * (p - p * (m - 1) / n))


def overpayment(payment, periods, principal):
    return ceil(payment * periods - principal)


def annuity_payment(principal, payment, periods, interest):
    i = (float(interest) / 12) / 100
    union = "and "

    if periods == None:
        periods = ceil(log(payment / (payment - i * principal), 1 + i))
        months = periods % 12
        years = periods // 12

        if months * years == 0:
            union = ""

        if years == 1:
            years = f" {years} year"
        elif years > 1:
            years = f" {years} years"

        if months == 1:
            months = f"{months} month "
        elif months > 1:
            months = f"{months} months "

        if years == 0:
            years = ""
        if months == 0:
            months = ""
        print(f"It will take{years} {union}{months}to repay this loan!")
    elif payment == None:
        payment = ceil(principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
        print(f"Your monthly payment = {payment}!")
    elif principal == None:
        principal = ceil(payment / ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1)))
        print(f"Your loan principal = {principal}!")

    print("Overpayment = ", overpayment(payment, periods, principal))


def differentiate_payment(principal, periods, interest):
    i = (interest / 12) / 100
    current_mth = 1
    payments = payment = 0.0
    while current_mth <= periods:
        payment = mth_diff_payment(principal, periods, i, current_mth)
        print("Month ", current_mth, ": payment is ", ceil(payment))
        payments += payment
        current_mth += 1
    print("Overpayment = ", ceil(payments - principal))


parser = argparse.ArgumentParser(description="This program is loan calculator.")
parser.add_argument("-t", "--type", type=str)
parser.add_argument("-a", "--payment", type=int)
parser.add_argument("-p", "--principal", type=int)
parser.add_argument("-n", "--periods", type=int)
parser.add_argument("-i", "--interest", type=float)

args = parser.parse_args()
alist = list()

for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))

if args.interest is None or args.type not in ("diff", "annuity") or len(alist) != 4:
    print("Incorrect parameters.")
else:
    if args.type == "diff":
        differentiate_payment(args.principal, args.periods, args.interest)
    else:
        annuity_payment(args.principal, args.payment, args.periods, args.interest)
