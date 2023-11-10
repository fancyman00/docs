from enum import Enum


class Types(Enum):
    IN = 1
    OUT = 2
    INNER = 3

    def get_name(self):
        return TYPES_NAME[self]


class Links(Enum):
    IN_OUT = 1
    OUT_IN = 2
    INNER_INNER = 3

    def get_name(self):
        return LINKS_NAME[self]


LINKS_NAME = {
    Links.IN_OUT: "Входящий-Исходящий",
    Links.OUT_IN: "Исходящий-Входящий",
    Links.INNER_INNER: "Внутренний-Внутренний",
}

TYPES_NAME = {
    Types.IN: "Входящий",
    Types.OUT: "Исходящий",
    Types.INNER: "Внутренний",
}
