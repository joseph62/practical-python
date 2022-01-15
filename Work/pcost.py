# pcost.py
#
# Exercise 1.27

import sys

from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)

    total = 0

    for row_number, row in enumerate(portfolio, start=1):
        try:
            total += row["shares"] * row["price"]
        except ValueError:
            print(f"Row {row_number}: Bad row: {row}")

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

total_cost = portfolio_cost(filename)

print(f"Total cost ${total_cost:0.2f}")
