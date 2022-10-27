from Constants import core_scopes, core_scopes_types, tokens, byte_sizes
from SymbolTable import ScopeSymbolTable, st
from yapl.MyGrammarParser import MyGrammarParser


class TypeSystem:
    def __init__(self):
        pass

    @staticmethod
    def add_core_scopes():
        for core_scope in core_scopes:
            symbol_table = ScopeSymbolTable(core_scope, st)
            st.insert(core_scope, [tokens['TYPE'], 0, 0, "", 0, "", byte_sizes[core_scope], "class", 0])
            for core_scopes_type in core_scopes_types[core_scope]:
                symbol_table.insert(core_scopes_type[0], [tokens['TYPE'], 0, 0, core_scopes_type[1], 0, "",
                                                          byte_sizes[core_scopes_type[1]], "class", 0])


type_system = TypeSystem()
