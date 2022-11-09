import sys
from antlr4 import *

import Constants
from TypeSystem import type_system
from yapl import *
from yapl.MyGrammarErrorListener import MyGrammarErrorListener

from yapl.MyGrammarLexer import MyGrammarLexer
from yapl.MyGrammarListener import MyGrammarListener
from yapl.MyGrammarParser import MyGrammarParser
from SymbolTable import st
from Errors import ett
from globalVariables import *

def main(argv):
    #print(Constants.tokens)
    file = open("./silly.yapl")
    code = ""
    for x in file:
        code += x
    print(code)
    input_stream = InputStream(code)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyGrammarErrorListener.instance)
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(MyGrammarListener(), tree)
    # print tableList
    print(st)
    if (st.get_children() != []):
        st.print_children()

    # for table in st.children:
    #     print(table)
    # if ett.getError() == "":
    #     print("No errors found")


if __name__ == '__main__':
    main(sys.argv)
