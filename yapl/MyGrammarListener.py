# Generated from C:/Users/massa/Documents/Universidad/quinto año/Segundo semestre/Compiladores/newBeggining\MyGrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):
    def __init__(self):
        self.ant = 0
    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx:MyGrammarParser.ProgramContext):

        self.ant +=1
        print("hola desde enter program: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx:MyGrammarParser.ProgramContext):
        print("hola desde EXIT PROGRAM: ", self.ant)

        pass


    # Enter a parse tree produced by MyGrammarParser#class.
    def enterClass(self, ctx:MyGrammarParser.ClassContext):
        self.ant += 1
        print("hola desde enter class: ", self.ant)

        pass

    # Exit a parse tree produced by MyGrammarParser#class.
    def exitClass(self, ctx:MyGrammarParser.ClassContext):

        # check main existance
        if ctx.children[1].getText() != "Main":
            print("ERROR: main class not found")

        pass


    # Enter a parse tree produced by MyGrammarParser#feature.
    def enterFeature(self, ctx:MyGrammarParser.FeatureContext):
        self.ant += 1
        print("hola desde enter feature: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#feature.
    def exitFeature(self, ctx:MyGrammarParser.FeatureContext):
        self.ant += 1
        print("hola desde exit feature: ", self.ant)
        pass


    # Enter a parse tree produced by MyGrammarParser#formal.
    def enterFormal(self, ctx:MyGrammarParser.FormalContext):
        self.ant += 1
        print("hola desde enter Formal: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#formal.
    def exitFormal(self, ctx:MyGrammarParser.FormalContext):
        self.ant += 1
        print("hola desde exit formal: ", self.ant)
        pass


    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx:MyGrammarParser.ExprContext):
        self.ant += 1
        print("hola desde enter expr: ", self.ant)
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx:MyGrammarParser.ExprContext):
        self.ant += 1
        print("hola desde exit expr: ", self.ant)
        pass



del MyGrammarParser