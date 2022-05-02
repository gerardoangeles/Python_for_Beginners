import sys
import argparse
import math


def get_args_values():
    _type = args.type
    payment = args.payment
    principal = args.principal
    periods = args.periods
    interest = args.interest


def set_args_values():
    args.type = None
    args.payment = None
    args.periods = None
    args.interest = None
    args.principal = None


def type_diff_calc_overpayment():
    suma = 0
    for m in range(1, n + 1):
        dp = P / n + i * (P - (P * (m - 1) / n))
        dp = math.ceil(dp)
        suma += dp
        print(f"Month {m}: payment is {dp}")
    overpayment = suma - P
    print()
    print(f"Overpayment = {overpayment}")


def type_annuity_calc_overpayment():
    suma = 0
    for m in range(1, n + 1):
        dp = P / n + i * (P - (P * (m - 1) / n))
        dp = math.ceil(dp)
        suma += dp

    # Thank you to Moderator: aghogho monorien
    # Overpayment = annuity payment * n - principal
    overpayment = A * n - P
    print(f"Overpayment = {overpayment}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--type")
    parser.add_argument("--payment")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    parser.add_argument("--principal")

    args = parser.parse_args()
    get_args_values()

    MSG_WRONG_PARAMS = "Incorrect parameters."
    _payment = ""
    n = ""

    params = len(sys.argv)
    if params - 1 < 4:
        # Example 3: fewer than four arguments are given
        # python creditcalc.py --type=diff --principal=1000000 --payment=104000
        #
        # If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
        print(MSG_WRONG_PARAMS)
        set_args_values()
        exit()

    if args.type is None:
        # not specified at all
        # python creditcalc.py --principal=1000000 --periods=60 --interest=10
        print(MSG_WRONG_PARAMS)
        set_args_values()
        exit()

    if args.type == "diff" and args.payment is not None:
        # we can't calculate "months or principal", therefore a combination with --payment is invalid
        # python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
        print(MSG_WRONG_PARAMS)
        set_args_values()
        exit()

    if args.interest is None:
        # incorrect because --interest is missing
        # python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
        print(MSG_WRONG_PARAMS)
        set_args_values()
        exit()

    if args.periods is not None:
        if "-" in args.periods:  # or "-" in args.payment or "-" in args.principal or "-" in str(args.interest):
            # display an error message when negative values are entered
            # python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
            print(MSG_WRONG_PARAMS)
            set_args_values()
            exit()
        else:
            n = args.periods
            n = int(n)

    _interest = args.interest
    _interest = float(_interest)
    i = _interest / (12 * 100)

    if args.payment is not None:
        _payment = args.payment
        _payment = int(_payment)

    if args.principal is None:
        P = round((_payment * 12) / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
    else:
        P = args.principal
        P = int(P)

    if args.type == "diff":
        if args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
            # Example 1: calculating differentiated payments - Now let’s calculate the payment for each month:
            # python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
            #                     1) type     5) principal        3) periods   4) interest                        2) payment
            type_diff_calc_overpayment()

        if args.payment is not None and args.periods is not None and args.interest is not None and args.principal is None:
            # Example 4: calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%
            # python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
            #                     1) type     5) principal       3) periods  4) interest                        2) payment
            type_diff_calc_overpayment()

    if args.type == "annuity":
        if args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
            # Example 2: calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest
            # python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
            #                     1) type        5) principal        3) periods 4)   interest                       2) payment ?
            # Your annuity payment = 21248!
            # Overpayment = 274880
            A = math.ceil(P * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
            print(f"Your annuity payment = {A}!")
            type_annuity_calc_overpayment()

        if args.payment is not None and args.periods is not None and args.interest is not None and args.principal is None:
            # Example 5: calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest
            # python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
            #                     1) type        2) payment     3) periods   4) interest                    5) principal
            # Your loan principal = 800018!
            # Overpayment = 246622
            P = math.floor(math.ceil(_payment) / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
            print(f"Your loan principal = {P}!")
            A = math.ceil(P * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
            type_annuity_calc_overpayment()

        if args.principal is not None and args.payment is not None and args.interest is not None and args.periods is None:
            # Example 6: calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interes
            # python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
            #                     1) type        5) principal       2) payment      4) interest                   3) periods
            # It will take 2 years to repay this loan!
            # Overpayment = 52000

            # print("Enter the loan principal:", P)
            # print("Enter the monthly payment: ", _payment)
            A = float(_payment)
            # print("Enter the loan interest:", _interest)
            n = math.ceil(math.log(A / (A - i * P), 1 + i))
            # print("meses =", n)
            year = n // 12
            months = n % 12

            if year == 1 and months == 0:
                print(f"It will take a {year} year to repay this loan!")
            elif year > 1 and months == 0:
                print(f"It will take {year} years to repay this loan!")
            elif year > 1 and months == 1:
                print(f"It will take {year} years and {months} month to repay this loan!")
            else:
                print(f"It will take {year} years and {months} months to repay this loan!")

            type_annuity_calc_overpayment()
