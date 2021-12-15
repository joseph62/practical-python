# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
            try:
                holding['shares'] = int(holding['shares'])
                holding['price'] = float(holding['price'])
                portfolio.append(
                    holding
                )
            except ValueError:
                print("Warning! Failed to parse shares or price for symbol", symbol)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, "rt") as f:
        for row in csv.reader(f):
            if row:
                name, price = row
                prices[name] = float(price)
    return prices


def can_i_retire(portfolio_filename, prices_filename, retirement_target=100_000_000):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    total_unrealized_gains_or_losses = []

    for position in portfolio:
        purchase = position["shares"] * position["price"]
        current_value = position["shares"] * prices[position["name"]]
        total_unrealized_gains_or_losses.append(
            (position["name"], purchase, current_value, current_value - purchase)
        )

    return (
        total_unrealized_gains_or_losses,
        sum(
            gain_or_loss
            for name, p, cv, gain_or_loss in total_unrealized_gains_or_losses
        ),
    )


def make_report(portfolio, prices):
    return [
        (
            position["name"],
            position["shares"],
            prices[position["name"]],
            prices[position["name"]] - position["price"],
        )
        for position in portfolio
    ]


def display_report_with_f_string(report):
    headers = ("Name", "Shares", "Price", "Change")
    print(" ".join(f"{h:>10}" for h in headers))
    print(" ".join(["-" * 10] * 4))
    for name, shares, price, change in report:
        price = f"${price:.2f}"
        print(f"{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}")


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
display_report_with_f_string(report)
