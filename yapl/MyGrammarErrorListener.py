from antlr4 import *
from antlr4.error import ErrorListener


class MyGrammarErrorListener(ErrorListener.ErrorListener):
    instance = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax error at line " + str(line) + ":" + str(column) + " " + msg)

MyGrammarErrorListener.instance = MyGrammarErrorListener()