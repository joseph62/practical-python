import os
import time
import sys
import report


def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


def main(argv):
    filename = "Data/stocklog.csv"
    portfolio_filename = "Data/portfolio.csv"

    with open(portfolio_filename) as f:
        portfolio = report.read_portfolio(f)

    print("Following", filename)
    for line in follow(filename):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")


if __name__ == "__main__":
    main(sys.argv)
