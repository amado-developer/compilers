from Constants import core_scopes, core_scopes_types, tokens
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

    def evaluate_feature(self, ctx):
        rules = []
        children = ctx.children
        if len(ctx.children) == 3:
            rules = [children[0].symbol.type == 44, children[1].symbol.type == 45, children[2].symbol.type == 46]
            pass
        if len(ctx.children) == 4:
            pass
        if len(ctx.children) == 8:
            pass
        if len(ctx.children) > 8:
            pass

    def evaluate_formal(self, ctx):
        return True

    def evaluate_expression(self, ctx):
        return True


type_system = TypeSystem()
