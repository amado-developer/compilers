# Reference https://github.com/antlr/antlr4/blob/master/doc/python-target.md
# https://github.com/antlr/antlr4/blob/master/doc/getting-started.md
"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
COMPILADORES
LAB 0
Amado Garcia y Mario Sarmientos
"""

from antlr4 import *

from ErrorHandler import YaplErrorListener
from dist.YAPLLexer import YAPLLexer
from dist.YAPLParser import YAPLParser


def main(file_name):
    input_stream = FileStream(f'./{file_name}')
    lexer = YAPLLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = YAPLParser(tokens)
    parser.addErrorListener(YaplErrorListener())
    tree = parser.program()
    print(tree.toStringTree())

    try:
        input_stream = FileStream(f'./{file_name}')
        lexer = YAPLLexer(input_stream)
        token = lexer.nextToken()

        while token.type != token.EOF:
            print(token)
            token = lexer.nextToken()
    except Exception:
        print("Error occurred")


if __name__ == '__main__':
    test_file = input("Enter Test File Name: ")
    main(test_file)
