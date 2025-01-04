from enum import Enum


class Token_type(Enum):
    predicates = 1
    clauses = 2
    goal = 3
    data_type_integer = 4
    data_type_string = 5
    data_type_char = 6
    data_type_symbol = 7
    data_type_real = 8
    integer = 9
    string = 10
    char = 11
    real = 12
    And = 13
    Or = 14
    readln = 15
    readint = 16
    readchar = 17
    write = 18
    Comma = 19
    Relational_op = 20
    Arithmetic_op = 21
    Dot = 22
    identifier = 23
    open_bracket = 24
    close_bracket = 25
    variable = 26
    imply = 27
    new_line = 28
    error = 29


class Token:
    def __init__(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type

    def to_dict(self):
        return {
            "Lex": self.lex,
            "token_type": self.token_type
        }


ReservedWords = {
    "predicates": Token_type.predicates,
    "clauses": Token_type.clauses,
    "goal": Token_type.goal,
    "readln": Token_type.readln,
    "readint": Token_type.readint,
    "readchar": Token_type.readchar,
    "write": Token_type.write,
    "integer": Token_type.data_type_integer,
    "symbol": Token_type.data_type_symbol,
    "char": Token_type.data_type_char,
    "string": Token_type.data_type_string,
    "real": Token_type.data_type_real,
}

Operators = {
    "<": Token_type.Relational_op,
    "<=": Token_type.Relational_op,
    ">": Token_type.Relational_op,
    ">=": Token_type.Relational_op,
    "=": Token_type.Relational_op,
    "<>": Token_type.Relational_op,
    "+": Token_type.Arithmetic_op,
    "-": Token_type.Arithmetic_op,
    "*": Token_type.Arithmetic_op,
    "/": Token_type.Arithmetic_op,
    ",": Token_type.And,
    ";": Token_type.Or,
    ".": Token_type.Dot,
    "(": Token_type.open_bracket,
    ")": Token_type.close_bracket,
    ":-": Token_type.imply
}
