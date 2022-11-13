import globalVariables
from Constants import core_scopes, core_scopes_types, tokens, byte_sizes, operands
from Errors import ett

from SymbolTable import ScopeSymbolTable, st
from yapl.MyGrammarParser import MyGrammarParser
from globalVariables import *

class TypeSystem:
    def __init__(self):
        pass

    @staticmethod
    def add_core_scopes():
        for core_scope in core_scopes:
            symbol_table = ScopeSymbolTable(core_scope, st)
            st.insert(core_scope, [tokens['TYPE'], 0, 0, "", globalVariables.memPos, "", byte_sizes[core_scope], "class", 0])
            if core_scope == "Int":
                globalVariables.memPos += 4
            elif core_scope == "Bool":
                globalVariables.memPos += 1
            for core_scopes_type in core_scopes_types[core_scope]:
                symbol_table.insert(core_scopes_type[0], [tokens['TYPE'], 0, 0, core_scopes_type[1], globalVariables.memPos, "",
                                                          byte_sizes[core_scopes_type[1]], "class", 0])
                if core_scope == "String":
                    globalVariables.memPos += 50
                elif core_scope == "Object":
                    globalVariables.memPos += 75
                elif core_scope == "IO":
                    globalVariables.memPos += 100


    def get_children(self, child, arr, ctx):
        token_keys = list(tokens.keys())
        for c in child.children:
            if isinstance(c, MyGrammarParser.ExprContext):
                self.get_children(c, arr, ctx)
            else:
                if hasattr(child.children[0], 'symbol') and\
                        token_keys[list(tokens.values()).index(child.children[0].symbol.type)] != 'INTEGER' \
                        and c.getText() != '+' and c.getText() != '-' and c.getText() != '*' and c.getText() != '/':
                    print("ERROR: Invalid Arithmetic types in " + str(child.children[0].getSymbol().line)
                          + " column " + str(child.children[0].getSymbol().column))
                    ett.addError(
                        "ERROR: Invalid Arithmetic types in  " + str(child.children[0].getSymbol().line)
                        + " column " + str(child.children[0].getSymbol().column))

                arr.append(c.getText())

    def check_arithmetic(self, ctx, expected_type):
        expr = ctx.children[-1]
        arr = []

        for child in expr.children:
            if isinstance(child, MyGrammarParser.ExprContext):
                self.get_children(child, arr, ctx)
            else:
                if child.symbol.type != 41:
                    print("ERROR: Invalid Arithmetic operation in " + str(ctx.children[0].getSymbol().line)
                          + " column " + str(ctx.children[0].getSymbol().column))
                    ett.addError(
                        "ERROR: Invalid Arithmetic operation in  " + str(ctx.children[0].getSymbol().line)
                        + " column " + str(ctx.children[0].getSymbol().column))
                    return
                else:
                    arr.append(child.getText())

        is_previous_operand = False
        for element in arr:
            if element == '+' or element == '-' or element == '*' or element == '/':
                if is_previous_operand:
                    print("ERROR: Invalid Arithmetic operation in " + str(ctx.children[0].getSymbol().line)
                          + " column " + str(ctx.children[0].getSymbol().column))
                    ett.addError(
                        "ERROR: Invalid Arithmetic operation in  " + str(ctx.children[0].getSymbol().line)
                        + " column " + str(ctx.children[0].getSymbol().column))
                is_previous_operand = True
            else:
                is_previous_operand = False

    def check_assignment(self, ctx):

        expected_type = ''

        for child in ctx.children:
            if child.getText() == ":":
                expected_type = ctx.children[ctx.children.index(child) + 1].getText().upper()
        token_keys = list(tokens.keys())
        if isinstance(ctx.children[-1], MyGrammarParser.ExprContext) \
                and len(ctx.children[-1].children) > 1 \
                and ctx.children[-1].children[1].getText() in operands:
            self.check_arithmetic(ctx, expected_type)
        elif expected_type == 'BOOLEAN':
            self.check_boolean_assignment(ctx, token_keys)
        elif expected_type == 'INT':
            self.check_int_assignment(ctx, token_keys)
        elif expected_type == 'STRING':
            self.check_string_assignment(ctx, token_keys)

    def check_boolean_assignment(self, ctx, token_keys):
        if token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'INTEGER':
            if ctx.children[-1].getText() != 'true' and ctx.children[-1].getText() != 'false':
                self.type_mismatch_error(ctx)
        elif token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] == 'INTEGER' \
                and ctx.children[-1].children[0].getText() != '1' \
                and ctx.children[-1].children[0].getText() != '0':
            self.type_mismatch_error(ctx)

    def check_int_assignment(self, ctx, token_keys):
        if hasattr(ctx.children[-1], 'children') and hasattr(ctx.children[-1].children[0], 'symbol') and \
                token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'INTEGER':
            self.type_mismatch_error(ctx)

    def check_string_assignment(self, ctx, token_keys):
        if hasattr(ctx.children[-1], 'children') and hasattr(ctx.children[-1].children[0], 'symbol') and \
                token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'STRING':
            self.type_mismatch_error(ctx)

    @staticmethod
    def type_mismatch_error(ctx):
        print("ERROR: Type mismatch in line " + str(ctx.children[0].getSymbol().line) + " column " + str(
            ctx.children[0].getSymbol().column))
        ett.addError("ERROR: Type mismatch in line " + str(ctx.children[0].getSymbol().line) + " column " + str(
            ctx.children[0].getSymbol().column))


    def getMemorySize(self, type, tree):
        if type == "Int":
            globalVariables.memPos += 4
        elif type == "Bool":
            globalVariables.memPos += 1
        elif type == "String":
            globalVariables.memPos += 50
        elif type == "Object":
            globalVariables.memPos += 75
        elif type == "IO":
            globalVariables.memPos += 100
        elif type == "SELF_TYPE" or tree.lookupKey(type):
            globalVariables.memPos += 100

type_system = TypeSystem()

"""
import globalVariables
from Constants import core_scopes, core_scopes_types, tokens, byte_sizes, operands
from Errors import ett

from SymbolTable import ScopeSymbolTable, st
from yapl.MyGrammarParser import MyGrammarParser
from globalVariables import *

class TypeSystem:
    def __init__(self):
        pass

    @staticmethod
    def add_core_scopes():
        for core_scope in core_scopes:
            symbol_table = ScopeSymbolTable(core_scope, st)
            st.insert(core_scope, [tokens['TYPE'], 0, 0, "", globalVariables.memPos, "", byte_sizes[core_scope], "class", 0])
            for core_scopes_type in core_scopes_types[core_scope]:
                symbol_table.insert(core_scopes_type[0], [tokens['TYPE'], 0, 0, core_scopes_type[1], globalVariables.memPos, "",
                                                          byte_sizes[core_scopes_type[1]], "class", 0])

    def get_children(self, child, arr, ctx):
        token_keys = list(tokens.keys())
        for c in child.children:
            if isinstance(c, MyGrammarParser.ExprContext):
                self.get_children(c, arr, ctx)
            else:
                if hasattr(child.children[0], 'symbol') and \
                        token_keys[list(tokens.values()).index(child.children[0].symbol.type)] != 'INTEGER' \
                        and c.getText() != '+' and c.getText() != '-' and c.getText() != '*' and c.getText() != '/':
                    print("ERROR: Invalid Arithmetic types in " + str(child.children[0].getSymbol().line)
                          + " column " + str(child.children[0].getSymbol().column))
                    ett.addError(
                        "ERROR: Invalid Arithmetic types in  " + str(child.children[0].getSymbol().line)
                        + " column " + str(child.children[0].getSymbol().column))

                arr.append(c.getText())

    def check_arithmetic(self, ctx, expected_type):
        expr = ctx.children[-1]
        arr = []

        for child in expr.children:
            if isinstance(child, MyGrammarParser.ExprContext):
                self.get_children(child, arr, ctx)
            else:
                arr.append(child.getText())

        is_previous_operand = False
        for element in arr:
            if element == '+' or element == '-' or element == '*' or element == '/':
                if is_previous_operand:
                    print("ERROR: Invalid Arithmetic operation in " + str(ctx.children[0].getSymbol().line)
                          + " column " + str(ctx.children[0].getSymbol().column))
                    ett.addError(
                        "ERROR: Invalid Arithmetic operation in  " + str(ctx.children[0].getSymbol().line)
                        + " column " + str(ctx.children[0].getSymbol().column))
                is_previous_operand = True
            else:
                is_previous_operand = False

    def check_assignment(self, ctx):

        expected_type = ''

        for child in ctx.children:
            if child.getText() == ":":
                expected_type = ctx.children[ctx.children.index(child) + 1].getText().upper()
        token_keys = list(tokens.keys())

        if isinstance(ctx.children[-1], MyGrammarParser.ExprContext):
            try:
                if ctx.children[-1].children[1].getText() in operands:
                    self.check_arithmetic(ctx, expected_type)
            except:
                pass

        if expected_type == 'BOOLEAN':
            self.check_boolean_assignment(ctx, token_keys)
        if expected_type == 'INT':
            self.check_int_assignment(ctx, token_keys)
        if expected_type == 'STRING':
            self.check_string_assignment(ctx, token_keys)

    def check_boolean_assignment(self, ctx, token_keys):
        if token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'INTEGER':
            if ctx.children[-1].getText() != 'true' and ctx.children[-1].getText() != 'false':
                self.type_mismatch_error(ctx)
        elif token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] == 'INTEGER' \
                and ctx.children[-1].children[0].getText() != '1' \
                and ctx.children[-1].children[0].getText() != '0':
            self.type_mismatch_error(ctx)

    def check_int_assignment(self, ctx, token_keys):
        if hasattr(ctx.children[-1], 'children') and hasattr(ctx.children[-1].children[0], 'symbol') and \
                token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'INTEGER':
            self.type_mismatch_error(ctx)

    def check_string_assignment(self, ctx, token_keys):
        if hasattr(ctx.children[-1], 'children') and hasattr(ctx.children[-1].children[0], 'symbol') and \
                token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'STRING':
            self.type_mismatch_error(ctx)

    @staticmethod
    def type_mismatch_error(ctx):
        print("ERROR: Type mismatch in line " + str(ctx.children[0].getSymbol().line) + " column " + str(
            ctx.children[0].getSymbol().column))
        ett.addError("ERROR: Type mismatch in line " + str(ctx.children[0].getSymbol().line) + " column " + str(
            ctx.children[0].getSymbol().column))


    def getMemorySize(self, type, tree):
        if type == "Int":
            globalVariables.memPos += 4
        elif type == "Bool":
            globalVariables.memPos += 1
        elif type == "String":
            globalVariables.memPos += 50
        elif type == "Object":
            globalVariables.memPos += 75
        elif type == "IO":
            globalVariables.memPos += 100
        elif type == "SELF_TYPE" or tree.lookupKey(type):
            globalVariables.memPos += 100

type_system = TypeSystem()

"""