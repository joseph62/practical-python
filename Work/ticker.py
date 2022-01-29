from follow import follow
from tableformat import get_formatter
import csv
import report


def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)


def convert_types(rows, types):
    return ([f(val) for f, val in zip(types, row)] for row in rows)


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, symbols):
    return (row for row in rows if row["name"] in symbols)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfolio_filename, stocklog_filename, format):
    with open(portfolio_filename) as f:
        portfolio = report.read_portfolio(f)
    lines = follow(stocklog_filename)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = get_formatter(format)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row((row["name"], row["price"], row["change"]))


if __name__ == "__main__":
    ticker("Data/portfolio.csv", "Data/stocklog.csv", "txt")
