# Generated from C:/Users/massa/Documents/Universidad/quinto a�o/Segundo semestre/Compiladores/newBeggining\MyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *

import Constants
import globalVariables

from TypeSystem import type_system

if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser
from Errors import ett
from SymbolTable import *
from globalVariables import *



# tabla de simbolos
# lexema , semantica, linea, columna, tipo,  posicion, herencia, byte size,tipo semantica, no param



def getNodeIndex(node):
    if (node.parentCtx == None or node == None):
        return -1
    parent = node.parentCtx
    for i in range(len(parent.children)):
        if (parent.children[i] == node):
            return i


def getLeftSibling(node):
    index = getNodeIndex(node)
    if (index < 1):
        return None
    return node.parentCtx.children[index - 1]


def getTable(name, list):
    for x in list:
        # print("tableLiist",x )
        # print("table name", x.name)
        if x.name == name:
            return x


def getFather(name, list):
    for x in list:
        # print("tableLiist",x )
        # print("table name", x.name)
        if x.name == name:
            return x.parent


# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):
    def __init__(self):
        self.ant = 0
        self.lt = None  # ultima tabla utilizada
        self.propiedad = ""

    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx: MyGrammarParser.ProgramContext):

        self.ant += 1
        type_system.add_core_scopes()

        # print("hola desde enter program: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx: MyGrammarParser.ProgramContext):
        # print("hola desde EXIT PROGRAM: ", self.ant)
        if "Main" not in st.symbols.keys():
            print("ERROR: Class Main does not exist")
            ett.addError("ERROR: Class Main does not exist")

    # Enter a parse tree produced by MyGrammarParser#class.
    def enterClass(self, ctx: MyGrammarParser.ClassContext):
        self.ant += 1
        self.propiedad = "class"
        lex = ctx.children[1].symbol.text
        token = ctx.children[1].symbol.type
        line = ctx.children[0].getSymbol().line
        column = ctx.children[0].getSymbol().column
        inherits = ""
        byteSize = 0
        sem_type = "class"
        noParam = 0
        clean_error = True
        print("entering class: ", lex)
        # check Lex existance
        if lex in st.symbols.keys():
            clean_error = False
            print("ERROR: Class " + lex + " already exists in line " + str(line) + " column " + str(column))
            ett.addError("ERROR: Class " + lex + " already exists in line " + str(line) + " column " + str(column))

        # inherits
        for i in ctx.children:
            if i.getText() == "inherits":
                inherits = ctx.children[ctx.children.index(i) + 1].getText()
                if inherits not in st.symbols.keys():
                    clean_error = False
                    print(
                        "ERROR: Class " + inherits + " does not exist in line " + str(line) + " column " + str(column))
                    ett.addError(
                        "ERROR: Class " + inherits + " does not exist in line " + str(line) + " column " + str(column))
                if inherits == lex:
                    clean_error = False
                    print("ERROR: Class " + lex + " cannot inherit from itself in line " + str(line) + " column " + str(
                        column))
                    ett.addError(
                        "ERROR: Class " + lex + " cannot inherit from itself in line " + str(line) + " column " + str(
                            column))
                break

        if clean_error:
            st.insert(lex, [token, line, column, "", globalVariables.memPos, inherits, byteSize, sem_type, noParam])
            self.lt = st
            if st not in tableList:
                # print("insertando tabla")
                tableList.append(st)
            #st.insert(lex, [token, line, column, "", 0, inherits, byteSize, sem_type, noParam])
        pass

    # Exit a parse tree produced by MyGrammarParser#class.
    def exitClass(self, ctx: MyGrammarParser.ClassContext):
        print("exiting class")
        pass

    # Enter a parse tree produced by MyGrammarParser#feature.
    def enterFeature(self, ctx: MyGrammarParser.FeatureContext):
        print("entering feature")
        # print("IM LEFT SYBLING: ",getLeftSibling(ctx))
        # print("mapped list",list(map(lambda x: x.getText(), ctx.children)))
        line = ctx.children[0].getSymbol().line
        column = ctx.children[0].getSymbol().column
        byteSize = 0
        sem_type = "null"
        noParam = 0


        # insertar feature
        parentName = ctx.parentCtx.children[1].getText()
        ID = ctx.children[0].getText()
        print("lexema: ", ID)
        st2 = self.lt

        #Assignment check
        type_system.check_assignment(ctx)

        if ett.getError() == "":
            if self.lt.name == "global":
                st2 = ScopeSymbolTable(parentName, self.lt)
                # Amado - Self Insertion
                st2.insert("self", [44, line, column, parentName, globalVariables.memPos, "", byteSize, "reference", noParam]) #sem_type

            # Type insertion - Amado
            type_ = ""
            for child in ctx.children:
                if child.getText() == ":":
                    type_ = ctx.children[ctx.children.index(child) + 1].getText()
                    sem_type = "Reference"
                    if type_ == "SELF_TYPE":
                        type_ = parentName
                    break
            #--------------------------------------------
            #define byteSize
            if type_ == "Int":
                byteSize = 4
            elif type_ == "Bool":
                byteSize = 1
            elif type_ == "String":
                byteSize = 50
            elif type_ == "SELF_TYPE" or st2.lookup(type_):
                byteSize = 100
            elif type_ == "Object":
                byteSize = 75
            elif type_ == "IO":
                byteSize = 100

            st2.insert(ID, [ctx.children[0].symbol.type, line, column, type_, globalVariables.memPos, "",byteSize,sem_type,noParam])
            self.lt = st2
            self.propiedad = "feature"
            if st2 not in tableList:
                tableList.append(st2)
        # print(parentName)
        # print("tabla padre: ",getTable(parentName,tableList))
        # print("feature ID: ", ID)
        globalVariables.memPos = globalVariables.memPos + byteSize
        self.ant += 1

    # Exit a parse tree produced by MyGrammarParser#feature.
    def exitFeature(self, ctx: MyGrammarParser.FeatureContext):

        print("exiting feature")
        """
        for i in self.lt.symbols.keys():
            print("I: ",i)
            print("ID: ", ID)
            if i == ID:
                print("ERROR: Feature "+ID+ " already exists in line "+str(line)+" column "+str(column))
                ett.addError("ERROR: Feature "+ID+ " already exists in line "+str(line)+" column "+str(column))
                break
        ##print("hola desde exit feature: ", self.ant)
        pass
        """

    # Enter a parse tree produced by MyGrammarParser#formal.
    def enterFormal(self, ctx: MyGrammarParser.FormalContext):
        print("entering formal")
        line = ctx.children[0].getSymbol().line
        column = ctx.children[0].getSymbol().column
        ID = ctx.children[0].getText()
        parentName = ctx.parentCtx.children[0].getText()
        st3 = self.lt
        byteSize = 0
        sem_type = "null"
        noParam = 1

        #get no. of parameters
        for i in ctx.parentCtx.children:
            if i.getText() == ",":
                noParam = noParam + 1

        #inserting param number in parent
        if hasattr(st3.parent,"symbols") and  parentName in st3.parent.symbols.keys():
            #print("I FOUND IT: ",parentName)
            #print("this is the value: ",st3.lookupKey("fibonnacci"))

            #get parent current attributes
            parent = st3.parent.symbols[parentName]
            parent[8] = noParam
            st3.parent.insert(parentName, parent)

        if ett.getError() == "":
            if self.propiedad == "class" or self.propiedad == "feature":
                print("insertando formal: ", self.lt.name)
                st3 = ScopeSymbolTable(parentName, self.lt)

            # Type insertion - Amado
            type_ = ""
            for child in ctx.children:
                if child.getText() == ":":
                    type_ = ctx.children[ctx.children.index(child) + 1].getText() #revisar existencias del feature
                    if st3.lookupKey(type_) == True:
                        pass
                    else:
                        print("ERROR: Type " + type_ + " does not exist in line " + str(line) + " column " + str(column))
                        ett.addError("ERROR: Type " + type_ + " does not exist in line " + str(line) + " column " + str(column))
                    sem_type = "parameter"

                    break
            #--------------------------------------------  BYTE SIZE
            if type_ == "Int":
                byteSize = 4
            elif type_ == "Bool":
                byteSize = 1
            elif type_ == "String":
                byteSize = 50
            elif type_ == "SELF_TYPE" or st3.lookup(type_):
                byteSize = 100
            elif type_ == "Object":
                byteSize = 75
            elif type_ == "IO":
                byteSize = 100
            # --------------------------------------------
            st3.insert(ID, [ctx.children[0].symbol.type, line, column, type_, globalVariables.memPos, "", byteSize,sem_type,0])
            self.lt = st3
            self.propiedad = "formal"
            if st3 not in tableList:
                tableList.append(st3)
        # print("hola desde enter Formal: ", self.ant)
        globalVariables.memPos = globalVariables.memPos + byteSize
        pass

    # Exit a parse tree produced by MyGrammarParser#formal.
    def exitFormal(self, ctx: MyGrammarParser.FormalContext):
        self.ant += 1
        # print("hola desde exit formal: ", self.ant)
        pass

    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx: MyGrammarParser.ExprContext):
        self.ant += 1
        # print("hola desde enter expr: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx: MyGrammarParser.ExprContext):
        self.ant += 1
        # print("hola desde exit expr: ", self.ant)
        pass


del MyGrammarParser
