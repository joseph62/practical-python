import stock
import fileparse


class Portfolio:
    def __init__(self):
        self._holdings = []

    def __iter__(self):
        return iter(self._holdings)

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)

    def append(self, s):
        if not isinstance(s, stock.Stock):
            raise TypeError("Expected a Stock instance")
        self._holdings.append(s)

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares

    @classmethod
    def from_csv(cls, lines, **opts):
        columns = ["name", "shares", "price"]
        self = cls()
        portdicts = fileparse.parse_csv(
            lines, select=columns, types=[str, int, float], **opts
        )
        for d in portdicts:
            if all(column in d for column in columns):
                self.append(stock.Stock(**d))
        return self
