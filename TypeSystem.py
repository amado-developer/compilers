from Constants import core_scopes, core_scopes_types, tokens
from SymbolTable import ScopeSymbolTable, st
from yapl.MyGrammarParser import MyGrammarParser


class TypeSystem:
    def __init__(self):
        pass
        # self.symbol_table = SymbolTable()

    def add_core_scopes(self):
        byteSize = 0
        sem_type = "class"
        noParam = 0
        for core_scope in core_scopes:
            symbol_table = ScopeSymbolTable(core_scope, st)
            if core_scope == "Int":
                byteSize = 4
            if core_scope == "Object":
                byteSize = 75
            if core_scope == "Bool":
                byteSize = 1
            if core_scope == "String":
                byteSize = 50
            if core_scope == "IO":
                byteSize = 100
            st.insert(core_scope, [tokens['TYPE'], 0, 0, "", 0, "", byteSize, sem_type, noParam])
            for core_scopes_type in core_scopes_types[core_scope]:
                symbol_table.insert(core_scopes_type, [tokens['TYPE'], 0, 0, "", 0, "", byteSize, sem_type, noParam])



type_system = TypeSystem()
