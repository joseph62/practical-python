# pcost.py
#
# Exercise 1.27

from report import read_portfolio


def portfolio_cost(filename):
    with open(filename, "rt") as f:
        portfolio = read_portfolio(f)

    total = 0

    for row_number, row in enumerate(portfolio, start=1):
        try:
            total += row["shares"] * row["price"]
        except ValueError:
            print(f"Row {row_number}: Bad row: {row}")

    return total


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"

    total_cost = portfolio_cost(filename)

    print(f"Total cost ${total_cost:0.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
