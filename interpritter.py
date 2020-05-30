from arpeggio import PTNodeVisitor


class Nothing:
    pass


class Visitor(PTNodeVisitor):
    __scope = {
            "say": print,
            "Nothing": Nothing
            }

    def visit_number(self, node, children):
        return int(node.value)

    def visit_string(self, node, children):
        return node.value

    def visit_type_(self, node, children):
        return children[0]

    def visit_word(self, node, children):
        return node.value

    def visit_var(self, node, children):
        return self.__scope[node.value]

    def visit_function_call(self, node, children):
        res = children[0](*children[1:])
        if res is None:
            return Nothing()
        else:
            return res


    def visit_expression(self, node, children):
        return children[0]

    def visit_asginment(self, node, children):
        self.__scope[children[0]] = children[1]
        return None

    def visit_statment(self, node, children):
        return None

    def visit_program(self, node, children):
        return None
