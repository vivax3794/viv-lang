from arpeggio import visit_parse_tree

from parser import parser
from interpritter import Visitor


with open("test.viv") as f:
    code = f.read()


print("[PARSING CODE]")
parse_tree = parser.parse(code)

print("[RUNNING CODE]")
tree = visit_parse_tree(parse_tree, Visitor(debug=False))
