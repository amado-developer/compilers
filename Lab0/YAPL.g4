grammar YAPL;

CLASS: 'class' | 'CLASS';

ELSE: 'else' | 'ELSE';

FI: 'fi' | 'FI';

IF: 'if' | 'IF';

IN: 'in' | 'IN';

INHERITS: 'inherits' | 'INHERITS';

WHILE: 'while' | 'WHILE';

NEW: 'new' | 'NEW';

NOT: 'not' | 'NOT';

LET: 'let' | 'LET';

FALSE: 'false';

TRUE: 'true';

ISVOID: 'isvoid' | 'ISVOID';

LOOP: 'loop' | 'LOOP';

POOL: 'pool' | 'POOL';

THEN: 'then' | 'THEN';

SEMICOLON : ';';

LCURLY : '{';

RCURLY : '}';

LSQUARE : '[';

RSQUARE : ']';

LROUND : '(';

RROUND : ')';

COMMA : ',';

POINT : '.';

INT_NOT : '~';

COLON : ':';

ASIGN : '<-';

AT : '@';

LESS_THAN : '<';

LESS_EQUAL : '<=';

EQUAL: '=';

QUOTES : '"';

APOSTROPHE : '\'';

ADD : '+';

SUB : '-';

MULTIPLY : '*';

DIVIDE : '/';


LINE_COMMENT : '--' .*?  '\n' -> skip;
COMMENT: '(*' .*? '*)' -> skip;


INTEGER: DIGIT+;

STRING: '"' ~["]*? '"';
TYPE: (UPPER (LETTER_NUM | '_')*) | SELF_TYPE;
ID: (LOWER (LETTER_NUM | '_')*) | SELF;

fragment SELF: 'self';
fragment SELF_TYPE: 'SELF_TYPE';
fragment LETTER_NUM: LETTER | DIGIT;
fragment LETTER: UPPER | LOWER;
fragment UPPER: ('A'..'Z');
fragment LOWER: ('a'..'z');
fragment DIGIT: [0-9];
WS : [ \t\r\n\f]+ -> skip ;


// Parser
program : (class SEMICOLON)+ ;
class: CLASS TYPE (INHERITS TYPE)? LCURLY (feature SEMICOLON)* RCURLY;
feature: ID LROUND ( formal (COMMA formal)* )? RROUND COLON TYPE LCURLY expr RCURLY |
         ID COLON TYPE (ASIGN expr)? ;
formal: ID COLON TYPE;
expr: ID ASIGN expr |
      expr (AT TYPE)? POINT ID LROUND ( expr (COMMA expr)* )? RROUND |
      ID LROUND ( expr (COMMA expr)* )? RROUND |
      IF expr THEN expr ELSE expr FI |
      WHILE expr LOOP expr POOL |
      LCURLY (expr SEMICOLON)+ RCURLY |
      LET ID COLON TYPE (ASIGN expr)? (COMMA ID COLON TYPE (ASIGN expr)?)* IN expr |
      NEW TYPE |
      ISVOID expr |
      expr ADD expr |
      expr SUB expr |
      expr MULTIPLY expr |
      expr DIVIDE expr |
      INT_NOT expr |
      expr LESS_THAN expr |
      expr LESS_EQUAL expr |
      expr EQUAL expr |
      NOT expr |
      LROUND expr RROUND |
      ID |
      INTEGER |
      STRING |
      TRUE |
      FALSE;