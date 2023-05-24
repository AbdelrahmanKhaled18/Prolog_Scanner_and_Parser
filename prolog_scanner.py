from enum import Enum
import re


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


class Token:
    def __init__(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type

    def to_dict(self):
        return {
            "Lex": self.lex,
            "token_type": self.token_type
        }


class Scanner:
    def __init__(self, text):
        self.tokens = self.find_tokens(text)
        self.current_token_index = 0

    def get_next_token(self):
        if self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            self.current_token_index += 1
            return token

    def find_tokens(self, text):
        Tokens = []  # to add tokens to list
        lines = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", text)
        inside_comment = False

        for line in lines.split('\n'):
            if '*/' in line and inside_comment:
                inside_comment = False
                continue
            if inside_comment:
                continue
            if '/*' in line:
                inside_comment = True
                continue
            words = re.findall(
                r'[0-9]*[a-zA-Z_]+[0-9]*|[0-9]+(?:\.[0-9]*)?|\'[a-zA-Z0-9]?\'|"(?:\\.|[^"])*"|<=|>=|<|:-|>|.|<>|[(){};,'
                r':\[\]=+\-*/]',
                line)
            for word in words:
                if word == " ":
                    continue
                elif word in ReservedWords:
                    Tokens.append(Token(word, ReservedWords[word]))
                elif word in Operators:
                    if word == "<=" or word == ">=" or word == "<>" or word == "<" or word == ">" or word == "=":
                        Tokens.append(Token(word, Token_type.Relational_op))
                    elif word == "+" or word == "-" or word == "*" or word == "/":
                        Tokens.append(Token(word, Token_type.Arithmetic_op))
                    elif word == ",":
                        Tokens.append(Token(word, Token_type.And))
                    elif word == ";":
                        Tokens.append(Token(word, Token_type.Or))
                    elif word == ".":
                        Tokens.append(Token(word, Token_type.Dot))
                    elif word == "(":
                        Tokens.append(Token(word, Token_type.open_bracket))
                    elif word == ":-":
                        Tokens.append(Token(word, Token_type.imply))
                    else:
                        Tokens.append(Token(word, Token_type.close_bracket))
                elif re.match("^[a-z][a-zA-Z0-9_]*$", word):
                    Tokens.append(Token(word, Token_type.identifier))
                elif re.match("^[A-Z_][a-zA-Z0-9_]*$", word):
                    Tokens.append(Token(word, Token_type.variable))
                elif re.match("^([0-9]+)$", word):
                    Tokens.append(Token(word, Token_type.integer))
                elif re.match("^'[a-zA-Z0-9]?'$", word):
                    Tokens.append(Token(word, Token_type.char))
                elif re.match("^([0-9]+(.[0-9])?|.[0-9]+)$", word):
                    Tokens.append(Token(word, Token_type.real))
                elif word.startswith('"') and word.endswith('"'):
                    Tokens.append(Token(word, Token_type.string))
                else:
                    Tokens.append(Token(word, Token_type.error))
        return Tokens
