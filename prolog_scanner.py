import re
from prolog_tokens import Token, Token_type, ReservedWords, Operators


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
        lines = re.sub(re.compile(r"/\*.*?\*/", re.DOTALL), "", text)
        lines = re.sub(re.compile(r"//.*?$", re.MULTILINE), "", lines)
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
                r"[0-9]*[a-zA-Z_]+[0-9]*|[0-9]+(?:\.[0-9]+)?|'[a-zA-Z0-9]?'|\"(?:\\.|[^\"])*\"|<=|>=|<|:-|>|\.|<>|[(){};,\[\]=+\-*/]",
                line)
            for word in words:
                if word.strip() == "":
                    continue
                elif word in ReservedWords:
                    Tokens.append(Token(word, ReservedWords[word]))
                elif word in Operators:
                    Tokens.append(Token(word, Operators[word]))
                elif re.match(r"^[a-z][a-zA-Z0-9_]*$", word):
                    Tokens.append(Token(word, Token_type.identifier))
                elif re.match(r"^[A-Z_][a-zA-Z0-9_]*$", word):
                    Tokens.append(Token(word, Token_type.variable))
                elif re.match(r"^[0-9]+$", word):
                    Tokens.append(Token(word, Token_type.integer))
                elif re.match(r"^'[a-zA-Z0-9]?'$", word):
                    Tokens.append(Token(word, Token_type.char))
                elif re.match(r"^[0-9]+(\.[0-9]+)?$", word):
                    Tokens.append(Token(word, Token_type.real))
                elif word.startswith('"') and word.endswith('"'):
                    Tokens.append(Token(word, Token_type.string))
                else:
                    Tokens.append(Token(word, Token_type.error))
        return Tokens
