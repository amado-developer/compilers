# Generated from C:/Users/massa/Documents/Universidad/quinto a�o/Segundo semestre/Compiladores/newBeggining\MyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *

import Constants
from TypeSystem import type_system
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

from Errors import ett
from SymbolTable import *
from tableList import *
#tabla de simbolos
#lexema , semantica, linea, columna, tipo,  posicion, herencia,

def getNodeIndex(node):
    if(node.parentCtx == None or node == None):
        return -1
    parent = node.parentCtx
    for i in range(len(parent.children)):
        if(parent.children[i] == node):
            return i
def getLeftSibling(node):
    index = getNodeIndex(node)
    if(index <1):
        return None
    return node.parentCtx.children[index-1]
def getTable(name,list):
    for x in list:
        #print("tableLiist",x )
        #print("table name", x.name)
        if x.name == name:
            return x
def getFather(name,list):
    for x in list:
        #print("tableLiist",x )
        #print("table name", x.name)
        if x.name == name:
            return x.parent
# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):
    def __init__(self):
        self.ant = 0
        self.lt = None #ultima tabla utilizada
        self.propiedad = ""
    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx:MyGrammarParser.ProgramContext):

        self.ant +=1


        #print("hola desde enter program: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx:MyGrammarParser.ProgramContext):
        #print("hola desde EXIT PROGRAM: ", self.ant)
        if "Main" not in st.symbols.keys():
            print("ERROR: Class Main does not exist")
            ett.addError("ERROR: Class Main does not exist")
        pass


    # Enter a parse tree produced by MyGrammarParser#class.
    def enterClass(self, ctx:MyGrammarParser.ClassContext):
        type_system.test_type(ctx)
        self.ant += 1
        self.propiedad = "class"
        lex = ctx.children[1].symbol.text
        token = ctx.children[1].symbol.type
        line = ctx.children[0].getSymbol().line
        column = ctx.children[0].getSymbol().column
        element_type = Constants.tokens[ctx.children[0].symbol.type - 1]
        inherits = ""
        clean_error = True
        print("entering class: ", lex)
        #check Lex existance
        if lex in st.symbols.keys():
            clean_error = False
            print("ERROR: Class "+lex+ " already exists in line "+str(line)+" column "+str(column))
            ett.addError("ERROR: Class "+lex+ " already exists in line "+str(line)+" column "+str(column))

        #inherits
        for i in ctx.children:
            if i.getText() == "inherits":
                inherits = ctx.children[ctx.children.index(i)+1].getText()
                if inherits not in st.symbols.keys():
                    clean_error = False
                    print("ERROR: Class "+inherits+ " does not exist in line "+str(line)+" column "+str(column))
                    ett.addError("ERROR: Class "+inherits+ " does not exist in line "+str(line)+" column "+str(column))
                if inherits == lex:
                    clean_error = False
                    print("ERROR: Class "+lex+ " cannot inherit from itself in line "+str(line)+" column "+str(column))
                    ett.addError("ERROR: Class "+lex+ " cannot inherit from itself in line "+str(line)+" column "+str(column))
                break



        if clean_error:
            st.insert(lex, [token, line, column, "",0,inherits])
            self.lt = st
            if st not in tableList:
                #print("insertando tabla")
                tableList.append(st)
            st.insert(lex, [token, line, column, element_type ,0,inherits])
        #print("hola desde enter class: ", self.ant)

        pass

    # Exit a parse tree produced by MyGrammarParser#class.
    def exitClass(self, ctx:MyGrammarParser.ClassContext):
        print("exiting class")
        pass


    # Enter a parse tree produced by MyGrammarParser#feature.
    def enterFeature(self, ctx:MyGrammarParser.FeatureContext):
        print("entering feature")
        #print("IM LEFT SYBLING: ",getLeftSibling(ctx))
        #print("mapped list",list(map(lambda x: x.getText(), ctx.children)))
        line = ctx.children[0].getSymbol().line
        column = ctx.children[0].getSymbol().column
        #insertar feature
        parentName = ctx.parentCtx.children[1].getText()
        ID = ctx.children[0].getText()
        print("lexema: ", ID)
        st2 = self.lt
        if ett.getError() == "":

            if (self.lt.name == "global"):
                st2 = ScopeSymbolTable(parentName,self.lt)

            st2.insert(ID, [ctx.children[0].symbol.type, line, column, "",0,""])
            self.lt = st2
            self.propiedad = "feature"
            if st2 not in tableList:
                tableList.append(st2)
        #print(parentName)
        #print("tabla padre: ",getTable(parentName,tableList))
        #print("feature ID: ", ID)
        print( Constants.tokens[ctx.children[0].symbol.type - 1])
        self.ant += 1

        ##print("hola desde enter feature: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#feature.
    def exitFeature(self, ctx:MyGrammarParser.FeatureContext):
        print("self:" ,self.lt.name)
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
    def enterFormal(self, ctx:MyGrammarParser.FormalContext):
        print("entering formal")
        line = ctx.children[0].getSymbol().line
        column = ctx.children[0].getSymbol().column
        ID = ctx.children[0].getText()
        parentName = ctx.parentCtx.children[0].getText()
        st3 = self.lt
        print("parent: ",parentName)
        if ett.getError() == "":
            if (self.propiedad == "class" or self.propiedad == "feature"):
                print("insertando formal: ", self.lt.name)
                st3 = ScopeSymbolTable(parentName, self.lt)
            st3.insert(ID, [ctx.children[0].symbol.type, line, column, "", 0, ""])
            self.lt = st3
            self.propiedad = "formal"
            if st3 not in tableList:
                tableList.append(st3)

        #print("hola desde enter Formal: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#formal.
    def exitFormal(self, ctx:MyGrammarParser.FormalContext):
        self.ant += 1
        #print("hola desde exit formal: ", self.ant)
        pass


    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx:MyGrammarParser.ExprContext):
        self.ant += 1
        #print("hola desde enter expr: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx:MyGrammarParser.ExprContext):
        self.ant += 1
        #print("hola desde exit expr: ", self.ant)
        pass



del MyGrammarParser