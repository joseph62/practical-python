# fileparse.py
#
# Exercise 3.3

import csv


def error_reporting_callback(row, index, error):
    print(f"Row {index}: Couldn't convert {row}")
    print(f"Row {index}: Reason {error}")


def noop_error_reporting_callback(row, index, error):
    pass


def make_converter(types, error_callback):
    def convert_with_types(row, index):
        for type_, column in zip(types, row):
            try:
                yield type_(column)
            except ValueError as e:
                error_callback(row, index, e)

    if types:
        return convert_with_types
    else:
        return lambda row, _: row


def make_selector(select):
    if select:
        return lambda header: header in select
    else:
        return lambda _: True


def make_mapper_with_header(converter, selector):
    def mapper(rows):
        headers = next(rows)
        rows = (
            converter(
                (column for header, column in zip(headers, row) if selector(header)),
                index,
            )
            for index, row in enumerate(rows, start=1)
            if row
        )
        return [dict(zip(headers, row)) for row in rows]

    return mapper


def make_headerless_mapper(converter):  # Does not have header
    def mapper(rows):
        return [
            tuple(converter(row, index))
            for index, row in enumerate(rows, start=1)
            if row
        ]

    return mapper


def make_mapper(types, select, has_headers, silence_errors):
    if select and not has_headers:
        raise ValueError("Cannot select columns without headers")
    error_callback = (
        noop_error_reporting_callback if silence_errors else error_reporting_callback
    )
    converter = make_converter(types, error_callback)
    selector = make_selector(select)
    if has_headers:
        return make_mapper_with_header(converter, selector)
    else:
        return make_headerless_mapper(converter)


def parse_csv(
    file, types=(), select=(), has_headers=True, silence_errors=False, delimiter=","
):
    """
    Parse a CSV file into a list of records
    """
    mapper = make_mapper(types, select, has_headers, silence_errors)
    rows = csv.reader(file, delimiter=delimiter)
    return mapper(rows)
