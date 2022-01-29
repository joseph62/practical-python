from follow import follow
from tableformat import get_formatter
import csv
import report


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [f(val) for f, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, symbols):
    for row in rows:
        if row["name"] in symbols:
            yield row


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
