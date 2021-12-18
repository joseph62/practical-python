# fileparse.py
#
# Exercise 3.3

import csv

def make_converter(types):
    if types:
        return lambda row: (type_(row) for type_, row in zip(types, row))
    else:
        return lambda row: row

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
                column for header, column in zip(headers, row) if selector(header)
            )
            for row in rows if row
        )
        return [dict(zip(headers, row)) for row in rows]
    return mapper

def make_headerless_mapper(converter): # Does not have header
    def mapper(rows):
        return [tuple(converter(row)) for row in rows if row]
    return mapper


def make_mapper(types, select, has_headers):
    if select and not has_headers:
        raise ValueError("Cannot select columns without headers")
    converter = make_converter(types)
    selector = make_selector(select)
    if has_headers:
        return make_mapper_with_header(converter, selector)
    else:
        return make_headerless_mapper(converter)


def parse_csv(filename, types=(), select=(), has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of records
    """
    mapper = make_mapper(types, select, has_headers)
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        return mapper(rows)