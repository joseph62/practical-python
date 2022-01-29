# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
from tableformat import get_formatter


def read_portfolio(filename, silence_errors=False):
    columns = ["name", "shares", "price"]
    return Portfolio(
        [
            Stock(**s)
            for s in parse_csv(
                filename,
                select=columns,
                types=[str, int, float],
                silence_errors=silence_errors,
            )
            if all(column in s for column in columns)
        ]
    )


def read_prices(filename):
    return dict(parse_csv(filename, types=[str, float], has_headers=False))


def can_i_retire(portfolio_filename, prices_filename):
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
            position.name,
            position.shares,
            prices[position.name],
            prices[position.name] - position.price,
        )
        for position in portfolio
    ]


def display_report_with_f_string(
    report, headers=("Name", "Shares", "Price", "Change"), column_size=10
):
    print(" ".join(f"{h:>10}" for h in headers))
    print(" ".join(["-" * column_size] * len(headers)))
    for name, shares, price, change in report:
        price = f"${price:.2f}"
        print(f"{name:>10} {shares:>10d} {price:>10} {change:>10.2f}")


def display_report(report, formatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        formatter.row([name, str(shares), f"{price:0.2f}", f"{change:0.2f}"])


def portfolio_report(portfolio_file, prices_file, fmt="txt"):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    report = make_report(portfolio, prices)

    formatter = get_formatter(fmt)

    display_report(report, formatter)


def main(argv):
    if len(argv) == 4:
        _, portfolio_filename, price_filename, fmt = argv
    elif len(argv) == 3:
        _, portfolio_filename, price_filename = argv
        fmt = "txt"
    else:
        portfolio_filename = "Data/portfolio.csv"
        price_filename = "Data/prices.csv"
        fmt = "txt"

    with (
        open(portfolio_filename) as portfolio_file,
        open(price_filename) as price_file,
    ):
        portfolio_report(portfolio_file, price_file, fmt=fmt)


if __name__ == "__main__":
    import sys

    main(sys.argv)
