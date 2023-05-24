import graphviz


def generate_dfa_res():
    dfa_reserved_words = graphviz.Digraph('dfa_reserved_words', format='png')

    dfa_reserved_words.attr('node', shape='doublecircle')
    dfa_reserved_words.attr('node', fixedsize='true')
    dfa_reserved_words.attr('node', width='1')
    dfa_reserved_words.attr('edge', shape='normal')

    dfa_reserved_words.node('start_reserved_words', shape='point', width='0')
    dfa_reserved_words.node('s0', shape='circle', width='1')
    dfa_reserved_words.node('s67', 's67: \nidentifier')
    dfa_reserved_words.edge('start_reserved_words', 's0', label='start')

    # Predicates
    dfa_reserved_words.node('s1', 's1: \nidentifier')
    dfa_reserved_words.node('s2', 's2: \nidentifier')
    dfa_reserved_words.node('s3', 's3: \nidentifier')
    dfa_reserved_words.node('s4', 's4: \nidentifier')
    dfa_reserved_words.node('s5', 's5: \nidentifier')
    dfa_reserved_words.node('s6', 's6: \nidentifier')
    dfa_reserved_words.node('s7', 's7: \nidentifier')
    dfa_reserved_words.node('s8', 's8: \nidentifier')
    dfa_reserved_words.node('s9', 's9: \nidentifier')
    dfa_reserved_words.node('s10', 's10: \npredicates')

    dfa_reserved_words.edge('s0', 's1', label='p')
    dfa_reserved_words.edge('s1', 's2', label='r')
    dfa_reserved_words.edge('s2', 's3', label='e')
    dfa_reserved_words.edge('s3', 's4', label='d')
    dfa_reserved_words.edge('s4', 's5', label='i')
    dfa_reserved_words.edge('s5', 's6', label='c')
    dfa_reserved_words.edge('s6', 's7', label='a')
    dfa_reserved_words.edge('s7', 's8', label='t')
    dfa_reserved_words.edge('s8', 's9', label='e')
    dfa_reserved_words.edge('s9', 's10', label='s')
    dfa_reserved_words.edge('s10', 's67', label='[a-zA-Z0-9]')

    # Goal
    dfa_reserved_words.node('s11', 's11: \nidentifier')
    dfa_reserved_words.node('s12', 's12: \nidentifier')
    dfa_reserved_words.node('s13', 's13: \nidentifier')
    dfa_reserved_words.node('s14', 's14: \ngoal')

    dfa_reserved_words.edge('s0', 's11', label='g')
    dfa_reserved_words.edge('s11', 's12', label='o')
    dfa_reserved_words.edge('s12', 's13', label='a')
    dfa_reserved_words.edge('s13', 's14', label='l')
    dfa_reserved_words.edge('s14', 's67', label='[a-zA-Z0-9]')

    # Clauses
    dfa_reserved_words.node('s15', 's15: \nidentifier')
    dfa_reserved_words.node('s16', 's16: \nidentifier')
    dfa_reserved_words.node('s17', 's17: \nidentifier')
    dfa_reserved_words.node('s18', 's18: \nidentifier')
    dfa_reserved_words.node('s19', 's19: \nidentifier')
    dfa_reserved_words.node('s20', 's20: \nidentifier')
    dfa_reserved_words.node('s21', 's21: \nclauses')

    dfa_reserved_words.edge('s0', 's15', label='c')
    dfa_reserved_words.edge('s15', 's16', label='l')
    dfa_reserved_words.edge('s16', 's17', label='a')
    dfa_reserved_words.edge('s17', 's18', label='u')
    dfa_reserved_words.edge('s18', 's19', label='s')
    dfa_reserved_words.edge('s19', 's20', label='e')
    dfa_reserved_words.edge('s20', 's21', label='s')
    dfa_reserved_words.edge('s21', 's67', label='[a-zA-Z0-9]')

    # read
    dfa_reserved_words.node('s22', 's22: \nidentifier')
    dfa_reserved_words.node('s23', 's23: \nidentifier')
    dfa_reserved_words.node('s24', 's24: \nidentifier')
    dfa_reserved_words.node('s25', 's25: \nread')

    dfa_reserved_words.edge('s0', 's22', label='r')
    dfa_reserved_words.edge('s22', 's23', label='e')
    dfa_reserved_words.edge('s23', 's24', label='a')
    dfa_reserved_words.edge('s24', 's25', label='d')
    dfa_reserved_words.edge('s25', 's67', label='[a-zA-Z0-9]')

    # readln
    dfa_reserved_words.node('s26', 's26: \nidentifier')
    dfa_reserved_words.node('s27', 's27: \nreadln')

    dfa_reserved_words.edge('s25', 's26', label='l')
    dfa_reserved_words.edge('s26', 's27', label='n')
    dfa_reserved_words.edge('s27', 's67', label='[a-zA-Z0-9]')

    # readint
    dfa_reserved_words.node('s28', 's28: \nidentifier')
    dfa_reserved_words.node('s29', 's29: \nidentifier')
    dfa_reserved_words.node('s30', 's30: \nreadint')

    dfa_reserved_words.edge('s25', 's28', label='i')
    dfa_reserved_words.edge('s28', 's29', label='n')
    dfa_reserved_words.edge('s29', 's30', label='t')
    dfa_reserved_words.edge('s30', 's67', label='[a-zA-Z0-9]')

    # readchar
    dfa_reserved_words.node('s31', 's31: \nidentifier')
    dfa_reserved_words.node('s32', 's32: \nidentifier')
    dfa_reserved_words.node('s33', 's33: \nidentifier')
    dfa_reserved_words.node('s34', 's34: \nreadchar')

    dfa_reserved_words.edge('s25', 's31', label='c')
    dfa_reserved_words.edge('s31', 's32', label='h')
    dfa_reserved_words.edge('s32', 's33', label='a')
    dfa_reserved_words.edge('s33', 's34', label='r')
    dfa_reserved_words.edge('s34', 's67', label='[a-zA-Z0-9]')

    # write
    dfa_reserved_words.node('s35', 's35: \nidentifier')
    dfa_reserved_words.node('s36', 's36: \nidentifier')
    dfa_reserved_words.node('s37', 's37: \nidentifier')
    dfa_reserved_words.node('s38', 's38: \nidentifier')
    dfa_reserved_words.node('s39', 's39: \nwrite')

    dfa_reserved_words.edge('s0', 's35', label='w')
    dfa_reserved_words.edge('s35', 's36', label='r')
    dfa_reserved_words.edge('s36', 's37', label='i')
    dfa_reserved_words.edge('s37', 's38', label='t')
    dfa_reserved_words.edge('s38', 's39', label='e')
    dfa_reserved_words.edge('s39', 's67', label='[a-zA-Z0-9]')

    # symbol
    dfa_reserved_words.node('s40', 's40: \nidentifier')
    dfa_reserved_words.node('s41', 's41: \nidentifier')
    dfa_reserved_words.node('s42', 's42: \nidentifier')
    dfa_reserved_words.node('s43', 's43: \nidentifier')
    dfa_reserved_words.node('s44', 's44: \nidentifier')
    dfa_reserved_words.node('s45', 's45: \nsymbol')

    dfa_reserved_words.edge('s0', 's40', label='s')
    dfa_reserved_words.edge('s40', 's41', label='y')
    dfa_reserved_words.edge('s41', 's42', label='m')
    dfa_reserved_words.edge('s42', 's43', label='b')
    dfa_reserved_words.edge('s43', 's44', label='o')
    dfa_reserved_words.edge('s44', 's45', label='l')
    dfa_reserved_words.edge('s45', 's67', label='[a-zA-Z0-9]')

    # integer
    dfa_reserved_words.node('s46', 's46: \nidentifier')
    dfa_reserved_words.node('s47', 's47: \nidentifier')
    dfa_reserved_words.node('s48', 's48: \nidentifier')
    dfa_reserved_words.node('s49', 's49: \nidentifier')
    dfa_reserved_words.node('s50', 's50: \nidentifier')
    dfa_reserved_words.node('s51', 's51: \nidentifier')
    dfa_reserved_words.node('s52', 's52: \ninteger')

    dfa_reserved_words.edge('s0', 's46', label='i')
    dfa_reserved_words.edge('s46', 's47', label='n')
    dfa_reserved_words.edge('s47', 's48', label='t')
    dfa_reserved_words.edge('s48', 's49', label='e')
    dfa_reserved_words.edge('s49', 's50', label='g')
    dfa_reserved_words.edge('s50', 's51', label='e')
    dfa_reserved_words.edge('s51', 's52', label='r')
    dfa_reserved_words.edge('s52', 's67', label='[a-zA-Z0-9]')

    # char
    dfa_reserved_words.node('s53', 's53: \nidentifier')
    dfa_reserved_words.node('s54', 's54: \nidentifier')
    dfa_reserved_words.node('s55', 's55: \nidentifier')
    dfa_reserved_words.node('s56', 's56: \nchar')

    dfa_reserved_words.edge('s0', 's53', label='c')
    dfa_reserved_words.edge('s53', 's54', label='h')
    dfa_reserved_words.edge('s54', 's55', label='a')
    dfa_reserved_words.edge('s55', 's56', label='r')
    dfa_reserved_words.edge('s56', 's67', label='[a-zA-Z0-9]')

    # real
    dfa_reserved_words.node('s57', 's57: \nidentifier')
    dfa_reserved_words.node('s58', 's58: \nidentifier')
    dfa_reserved_words.node('s59', 's59: \nidentifier')
    dfa_reserved_words.node('s60', 's60: \nreal')

    dfa_reserved_words.edge('s0', 's57', label='r')
    dfa_reserved_words.edge('s57', 's58', label='e')
    dfa_reserved_words.edge('s58', 's59', label='a')
    dfa_reserved_words.edge('s59', 's60', label='l')
    dfa_reserved_words.edge('s60', 's67', label='[a-zA-Z0-9]')

    # string
    dfa_reserved_words.node('s60', 's60: \nidentifier')
    dfa_reserved_words.node('s61', 's61: \nidentifier')
    dfa_reserved_words.node('s62', 's62: \nidentifier')
    dfa_reserved_words.node('s63', 's63: \nidentifier')
    dfa_reserved_words.node('s64', 's64: \nidentifier')
    dfa_reserved_words.node('s65', 's65: \nidentifier')
    dfa_reserved_words.node('s66', 's66: \nstring')

    dfa_reserved_words.edge('s0', 's61', label='s')
    dfa_reserved_words.edge('s61', 's62', label='t')
    dfa_reserved_words.edge('s62', 's63', label='r')
    dfa_reserved_words.edge('s63', 's64', label='i')
    dfa_reserved_words.edge('s64', 's65', label='n')
    dfa_reserved_words.edge('s65', 's66', label='g')
    dfa_reserved_words.edge('s66', 's67', label='[a-zA-Z0-9]')
    dfa_reserved_words.render(directory='dfa_output')


def generate_dfa_operators():
    dfa_operators = graphviz.Digraph('dfa_operators', format='png')

    dfa_operators.attr('node', shape='doublecircle')
    dfa_operators.attr('node', fixedsize='true')
    dfa_operators.attr('node', width='1.2')
    dfa_operators.attr('edge', shape='normal')

    dfa_operators.node('start_operators', shape='point', width='0')
    dfa_operators.node('q0', shape='circle', width='1')
    dfa_operators.edge('start_operators', 'q0', label='start')

    dfa_operators.node('q1', 'q1: \nRelational_\nop_lessthan')
    dfa_operators.node('q2', 'q2:\nRelational_\nop_lessthan\norequal')
    dfa_operators.node('q3', 'q3:\nRelational_\nop_notequal')
    dfa_operators.node('q4', 'q4:\nRelational_\nop_morethan')
    dfa_operators.node('q5', 'q5:\nRelational_\nop_morethan\norequal')
    dfa_operators.node('q6', 'q6:\nArithmetic_\nop_divide')
    dfa_operators.node('q7', 'q7:\nArithmetic_\nop_multiply')
    dfa_operators.node('q8', 'q8:\nArithmetic_\nop_subtract')
    dfa_operators.node('q9', 'q9:\nArithmetic_\nop_add')
    dfa_operators.node('q10', 'q10:\nAnd')
    dfa_operators.node('q11', 'q11:\nDot')
    dfa_operators.node('q12', 'q12:\nclose_\nbracket')
    dfa_operators.node('q13', 'q13:\nopen_\nbracket')
    dfa_operators.node('q14', 'q14:\nOr')

    dfa_operators.edge('q0', 'q1', label='<')
    dfa_operators.edge('q1', 'q2', label='=')
    dfa_operators.edge('q1', 'q3', label='>')
    dfa_operators.edge('q0', 'q4', label='>')
    dfa_operators.edge('q4', 'q5', label='=')
    dfa_operators.edge('q0', 'q6', label='/')
    dfa_operators.edge('q0', 'q7', label='*')
    dfa_operators.edge('q0', 'q8', label='-')
    dfa_operators.edge('q0', 'q9', label='+')
    dfa_operators.edge('q0', 'q10', label=',')
    dfa_operators.edge('q0', 'q11', label='.')
    dfa_operators.edge('q0', 'q12', label=')')
    dfa_operators.edge('q0', 'q13', label='(')
    dfa_operators.edge('q0', 'q14', label=';')

    dfa_operators.render(directory='dfa_output')


def generate_dfa_values():
    dfa_values = graphviz.Digraph('dfa_values', format='png')

    dfa_values.attr('node', shape='circle')
    dfa_values.attr('node', fixedsize='true')
    dfa_values.attr('node', width='1')
    dfa_values.attr('edge', shape='normal')

    dfa_values.node('start_reserved_words', shape='point', width='0')
    dfa_values.node('t0', shape='circle', width='1')
    dfa_values.edge('start_reserved_words', 't0', label='start')

    dfa_values.node('integer', shape='doublecircle')
    dfa_values.node('real', shape='doublecircle')
    dfa_values.node('char', shape='doublecircle')
    dfa_values.node('string', shape='doublecircle')

    dfa_values.edge('t0', 't1', label='\'')
    dfa_values.edge('t1', 't2', label='[a-zA-Z0-9]')
    dfa_values.edge('t2', 'char', label='\'')

    dfa_values.edge('t0', 'integer', label='[0-9]')
    dfa_values.edge('integer', 'integer', label='[0-9]')
    dfa_values.edge('integer', 't3', label='.')
    dfa_values.edge('t3', 'real', label='[0-9]')
    dfa_values.edge('real', 'real', label='[0-9]')

    dfa_values.edge('t0', 't4', label='\"')
    dfa_values.edge('t4', 't5', label='[a-zA-Z0-9]')
    dfa_values.edge('t5', 't6', label='[a-zA-Z0-9]')
    dfa_values.edge('t6', 'string', label='\"')

    dfa_values.render(directory='dfa_output')
