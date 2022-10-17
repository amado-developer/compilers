import sys
from antlr4 import *
from yapl import *
from yapl.MyGrammarErrorListener import MyGrammarErrorListener

from yapl.MyGrammarLexer import MyGrammarLexer
from yapl.MyGrammarListener import MyGrammarListener
from yapl.MyGrammarParser import MyGrammarParser


def main(argv):
    file = open("./silly.yapl")
    code = ""
    for x in file:
        code += x + "\n"
    print(code)
    input_stream = InputStream(code)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyGrammarErrorListener.instance)
    tree = parser.program()
    walker = ParseTreeWalker();
    walker.walk(MyGrammarListener(), tree)


if __name__ == '__main__':
    main(sys.argv)