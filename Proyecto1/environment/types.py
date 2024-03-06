from enum import Enum

class ExpressionType(Enum):
    INTEGER = 0
    FLOAT = 1
    STRING = 2
    BOOLEAN = 3
    ARRAY = 4
    STRUCT = 5
    NULL = 6
    BREAK = 7
    CONTINUE = 8
    RETURN = 9