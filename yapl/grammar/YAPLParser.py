# Generated from ./grammar/YAPL.g4 by ANTLR 4.10
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,222,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,3,2,28,
        8,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,5,3,51,8,3,10,3,12,3,54,
        9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,3,
        3,70,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,81,8,5,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,89,8,6,10,6,12,6,92,9,6,5,6,94,8,6,10,6,12,6,
        97,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,4,6,118,8,6,11,6,12,6,119,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,128,8,6,10,6,12,6,131,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,4,6,146,8,6,11,6,12,6,147,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,172,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,198,8,6,
        1,6,1,6,1,6,1,6,1,6,1,6,5,6,206,8,6,10,6,12,6,209,9,6,5,6,211,8,
        6,10,6,12,6,214,9,6,1,6,5,6,217,8,6,10,6,12,6,220,9,6,1,6,0,1,12,
        7,0,2,4,6,8,10,12,0,0,254,0,14,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,
        6,69,1,0,0,0,8,71,1,0,0,0,10,75,1,0,0,0,12,171,1,0,0,0,14,15,3,2,
        1,0,15,1,1,0,0,0,16,17,3,4,2,0,17,18,5,1,0,0,18,19,3,2,1,0,19,22,
        1,0,0,0,20,22,5,0,0,1,21,16,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,
        24,5,16,0,0,24,27,5,44,0,0,25,26,5,17,0,0,26,28,5,44,0,0,27,25,1,
        0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,35,5,2,0,0,30,31,3,6,3,0,31,
        32,5,1,0,0,32,34,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,
        0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,3,0,0,39,5,1,
        0,0,0,40,41,5,46,0,0,41,52,5,4,0,0,42,47,3,8,4,0,43,44,5,5,0,0,44,
        46,3,8,4,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,
        0,48,51,1,0,0,0,49,47,1,0,0,0,50,42,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,6,0,0,
        56,57,5,7,0,0,57,58,5,44,0,0,58,59,5,2,0,0,59,60,3,12,6,0,60,61,
        5,3,0,0,61,70,1,0,0,0,62,63,5,46,0,0,63,64,5,7,0,0,64,67,5,44,0,
        0,65,66,5,20,0,0,66,68,3,12,6,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,
        1,0,0,0,69,40,1,0,0,0,69,62,1,0,0,0,70,7,1,0,0,0,71,72,5,46,0,0,
        72,73,5,7,0,0,73,74,5,44,0,0,74,9,1,0,0,0,75,76,5,46,0,0,76,77,5,
        7,0,0,77,80,5,44,0,0,78,79,5,20,0,0,79,81,3,12,6,0,80,78,1,0,0,0,
        80,81,1,0,0,0,81,11,1,0,0,0,82,83,6,6,-1,0,83,84,5,46,0,0,84,95,
        5,4,0,0,85,90,3,12,6,0,86,87,5,5,0,0,87,89,3,12,6,0,88,86,1,0,0,
        0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,94,1,0,0,0,92,90,
        1,0,0,0,93,85,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,
        96,98,1,0,0,0,97,95,1,0,0,0,98,172,5,6,0,0,99,100,5,21,0,0,100,101,
        3,12,6,0,101,102,5,23,0,0,102,103,3,12,6,0,103,104,5,22,0,0,104,
        105,3,12,6,0,105,106,5,24,0,0,106,172,1,0,0,0,107,108,5,25,0,0,108,
        109,3,12,6,0,109,110,5,26,0,0,110,111,3,12,6,0,111,112,5,27,0,0,
        112,172,1,0,0,0,113,117,5,2,0,0,114,115,3,12,6,0,115,116,5,1,0,0,
        116,118,1,0,0,0,117,114,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,
        119,120,1,0,0,0,120,121,1,0,0,0,121,122,5,3,0,0,122,172,1,0,0,0,
        123,124,5,28,0,0,124,129,3,10,5,0,125,126,5,5,0,0,126,128,3,10,5,
        0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,
        0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,5,29,0,0,133,134,3,12,
        6,20,134,172,1,0,0,0,135,136,5,30,0,0,136,137,3,12,6,0,137,145,5,
        31,0,0,138,139,5,46,0,0,139,140,5,7,0,0,140,141,5,44,0,0,141,142,
        5,33,0,0,142,143,3,12,6,0,143,144,5,1,0,0,144,146,1,0,0,0,145,138,
        1,0,0,0,146,147,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,149,
        1,0,0,0,149,150,5,32,0,0,150,172,1,0,0,0,151,152,5,34,0,0,152,172,
        5,44,0,0,153,154,5,35,0,0,154,172,3,12,6,17,155,156,5,10,0,0,156,
        172,3,12,6,12,157,158,5,40,0,0,158,172,3,12,6,8,159,160,5,4,0,0,
        160,161,3,12,6,0,161,162,5,6,0,0,162,172,1,0,0,0,163,172,5,47,0,
        0,164,172,5,45,0,0,165,172,5,18,0,0,166,172,5,19,0,0,167,172,5,46,
        0,0,168,169,5,46,0,0,169,170,5,20,0,0,170,172,3,12,6,1,171,82,1,
        0,0,0,171,99,1,0,0,0,171,107,1,0,0,0,171,113,1,0,0,0,171,123,1,0,
        0,0,171,135,1,0,0,0,171,151,1,0,0,0,171,153,1,0,0,0,171,155,1,0,
        0,0,171,157,1,0,0,0,171,159,1,0,0,0,171,163,1,0,0,0,171,164,1,0,
        0,0,171,165,1,0,0,0,171,166,1,0,0,0,171,167,1,0,0,0,171,168,1,0,
        0,0,172,218,1,0,0,0,173,174,10,16,0,0,174,175,5,38,0,0,175,217,3,
        12,6,17,176,177,10,15,0,0,177,178,5,39,0,0,178,217,3,12,6,16,179,
        180,10,14,0,0,180,181,5,36,0,0,181,217,3,12,6,15,182,183,10,13,0,
        0,183,184,5,37,0,0,184,217,3,12,6,14,185,186,10,11,0,0,186,187,5,
        41,0,0,187,217,3,12,6,12,188,189,10,10,0,0,189,190,5,42,0,0,190,
        217,3,12,6,11,191,192,10,9,0,0,192,193,5,43,0,0,193,217,3,12,6,10,
        194,197,10,25,0,0,195,196,5,8,0,0,196,198,5,44,0,0,197,195,1,0,0,
        0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,5,9,0,0,200,201,5,46,0,
        0,201,212,5,4,0,0,202,207,3,12,6,0,203,204,5,5,0,0,204,206,3,12,
        6,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,
        0,0,208,211,1,0,0,0,209,207,1,0,0,0,210,202,1,0,0,0,211,214,1,0,
        0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,212,1,0,
        0,0,215,217,5,6,0,0,216,173,1,0,0,0,216,176,1,0,0,0,216,179,1,0,
        0,0,216,182,1,0,0,0,216,185,1,0,0,0,216,188,1,0,0,0,216,191,1,0,
        0,0,216,194,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,
        0,0,219,13,1,0,0,0,220,218,1,0,0,0,19,21,27,35,47,52,67,69,80,90,
        95,119,129,147,171,197,207,212,216,218
    ]

class YAPLParser ( Parser ):

    grammarFileName = "YAPL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'('", "','", "')'", 
                     "':'", "'@'", "'.'", "'~'", "'(*'", "'*)'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'=>'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "<INVALID>", "'<'", "'<='", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OPEN_COMMENT", 
                      "CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", "WHITESPACE", 
                      "CLASS", "INHERITS", "TRUE", "FALSE", "ASSIGNMENT", 
                      "IF", "ELSE", "THEN", "FI", "WHILE", "LOOP", "POOL", 
                      "LET", "IN", "CASE", "OF", "ESAC", "CASEARR", "NEW", 
                      "ISVOID", "ADD", "MINUS", "MULT", "DIV", "NOT", "LT", 
                      "LE", "EQ", "TYPE", "STR", "ID", "INT" ]

    RULE_start = 0
    RULE_program = 1
    RULE_class_exp = 2
    RULE_feature = 3
    RULE_formal = 4
    RULE_declaration = 5
    RULE_expr = 6

    ruleNames =  [ "start", "program", "class_exp", "feature", "formal", 
                   "declaration", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    OPEN_COMMENT=11
    CLOSE_COMMENT=12
    COMMENT=13
    ONE_LINE_COMMENT=14
    WHITESPACE=15
    CLASS=16
    INHERITS=17
    TRUE=18
    FALSE=19
    ASSIGNMENT=20
    IF=21
    ELSE=22
    THEN=23
    FI=24
    WHILE=25
    LOOP=26
    POOL=27
    LET=28
    IN=29
    CASE=30
    OF=31
    ESAC=32
    CASEARR=33
    NEW=34
    ISVOID=35
    ADD=36
    MINUS=37
    MULT=38
    DIV=39
    NOT=40
    LT=41
    LE=42
    EQ=43
    TYPE=44
    STR=45
    ID=46
    INT=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(YAPLParser.ProgramContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = YAPLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.program()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YAPLParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EndContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(YAPLParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd" ):
                return visitor.visitEnd(self)
            else:
                return visitor.visitChildren(self)


    class Class_listContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def class_exp(self):
            return self.getTypedRuleContext(YAPLParser.Class_expContext,0)

        def program(self):
            return self.getTypedRuleContext(YAPLParser.ProgramContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_list" ):
                return visitor.visitClass_list(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = YAPLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YAPLParser.CLASS]:
                localctx = YAPLParser.Class_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.class_exp()
                self.state = 17
                self.match(YAPLParser.T__0)
                self.state = 18
                self.program()
                pass
            elif token in [YAPLParser.EOF]:
                localctx = YAPLParser.EndContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(YAPLParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(YAPLParser.CLASS, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.TYPE)
            else:
                return self.getToken(YAPLParser.TYPE, i)

        def INHERITS(self):
            return self.getToken(YAPLParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.FeatureContext)
            else:
                return self.getTypedRuleContext(YAPLParser.FeatureContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_class_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_exp" ):
                return visitor.visitClass_exp(self)
            else:
                return visitor.visitChildren(self)




    def class_exp(self):

        localctx = YAPLParser.Class_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(YAPLParser.CLASS)
            self.state = 24
            self.match(YAPLParser.TYPE)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YAPLParser.INHERITS:
                self.state = 25
                self.match(YAPLParser.INHERITS)
                self.state = 26
                self.match(YAPLParser.TYPE)


            self.state = 29
            self.match(YAPLParser.T__1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YAPLParser.ID:
                self.state = 30
                self.feature()
                self.state = 31
                self.match(YAPLParser.T__0)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(YAPLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YAPLParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MethodContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)

        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.FormalContext)
            else:
                return self.getTypedRuleContext(YAPLParser.FormalContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)


    class AttributeContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)
        def ASSIGNMENT(self):
            return self.getToken(YAPLParser.ASSIGNMENT, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)



    def feature(self):

        localctx = YAPLParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = YAPLParser.MethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(YAPLParser.ID)
                self.state = 41
                self.match(YAPLParser.T__3)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==YAPLParser.ID:
                    self.state = 42
                    self.formal()
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==YAPLParser.T__4:
                        self.state = 43
                        self.match(YAPLParser.T__4)
                        self.state = 44
                        self.formal()
                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                self.match(YAPLParser.T__5)
                self.state = 56
                self.match(YAPLParser.T__6)
                self.state = 57
                self.match(YAPLParser.TYPE)
                self.state = 58
                self.match(YAPLParser.T__1)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(YAPLParser.T__2)
                pass

            elif la_ == 2:
                localctx = YAPLParser.AttributeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(YAPLParser.ID)
                self.state = 63
                self.match(YAPLParser.T__6)
                self.state = 64
                self.match(YAPLParser.TYPE)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YAPLParser.ASSIGNMENT:
                    self.state = 65
                    self.match(YAPLParser.ASSIGNMENT)
                    self.state = 66
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def getRuleIndex(self):
            return YAPLParser.RULE_formal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal" ):
                return visitor.visitFormal(self)
            else:
                return visitor.visitChildren(self)




    def formal(self):

        localctx = YAPLParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(YAPLParser.ID)
            self.state = 72
            self.match(YAPLParser.T__6)
            self.state = 73
            self.match(YAPLParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def ASSIGNMENT(self):
            return self.getToken(YAPLParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = YAPLParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(YAPLParser.ID)
            self.state = 76
            self.match(YAPLParser.T__6)
            self.state = 77
            self.match(YAPLParser.TYPE)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YAPLParser.ASSIGNMENT:
                self.state = 78
                self.match(YAPLParser.ASSIGNMENT)
                self.state = 79
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YAPLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LetInContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(YAPLParser.LET, 0)
        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(YAPLParser.DeclarationContext,i)

        def IN(self):
            return self.getToken(YAPLParser.IN, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetIn" ):
                return visitor.visitLetIn(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(YAPLParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(YAPLParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class DispatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispatch" ):
                return visitor.visitDispatch(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(YAPLParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(YAPLParser.LOOP, 0)
        def POOL(self):
            return self.getToken(YAPLParser.POOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class DivisionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def DIV(self):
            return self.getToken(YAPLParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)


    class NewObjectContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(YAPLParser.NEW, 0)
        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewObject" ):
                return visitor.visitNewObject(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def LT(self):
            return self.getToken(YAPLParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class BlockContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)


    class NegIntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegInteger" ):
                return visitor.visitNegInteger(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(YAPLParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def THEN(self):
            return self.getToken(YAPLParser.THEN, 0)
        def ELSE(self):
            return self.getToken(YAPLParser.ELSE, 0)
        def FI(self):
            return self.getToken(YAPLParser.FI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class CaseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(YAPLParser.CASE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def OF(self):
            return self.getToken(YAPLParser.OF, 0)
        def ESAC(self):
            return self.getToken(YAPLParser.ESAC, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.ID)
            else:
                return self.getToken(YAPLParser.ID, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.TYPE)
            else:
                return self.getToken(YAPLParser.TYPE, i)
        def CASEARR(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.CASEARR)
            else:
                return self.getToken(YAPLParser.CASEARR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase" ):
                return visitor.visitCase(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def ADD(self):
            return self.getToken(YAPLParser.ADD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class StarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def MULT(self):
            return self.getToken(YAPLParser.MULT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar" ):
                return visitor.visitStar(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def ASSIGNMENT(self):
            return self.getToken(YAPLParser.ASSIGNMENT, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(YAPLParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(YAPLParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class CallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class StrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(YAPLParser.STR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr" ):
                return visitor.visitStr(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def EQ(self):
            return self.getToken(YAPLParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class IsVoidContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(YAPLParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsVoid" ):
                return visitor.visitIsVoid(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(YAPLParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class LessEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def LE(self):
            return self.getToken(YAPLParser.LE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEqual" ):
                return visitor.visitLessEqual(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = YAPLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = YAPLParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 83
                self.match(YAPLParser.ID)
                self.state = 84
                self.match(YAPLParser.T__3)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YAPLParser.T__1) | (1 << YAPLParser.T__3) | (1 << YAPLParser.T__9) | (1 << YAPLParser.TRUE) | (1 << YAPLParser.FALSE) | (1 << YAPLParser.IF) | (1 << YAPLParser.WHILE) | (1 << YAPLParser.LET) | (1 << YAPLParser.CASE) | (1 << YAPLParser.NEW) | (1 << YAPLParser.ISVOID) | (1 << YAPLParser.NOT) | (1 << YAPLParser.STR) | (1 << YAPLParser.ID) | (1 << YAPLParser.INT))) != 0):
                    self.state = 85
                    self.expr(0)
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==YAPLParser.T__4:
                        self.state = 86
                        self.match(YAPLParser.T__4)
                        self.state = 87
                        self.expr(0)
                        self.state = 92
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 98
                self.match(YAPLParser.T__5)
                pass

            elif la_ == 2:
                localctx = YAPLParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(YAPLParser.IF)
                self.state = 100
                self.expr(0)
                self.state = 101
                self.match(YAPLParser.THEN)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(YAPLParser.ELSE)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.match(YAPLParser.FI)
                pass

            elif la_ == 3:
                localctx = YAPLParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(YAPLParser.WHILE)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(YAPLParser.LOOP)
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(YAPLParser.POOL)
                pass

            elif la_ == 4:
                localctx = YAPLParser.BlockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(YAPLParser.T__1)
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.expr(0)
                    self.state = 115
                    self.match(YAPLParser.T__0)
                    self.state = 119 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YAPLParser.T__1) | (1 << YAPLParser.T__3) | (1 << YAPLParser.T__9) | (1 << YAPLParser.TRUE) | (1 << YAPLParser.FALSE) | (1 << YAPLParser.IF) | (1 << YAPLParser.WHILE) | (1 << YAPLParser.LET) | (1 << YAPLParser.CASE) | (1 << YAPLParser.NEW) | (1 << YAPLParser.ISVOID) | (1 << YAPLParser.NOT) | (1 << YAPLParser.STR) | (1 << YAPLParser.ID) | (1 << YAPLParser.INT))) != 0)):
                        break

                self.state = 121
                self.match(YAPLParser.T__2)
                pass

            elif la_ == 5:
                localctx = YAPLParser.LetInContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(YAPLParser.LET)
                self.state = 124
                self.declaration()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==YAPLParser.T__4:
                    self.state = 125
                    self.match(YAPLParser.T__4)
                    self.state = 126
                    self.declaration()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 132
                self.match(YAPLParser.IN)
                self.state = 133
                self.expr(20)
                pass

            elif la_ == 6:
                localctx = YAPLParser.CaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(YAPLParser.CASE)
                self.state = 136
                self.expr(0)
                self.state = 137
                self.match(YAPLParser.OF)
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 138
                    self.match(YAPLParser.ID)
                    self.state = 139
                    self.match(YAPLParser.T__6)
                    self.state = 140
                    self.match(YAPLParser.TYPE)
                    self.state = 141
                    self.match(YAPLParser.CASEARR)
                    self.state = 142
                    self.expr(0)
                    self.state = 143
                    self.match(YAPLParser.T__0)
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==YAPLParser.ID):
                        break

                self.state = 149
                self.match(YAPLParser.ESAC)
                pass

            elif la_ == 7:
                localctx = YAPLParser.NewObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(YAPLParser.NEW)
                self.state = 152
                self.match(YAPLParser.TYPE)
                pass

            elif la_ == 8:
                localctx = YAPLParser.IsVoidContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(YAPLParser.ISVOID)
                self.state = 154
                self.expr(17)
                pass

            elif la_ == 9:
                localctx = YAPLParser.NegIntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(YAPLParser.T__9)
                self.state = 156
                self.expr(12)
                pass

            elif la_ == 10:
                localctx = YAPLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(YAPLParser.NOT)
                self.state = 158
                self.expr(8)
                pass

            elif la_ == 11:
                localctx = YAPLParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(YAPLParser.T__3)
                self.state = 160
                self.expr(0)
                self.state = 161
                self.match(YAPLParser.T__5)
                pass

            elif la_ == 12:
                localctx = YAPLParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(YAPLParser.INT)
                pass

            elif la_ == 13:
                localctx = YAPLParser.StrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(YAPLParser.STR)
                pass

            elif la_ == 14:
                localctx = YAPLParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 165
                self.match(YAPLParser.TRUE)
                pass

            elif la_ == 15:
                localctx = YAPLParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 166
                self.match(YAPLParser.FALSE)
                pass

            elif la_ == 16:
                localctx = YAPLParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 167
                self.match(YAPLParser.ID)
                pass

            elif la_ == 17:
                localctx = YAPLParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(YAPLParser.ID)
                self.state = 169
                self.match(YAPLParser.ASSIGNMENT)
                self.state = 170
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 216
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = YAPLParser.StarContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 174
                        self.match(YAPLParser.MULT)
                        self.state = 175
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = YAPLParser.DivisionContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 177
                        self.match(YAPLParser.DIV)
                        self.state = 178
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = YAPLParser.AddContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 180
                        self.match(YAPLParser.ADD)
                        self.state = 181
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = YAPLParser.MinusContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 183
                        self.match(YAPLParser.MINUS)
                        self.state = 184
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = YAPLParser.LessThanContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 185
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 186
                        self.match(YAPLParser.LT)
                        self.state = 187
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = YAPLParser.LessEqualContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 189
                        self.match(YAPLParser.LE)
                        self.state = 190
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = YAPLParser.EqualContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 192
                        self.match(YAPLParser.EQ)
                        self.state = 193
                        self.expr(10)
                        pass

                    elif la_ == 8:
                        localctx = YAPLParser.DispatchContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 197
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==YAPLParser.T__7:
                            self.state = 195
                            self.match(YAPLParser.T__7)
                            self.state = 196
                            self.match(YAPLParser.TYPE)


                        self.state = 199
                        self.match(YAPLParser.T__8)
                        self.state = 200
                        self.match(YAPLParser.ID)
                        self.state = 201
                        self.match(YAPLParser.T__3)
                        self.state = 212
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YAPLParser.T__1) | (1 << YAPLParser.T__3) | (1 << YAPLParser.T__9) | (1 << YAPLParser.TRUE) | (1 << YAPLParser.FALSE) | (1 << YAPLParser.IF) | (1 << YAPLParser.WHILE) | (1 << YAPLParser.LET) | (1 << YAPLParser.CASE) | (1 << YAPLParser.NEW) | (1 << YAPLParser.ISVOID) | (1 << YAPLParser.NOT) | (1 << YAPLParser.STR) | (1 << YAPLParser.ID) | (1 << YAPLParser.INT))) != 0):
                            self.state = 202
                            self.expr(0)
                            self.state = 207
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==YAPLParser.T__4:
                                self.state = 203
                                self.match(YAPLParser.T__4)
                                self.state = 204
                                self.expr(0)
                                self.state = 209
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 214
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 215
                        self.match(YAPLParser.T__5)
                        pass

             
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 25)
         




