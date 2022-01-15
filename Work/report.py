# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):
    return parse_csv(
        filename, select=["name", "shares", "price"], types=[str, int, float]
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
            position["name"],
            position["shares"],
            prices[position["name"]],
            prices[position["name"]] - position["price"],
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


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    display_report_with_f_string(report)


def main(argv):
    if len(argv) == 3:
        portfolio_filename = argv[1]
        price_filename = argv[2]
    else:
        portfolio_filename = "Data/portfolio.csv"
        price_filename = "Data/prices.csv"

    portfolio_report(portfolio_filename, price_filename)


if __name__ == "__main__":
    import sys

    main(sys.argv)
