# Reference https://github.com/antlr/antlr4/blob/master/doc/python-target.md

from antlr4 import *
from dist.YAPLLexer import YAPLLexer


def main(file_name):
    input_stream = FileStream(f'./{file_name}')
    lexer = YAPLLexer(input_stream)


if __name__ == '__main__':
    test_file = input("Enter Test File Name: ")
    main(test_file)
