class Symbol:
    """
    字句の種類を示すclass, enumみたいな運用
    """
    # 初期値
    NULL = "NONE"
    # 解析中
    ON_ANALYSE = ""

    # 構文系
    IF = "もし"
    THEN = "ならば"
    ELIF = "そうでなくもし"
    ELSE = "そうでなければ"
    WHILE = "の間繰り返す"
    BREAK = "break"
    CONTINUE = "continue"
    FOR_L = "を"
    FOR_M = "から"
    FOR_N = "まで"
    FOR_INC = "ずつ増やしながら繰り返す"
    FOR_DEC = "ずつ減らしながら繰り返す"

    # 関数系
    FUNCTION = "関数"
    PRINT = "表示する"
    INPUT = "【外部からの入力】"
    FUNC_LENGTH = "要素数"
    FUNC_RANDOM = "乱数"
    FUNC_INT = "整数"
    FUNC_STR = "文字列"
    FUNC_FLOAT = "少数"

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
    DIV_JP = "÷"
    DIV_INT = "//"
    MOD = "%"
    ASSIGN = "="
    ASSIGN_ARROW = "←"
    ASSIGN_ADD = "+="
    ASSIGN_SUB = "-="
    ASSIGN_MUL = "*="
    ASSIGN_DIV = "/="
    ASSIGN_DIV_JP = "÷="
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
    L_KAKKO_JP = "「"
    R_KAKKO_JP = "」"

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

