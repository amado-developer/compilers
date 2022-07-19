import sys


class YaplErrorListener(object):

    @staticmethod
    def syntaxError(recognizer, wrong_character, line, column, msg, e):
        print(msg)
