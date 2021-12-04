# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for symbol, shares, price in rows:
            try:
                portfolio.append((symbol, int(shares), float(price)))
            except ValueError:
                print("Warning! Failed to parse shares or price for symbol", symbol)
