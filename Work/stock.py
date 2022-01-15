class Stock:
    def __init__(self, name, shares, price):
        if shares <= 0:
            raise ValueError("Cannot have a stock with zero or negative shares!")

        if price <= 0:
            raise ValueError("Cannot have a stock purchased at zero or negative price!")

        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares_to_sell):
        if shares_to_sell <= 0:
            raise ValueError(
                f"Cannot sell zero or negative shares of stock {self.name}"
            )

        if shares_to_sell > self.shares:
            raise ValueError(
                f"Cannot sell {shares_to_sell} shares of {self.name}! There are only {self.shares} shares of {self.name} available to sell."
            )

        self.shares -= shares_to_sell

    def __str__(self):
        return f"Stock({self.name} {self.shares}@{self.price:0.2f})"

    __repr__ = __str__
