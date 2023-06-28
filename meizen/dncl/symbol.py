from enum import Enum


class Symbol(Enum):
    NULL = None
    L_IF = "もし"
    R_IF = "ならば"
    L_ELIF = "そうでなくもし"
    ELSE = "そうでなければ"
    WHILE = "の間"
    BREAK = "break"
    FOR_L = "を"
    FOR_M = "から"
    FOR_N = "まで"
    FOR_INC = "ずつ増やしながら繰り返す"
    FOR_DEC = "ずつ減らしながら繰り返す"
    TRUE = "True"
    TRUE = "真"
    FALSE = "False"
    FALSE = "偽"



