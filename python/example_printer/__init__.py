import gdb

## https://www.ece.villanova.edu/VECR/doc/gdb/Types-In-Python.html#Types-In-Python
## https://www.ece.villanova.edu/VECR/doc/gdb/Pretty-Printing-API.html#Pretty-Printing-API

class chess_board_printer:
    """print a chess_board object."""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return (str(self.val.type.tag) + "("+str(self.val["size_"])+"x"+str(self.val["size_"])+")")


def build_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("example")
    pp.add_printer('chess_board', '^chess_board$', chess_board_printer)
    return pp