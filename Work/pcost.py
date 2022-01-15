# pcost.py
#
# Exercise 1.27

from report import read_portfolio


def portfolio_cost(filename):
    with open(filename, "rt") as f:
        portfolio = read_portfolio(f)

    return sum(position.cost() for position in portfolio)


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
