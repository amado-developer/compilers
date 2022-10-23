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



type_system = TypeSystem()
