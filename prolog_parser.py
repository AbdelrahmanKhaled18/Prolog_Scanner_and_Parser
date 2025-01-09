from prolog_scanner import *
from nltk.tree import *


class Parser:
    def __init__(self, scanner: Scanner):
        """
        Initialize the parser with a scanner instance.
        """
        self.scanner = scanner
        self.current_token = None
        self.dict_identifiers = dict()
        self.dict_variables = dict()
        self.error_list = []
        self.Nodes = []
        self.section = ''

    def parse(self) -> Tree:
        """
        Parse the input and return the parse tree.
        """
        self.advance()
        return self.program()

    def advance(self):
        """
        Advance to the next token.
        """
        self.current_token = self.scanner.get_next_token()

    def add_node(self, node, loc0=None, loc1=None):
        """
        Add a node to the parse tree.
        """
        if loc1 is None:
            if loc0 is None:
                self.Nodes.append(node)
            else:
                self.Nodes[loc0].append(node)
        else:
            self.Nodes[loc0][loc1].append(node)

    def error_found(self, loc0=None, loc1=None):
        """
        Handle errors by adding them to the error list and advancing the token.
        """
        self.error_list.append(f"Error at token: {self.current_token.lex} of type {self.current_token.token_type}")
        self.add_node('Error', loc0, loc1)
        self.skip_to_next_valid_token()

    def skip_to_next_valid_token(self):
        """
        Skip tokens until a valid token is found based on the current section.
        """
        if self.section == 'predicates':
            while self.current_token and self.current_token.token_type not in {Token_type.identifier,
                                                                               Token_type.clauses}:
                self.advance()
        elif self.section == 'clauses':
            while self.current_token and self.current_token.token_type not in {Token_type.Dot, Token_type.goal}:
                self.advance()
        elif self.section == 'goal':
            while self.current_token:
                self.advance()
        if self.current_token and self.current_token.token_type == Token_type.Dot:
            self.advance()

    def consume(self, expected_token_type, node=None, loc0=None, loc1=None) -> bool:
        """
        Consume the current token if it matches the expected token type.
        """
        if self.current_token and self.current_token.token_type == expected_token_type:
            if node:
                self.add_node(node, loc0, loc1)
            self.advance()
            return True
        else:
            self.error_found(loc0, loc1)
            return False

    def program(self) -> Tree:
        """
        Parse the entire program.
        """
        self.section = 'predicates'
        self.section_predicates()
        self.section = 'clauses'
        self.section_clauses()
        self.section = 'goal'
        self.section_goal()
        return self.display_parse_tree()

    def section_predicates(self):
        """
        Parse the predicates section.
        """
        if self.consume(Token_type.predicates, 'Predicates'):
            self.add_node(['predicates'])
        while self.current_token and self.current_token.token_type != Token_type.clauses:
            self.predicate_declaration()

    def predicate_declaration(self):
        """
        Parse a predicate declaration.
        """
        predicate_name = self.current_token.lex
        self.dict_identifiers[predicate_name] = []
        if self.consume(Token_type.identifier, 'Predicate Declaration', 1):
            self.add_node(['Predicate ID'], 1)
        if self.current_token and self.current_token.token_type == Token_type.open_bracket:
            self.parameter_list(predicate_name)

    def parameter_list(self, predicate_name):
        """
        Parse a parameter list.
        """
        self.consume(Token_type.open_bracket, '(', 1, -1)
        self.data_type(predicate_name)
        while self.current_token and self.current_token.token_type == Token_type.And:
            self.consume(Token_type.And, ',', 1, -1)
            self.data_type(predicate_name)
        self.consume(Token_type.close_bracket, ')', 1, -1)

    def data_type(self, predicate_name):
        """
        Parse a data type.
        """
        data_types = [
            Token_type.data_type_integer,
            Token_type.data_type_symbol,
            Token_type.data_type_char,
            Token_type.data_type_string,
            Token_type.data_type_real
        ]
        if self.current_token.token_type in data_types:
            self.dict_identifiers[predicate_name].append(self.current_token.token_type)
            self.consume(self.current_token.token_type, 'Data Type', 1, -1)
        else:
            self.error_found(1, -1)

    def section_clauses(self):
        """
        Parse the clauses section.
        """
        if self.consume(Token_type.clauses, 'Clauses'):
            self.add_node(['clauses'])
        while self.current_token and self.current_token.token_type != Token_type.goal:
            clause_ident = self.current_token.lex
            if clause_ident not in self.dict_identifiers:
                self.error_found(3)
                continue
            self.consume(Token_type.identifier)
            if self.current_token.token_type == Token_type.open_bracket:
                self.add_node('Fact', 3)
                self.add_node(['Predicate ID'], 3)
                self.value_list(clause_ident)
            elif self.current_token.token_type == Token_type.imply:
                if self.dict_identifiers[clause_ident]:
                    self.error_found(3)
                else:
                    self.add_node('Rule', 3)
                    self.add_node(['Predicate ID'], 3)
                    self.body()
            else:
                if self.consume(Token_type.Dot):
                    self.add_node('Fact', 3)
                    self.add_node(['Predicate ID', '.'], 3)

    def value_list(self, clause_ident):
        """
        Parse a value list.
        """
        self.consume(Token_type.open_bracket, '(', 3, -1)
        value_list = [self.values()]
        while self.current_token.token_type == Token_type.And:
            self.consume(Token_type.And, ',', 3, -1)
            value_list.append(self.values())
        if value_list != self.dict_identifiers[clause_ident]:
            self.error_found(3, -1)
        self.consume(Token_type.close_bracket, ')', 3, -1)
        self.consume(Token_type.Dot, '.', 3, -1)

    def values(self):
        """
        Parse values.
        """
        values = [
            Token_type.integer,
            Token_type.identifier,
            Token_type.char,
            Token_type.string,
            Token_type.real
        ]
        if self.current_token.token_type in values:
            temp = self.current_token.token_type
            if self.section == 'clauses':
                self.consume(self.current_token.token_type, 'Value', 3, -1)
            elif self.section == 'goal':
                self.consume(self.current_token.token_type, 'Value', 5)
            return temp
        else:
            if self.section == 'clauses':
                self.error_found(3, -1)
            elif self.section == 'goal':
                self.error_found(5)

    def body(self):
        """
        Parse the body of a rule.
        """
        self.consume(Token_type.imply, ':-', 3, -1)
        while True:
            if self.current_token.token_type == Token_type.And:
                self.consume(Token_type.And, ',', 3, -1)
            elif self.current_token.token_type == Token_type.Or:
                self.consume(Token_type.Or, ';', 3, -1)
            if self.current_token.token_type == Token_type.write:
                self.write()
            elif self.current_token.token_type == Token_type.readln:
                self.readln()
            elif self.current_token.token_type == Token_type.readint:
                self.readint()
            elif self.current_token.token_type == Token_type.readchar:
                self.readchar()
            elif self.current_token.token_type == Token_type.variable:
                self.statements()
            if self.current_token.token_type not in {Token_type.And, Token_type.Or}:
                break
        self.consume(Token_type.Dot, '.', 3, -1)

    def write(self):
        """
        Parse a write statement.
        """
        self.consume(Token_type.write, 'write statement', 3, -1)
        write_list = ['write']
        if self.consume(Token_type.open_bracket):
            write_list.append('(')
        while True:
            if self.current_token.token_type == Token_type.string:
                if self.consume(Token_type.string):
                    write_list.append('string')
            elif self.current_token.token_type == Token_type.variable:
                if self.current_token.lex not in self.dict_variables:
                    self.error_found(3)
                    break
                if self.dict_variables[self.current_token.lex] != Token_type.integer:
                    self.error_found(3)
                    break
                if self.consume(Token_type.variable):
                    write_list.append('Variable')
            if self.current_token.token_type == Token_type.And:
                if self.consume(Token_type.And):
                    write_list.append(',')
            elif self.current_token.token_type == Token_type.close_bracket:
                break
            else:
                self.error_found(3)
        if self.consume(Token_type.close_bracket):
            write_list.append(')')
        self.add_node(write_list, 3, -1)

    def readln(self):
        """
        Parse a readln statement.
        """
        self.consume(Token_type.readln, 'read statement', 3, -1)
        read_list = ['readln']
        if self.consume(Token_type.open_bracket):
            read_list.append('(')
        if self.current_token.lex in self.dict_variables:
            self.error_found(3)
        else:
            self.dict_variables[self.current_token.lex] = Token_type.string
            if self.consume(Token_type.variable):
                read_list.append('Variable')
            if self.consume(Token_type.close_bracket):
                read_list.append(')')
            self.add_node(read_list, 3, -1)

    def readint(self):
        """
        Parse a readint statement.
        """
        self.consume(Token_type.readint, 'read statement', 3, -1)
        read_list = ['readint']
        if self.consume(Token_type.open_bracket):
            read_list.append('(')
        if self.current_token.lex in self.dict_variables:
            self.error_found(3)
        else:
            self.dict_variables[self.current_token.lex] = Token_type.integer
        if self.consume(Token_type.variable):
            read_list.append('Variable')
        if self.consume(Token_type.close_bracket):
            read_list.append(')')
        self.add_node(read_list, 3, -1)

    def readchar(self):
        """
        Parse a readchar statement.
        """
        self.consume(Token_type.readchar, 'read statement', 3, -1)
        read_list = ['readchar']
        if self.consume(Token_type.open_bracket):
            read_list.append('(')
        if self.current_token.lex in self.dict_variables:
            self.error_found(3)
        else:
            self.dict_variables[self.current_token.lex] = Token_type.char
        if self.consume(Token_type.variable):
            read_list.append('Variable')
        if self.consume(Token_type.close_bracket):
            read_list.append(')')
        self.add_node(read_list, 3, -1)

    def statements(self):
        """
        Parse statements.
        """
        type_list = []
        statement_list = []
        flag = False
        while True:
            if self.current_token.token_type == Token_type.integer:
                type_list.append(Token_type.integer)
                self.consume(Token_type.integer)
                statement_list.append('integer')
            elif self.current_token.token_type == Token_type.real:
                type_list.append(Token_type.real)
                self.consume(Token_type.real)
                statement_list.append('real')
            elif self.current_token.token_type == Token_type.char:
                type_list.append(Token_type.char)
                self.consume(Token_type.char)
                statement_list.append('char')
            elif self.current_token.token_type == Token_type.string:
                type_list.append(Token_type.string)
                self.consume(Token_type.string)
                statement_list.append('string')
            elif self.current_token.lex not in self.dict_variables:
                self.error_found(3)
            else:
                type_list.append(self.dict_variables[self.current_token.lex])
                self.consume(Token_type.variable)
                statement_list.append('Variable')

            if not flag:
                if self.current_token.token_type not in {Token_type.Relational_op, Token_type.Arithmetic_op}:
                    self.error_found(3)
                else:
                    statement_list.append(self.current_token.lex)
                    if self.current_token.token_type == Token_type.Relational_op:
                        flag = True
                        self.consume(Token_type.Relational_op)
                    elif self.current_token.lex == "=":
                        flag = True
                        self.consume(Token_type.Arithmetic_op)
                    else:
                        self.consume(Token_type.Arithmetic_op)
            else:
                if self.current_token.token_type == Token_type.Relational_op or self.current_token.lex == "=":
                    self.error_found(3)
                elif self.current_token.token_type == Token_type.Arithmetic_op:
                    statement_list.append(self.current_token.lex)
                    self.consume(Token_type.Arithmetic_op)
                elif self.current_token.token_type in {Token_type.And, Token_type.Or}:
                    break
                else:
                    self.error_found(3)

        if len(set(type_list)) != 1:
            self.error_found(3)
        self.add_node('Statement', 3, -1)
        self.add_node(statement_list, 3, -1)

    def section_goal(self):
        """
        Parse the goal section.
        """
        if self.consume(Token_type.goal, 'Goal'):
            self.add_node(['goal'])
        goal_ident = self.current_token.lex
        if goal_ident not in self.dict_identifiers:
            self.error_found(5)
        self.consume(Token_type.identifier, 'Predicate ID', 5)
        if self.current_token.token_type == Token_type.open_bracket:
            self.value_list(goal_ident)
        elif self.dict_identifiers[goal_ident]:
            self.error_found(5)
        self.consume(Token_type.Dot, '.', 5)
        if self.current_token:
            self.error_found(5)

    def goal_value(self, goal_ident):
        """
        Parse goal values.
        """
        self.consume(Token_type.open_bracket, '(', 5)
        value_list = [self.values()]
        while self.current_token.token_type == Token_type.And:
            self.consume(Token_type.And, ',', 5)
            value_list.append(self.values())
        self.consume(Token_type.close_bracket, ')', 5)
        if value_list != self.dict_identifiers[goal_ident]:
            self.error_found(5)

    def display_parse_tree(self) -> Tree:
        """
        Display the parse tree.
        """
        parse_tree = Tree('Program', [])
        self.build_parse_tree(parse_tree, self.Nodes)
        return parse_tree

    def build_parse_tree(self, parent: Tree, nodes_list: list):
        """
        Build the parse tree recursively.
        """
        while nodes_list:
            node = nodes_list.pop(0)
            if isinstance(node, str):
                item = Tree(node, [])
                parent.append(item)
            elif isinstance(node, list):
                new_parent = parent[-1]
                self.build_parse_tree(new_parent, node)
