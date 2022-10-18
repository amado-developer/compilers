
class ScopeSymbolTable:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.symbols = {}
        self.children = []
        self.level = 0
        if parent:
            self.level = parent.level + 1
            parent.children.append(self)
    #representa como cadena la tabla de simbolos
    def __str__(self):
        ret = "ScopeSymbolTable(%s) - level: %d\n" % (self.name, self.level)
        ret += "lexema \t semantica \t\t linea \t\t columna"+ "\t\t tipo"+ "\t\t posicion"+ "\t\t herencia"+ "\n"
        keys = self.symbols.keys()
        for key in keys:
            if(self.symbols[key][3] == ""):
                ret += "%s \t\t %s \t\t %s \t\t\t  %s \t\t\t\t %s \t\t\t %s \t\t\t %s   \n" % (
                key, self.symbols[key][0], self.symbols[key][1], self.symbols[key][2], self.symbols[key][3],
                self.symbols[key][4], self.symbols[key][5])
            else:
                ret += "%s \t\t %s \t\t %s \t\t\t  %s \t\t\t %s \t\t %s \t\t\t\t %s   \n" % (key, self.symbols[key][0],self.symbols[key][1],self.symbols[key][2],self.symbols[key][3],
                                                                                             self.symbols[key][4],self.symbols[key][5])
        return ret
    #insertar elemento
    # lexema , semantica, linea, columna, tipo,  posicion, herencia
    def insert(self, name, symbol):
        self.symbols[name] = symbol
    #funcion para encontrar elemento
    def lookup(self, name, current_scope_only=False):
        symbol = None
        if name in self.symbols:
            symbol = self.symbols[name]
        else:
            if current_scope_only:
                return None
            if self.parent:
                symbol = self.parent.lookup(name)
        return symbol

    def lookup_current_scope(self, name):
        return self.lookup(name, True)

    def get_symbols(self):
        return self.symbols

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent
    #scope
    def get_level(self):
        return self.level

    def get_name(self):
        return self.name

st = ScopeSymbolTable("global")

"""
st.insert("a", [1,2,3])
st.insert("b", 2)
st.insert("c", 3)
"""
#get value inside list
#st.symbols.get("a")[0]

#print(st.symbols.get("a")[0])




