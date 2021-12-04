# pcost.py
#
# Exercise 1.27

import sys


def portfolio_cost(filename):
    with open(filename) as f:
        keys = [key.strip() for key in next(f).split(",")]
        rows = []
        for row in f:
            rows.append({key: col.strip() for key, col in zip(keys, row.split(","))})

    total = 0

    for row in rows:
        symbol = row["name"]
        try:
            total += int(row["shares"]) * float(row["price"])
        except ValueError:
            print(f"Warning! Unable to parse shares or price for {symbol!r}")

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

total_cost = portfolio_cost(filename)

print(f"Total cost ${total_cost:0.2f}")
