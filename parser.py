from arpeggio import RegExMatch, OneOrMore
from arpeggio import ParserPython


# abstract
def word():         return RegExMatch(r"\w+")


# types
def number():           return RegExMatch(r"\d+")
def string():           return RegExMatch(r'"(.*?)"')

def type_():            return [string, number]

# expressions
def var():              return word
def function_call():    return var, "{", expression, "}"

def expression():       return [type_, function_call, var]


# statements
def asginment():        return word, "<-", expression

def statement():        return [asginment, expression], ";"



# top node
def program():          return OneOrMore(statement)


print("[READING RULES]")
parser = ParserPython(program, debug=True)
