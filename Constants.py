core_types = {
    'INT': 'Int',
    'BOOL': 'Bool',
    'OBJECT': 'Object',
    'STRING': 'String',
    'IO': 'IO',
    # 'SELF_TYPE': 'SELF_TYPE'
}

core_scopes = ['Int', 'Bool', 'Object', 'String', 'IO']
core_scopes_types = {
    'Int': [],
    'Bool': [],
    'Object': ['abort', 'type_name', 'copy'],
    'String': ['length', 'concat', 'substr'],
    'IO': ['out_string', 'out_int', 'in_string', 'in_int'],
    # 'SELF_TYPE': ['abort', 'type_name', 'copy', 'length', 'concat', 'substr', 'out_string', 'out_int', 'in_string', 'in_int']
}

tokens = {
    'CLASS': 1,
    'ELSE': 2,
    'FI': 3,
    'IF': 4,
    'IN': 5,
    'INHERITS': 6,
    'ISVOID': 7,
    'LOOP': 8,
    'POOL': 9,
    'THEN': 10,
    'WHILE': 11,
    'NEW': 12,
    'NOT': 13,
    'LET': 14,
    'FALSE': 15,
    'TRUE': 16,
    'SEMICOLON': 17,
    'LCURLY': 18,
    'RCURLY': 19,
    'LSQUARE': 20,
    'RSQUARE': 21,
    'LROUND': 22,
    'RROUND': 23,
    'COMMA': 24,
    'POINT': 25,
    'QUOTES': 26,
    'APOSTROPHE': 27,
    'ADD': 28,
    'SUB': 29,
    'MULTIPLY': 30,
    'DIVIDE': 31,
    'INT_NOT': 32,
    'COLON': 33,
    'ASIGN': 34,
    'ARROBA': 35,
    'LESS_THAN': 36,
    'LESS_EQUAL': 37,
    'EQUAL': 38,
    'LINE_COMMENT': 39,
    'COMMENT': 40,
    'INTEGER': 41,
    'STRING': 42,
    'TYPE': 43,
    'ID': 44,
    'WS': 45,
    'ERR_TOKEN': 46
}

operations = {
    tokens['ADD']: '+',
    tokens['SUB']: '-',
    tokens['MULTIPLY']: '*',
    tokens['DIVIDE']: '/',
    tokens['LESS_THAN']: '<',
    tokens['LESS_EQUAL']: '<=',
    tokens['EQUAL']: '=='
}

semantic = {
    'CLASS': 'class',
    'ATTR': 'attr',
    'METHOD': 'method',
    'PARAMETER': 'parameter',
    'EXPR': 'expr',
    'OBJ': 'obj'
}

returnTypes = {
    'ERROR': 'ERROR',
    'NO_TYPE': 'no_type',
    'CHECK_TYPE': 'check_type'
}

strings = {
    'LET': 'let',
    'IN': 'in',
    'DELIMITER': ':'
}


