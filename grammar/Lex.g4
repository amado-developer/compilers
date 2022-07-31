lexer grammar Lex;


// comments
OPEN_COMMENT
   : '(*'
   ;
CLOSE_COMMENT
   : '*)'
   ;
COMMENT
   : OPEN_COMMENT (COMMENT | .)*? CLOSE_COMMENT -> skip
   ;
ONE_LINE_COMMENT
   : '--' (~ '\n')* '\n'? -> skip
   ;

WHITESPACE
   : [ \t\r\n\f\\] + -> skip
   ;

// Keywords

CLASS : C L A S S;

INHERITS : I N H E R I T S;

TRUE : 't' R U E ;

FALSE : 'f' A L S E ;

ASSIGNMENT : '<-' ;

IF : I F ;

ELSE : E L S E ;

THEN : T H E N ;

FI : F I ;

WHILE : W H I L E ;

LOOP : L O O P ;

POOL : P O O L ;

LET : L E T ;

IN : I N ;

CASE : C A S E ;

OF : O F ;

ESAC : E S A C ;

CASEARR : '=>' ;

NEW : N E W ;

ISVOID : I S V O I D ;

ADD : '+' ;

MINUS : '-' ;

MULT : '*' ;

DIV : '/' ;

NOT : N O T ;

LT : '<' ;

LE : '<=' ;

EQ : '=' ;

TYPE : [A-Z]([a-zA-Z0-9]|'_')*;

STR : '"' .*? '"';

ID : [a-z]([a-zA-Z0-9]|'_')*;

INT : [0-9]+;


fragment A: [Aa];
fragment B: [Bb];
fragment C: [Cc];
fragment D: [Dd];
fragment E: [Ee];
fragment F: [Ff];
fragment G: [Gg];
fragment H: [Hh];
fragment I: [Ii];
fragment J: [Jj];
fragment K: [Kk];
fragment L: [Ll];
fragment M: [Mm];
fragment N: [Nn];
fragment O: [Oo];
fragment P: [Pp];
fragment Q: [Qq];
fragment R: [Rr];
fragment S: [Ss];
fragment T: [Tt];
fragment U: [Uu];
fragment V: [Vv];
fragment W: [Ww];
fragment X: [Xx];
fragment Y: [Yy];
fragment Z: [Zz];
fragment BACK: [\][.*];
