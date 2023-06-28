from enum import Enum, auto


class ValueType(Enum):
    """値の型を定義するenum
    INT(整数), FLOAT(浮動小数点数), BOOL(真偽値), STRING(文字列), NULL
    """
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STRING = auto()
    NULL = auto()


class NameType(Enum):
    """命名の型を定義するenum
    CONST(定数), ARRAY(配列), VARIABLE(変数)
    """
    CONST = auto()
    ARRAY = auto()
    VARIABLE = auto()
