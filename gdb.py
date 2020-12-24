## import sys
## sys.path.insert(0, '/data/htdocs/src/github.com/terrywh/gdb-pretty-printer/python')

import gdb
import example_printer

gdb.printing.register_pretty_printer(gdb.current_objfile(), example_printer.build_printer())