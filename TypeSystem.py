from Constants import core_scopes, core_scopes_types, tokens
from Errors import ett
from SymbolTable import ScopeSymbolTable, st

from yapl.MyGrammarParser import MyGrammarParser


class TypeSystem:
    def __init__(self):
        pass
        # self.symbol_table = SymbolTable()

    def add_core_scopes(self):
        for core_scope in core_scopes:
            symbol_table = ScopeSymbolTable(core_scope, st)
            st.insert(core_scope, [tokens['TYPE'], 0, 0, "", 0, ""])
            for core_scopes_type in core_scopes_types[core_scope]:
                symbol_table.insert(core_scopes_type, [tokens['TYPE'], 0, 0, "", 0, ""])

    def check_arithmetic(self, expr):
        pass

    def check_assignment(self, ctx):
        expected_type = ''

        for child in ctx.children:
            if child.getText() == ":":
                expected_type = ctx.children[ctx.children.index(child) + 1].getText().upper()
        token_keys = list(tokens.keys())

        if expected_type == 'BOOLEAN' \
                and token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] != 'INT' \
                or (expected_type == 'BOOLEAN'
                    and token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)] == 'INT'
                    and ctx.children[-1].children[0].getText() != '1'
                    and ctx.children[-1].children[0].getText() != '0') \
                or (expected_type != 'BOOLEAN' and
                    type(ctx.children[-1]) == MyGrammarParser.ExprContext
                    and hasattr(ctx.children[-1].children[0], 'symbol')
                    and expected_type !=
                    token_keys[list(tokens.values()).index(ctx.children[-1].children[0].symbol.type)]):
            print("ERROR: Type mismatch in line " + str(ctx.children[0].getSymbol().line) + " column " + str(
                ctx.children[0].getSymbol().column))
            ett.addError("ERROR: Type mismatch in line " + str(ctx.children[0].getSymbol().line) + " column " + str(
                ctx.children[0].getSymbol().column))


type_system = TypeSystem()
