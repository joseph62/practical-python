class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, row):
        """
        Emit a single row of table data
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for heading in headers:
            print(f"{heading:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, row):
        for column in row:
            print(f"{column:>10s}", end=" ")
        print()


class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, row):
        print(",".join(row))


class HtmlTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="")
        for heading in headers:
            print(f"<th>{heading}</th>", end="")
        print("</tr>")

    def row(self, row):
        print("<tr>", end="")
        for column in row:
            print(f"<td>{column}</td>", end="")
        print("</tr>")
