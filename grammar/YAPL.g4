grammar YAPL;
import Lex;

options{
    language = Python3;
}

start 
    : program
    ;

program 
    : class_exp ';' program        # class_list
    | EOF                          # end
    ;

class_exp
    : CLASS TYPE (INHERITS TYPE)? '{' (feature ';')* '}'
    ;

feature 
    : ID '(' (formal (',' formal)*)* ')' ':' TYPE '{' expr '}' # method
    | ID ':' TYPE ( ASSIGNMENT expr )?                         # attribute
    ;

formal 
    : ID ':' TYPE 
    ;

declaration
    : ID ':' TYPE ( ASSIGNMENT expr )?
    ;

expr
    : expr ('@' TYPE)? '.' ID '(' ( expr (',' expr)* )* ')'         # dispatch
    | ID '(' ( expr (',' expr)* )* ')'                              # call
    | IF expr THEN expr ELSE expr FI                                # if
    | WHILE expr LOOP expr POOL                                     # while
    | '{' (expr ';') + '}'                                          # block
    | LET declaration (',' declaration)* IN expr                    # letIn
    | CASE expr OF (ID ':' TYPE CASEARR expr ';') + ESAC            # case
    | NEW TYPE                                                      # newObject
    | ISVOID expr                                                   # isVoid
    | expr MULT expr                                                # star
    | expr DIV expr                                                 # division
    | expr ADD expr                                                 # add
    | expr MINUS expr                                               # minus
    | '~' expr                                                      # negInteger
    | expr LT expr                                                  # lessThan
    | expr LE expr                                                  # lessEqual
    | expr EQ expr                                                  # equal
    | NOT expr                                                      # negation
    | '('expr')'                                                    # parenthesis
    | INT                                                           # int
    | STR                                                           # str
    | TRUE                                                          # true
    | FALSE                                                         # false
    | ID                                                            # id
    | ID ASSIGNMENT expr                                            # assignment
    ;

