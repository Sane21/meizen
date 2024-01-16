from enum import StrEnum


class Symbol:
    # 初期値
    NULL = "NONE"
    # 解析中
    ON_ANALYSE = ""

    # 構文系
    IF = "もし"
    THEN = "ならば"
    ELIF = "そうでなくもし"
    ELSE = "そうでなければ"
    WHILE = "の間"
    BREAK = "break"
    CONTINUE = "continue"
    FOR_L = "を"
    FOR_M = "から"
    FOR_N = "まで"
    FOR_INC = "ずつ増やしながら繰り返す"
    FOR_DEC = "ずつ減らしながら繰り返す"
    FUNCTION = "関数"
    PRINT = "表示する"

    # 真偽値系
    TRUE = "True"
    TRUE_JP = "真"
    FALSE = "False"
    FALSE_JP = "偽"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS = "<"
    GREAT = ">"
    LESS_EQUAL = "<="
    GREAT_EQUAL = ">="
    AND = "&&"
    OR = "||"
    NOT = "!"

    # 数式系
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    DIV_INT = "//"
    MOD = "%"
    ASSIGN = "="
    ASSIGN_ADD = "+="
    ASSIGN_SUB = "-="
    ASSIGN_MUL = "*="
    ASSIGN_DIV = "/="
    ASSIGN_DIV_INT = "//="
    ASSIGN_MOD = "%="
    INCREMENT = "++"
    DECREMENT = "--"

    # 記号系
    L_PAREN = "("
    R_PAREN = ")"
    L_BRACKET = "["
    R_BRACKET = "]"
    QUOTATION = "\""
    COMMA = ","
    DOT = "."
    SPACE = " "
    CORON = ":"
    SEMI_CORON = ";"

    # 値系
    INTEGER = "int"
    FLOAT = "float"
    STRING = "str"
    NAME = "変数名"
    CONST_NAME = "NAME"
    ARRAY_NAME = "Name"
    VAR_NAME = "name"
    ERROR = "error"

    # 段落系
    RETURN = "\n"
    INDENT = "\t"
    EOF = "\0"

