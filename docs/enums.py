from enum import Enum


class Types(Enum):
    IN = 1
    OUT = 2
    INNER = 3

    def get_name(self):
        return TYPES_NAME[self]


TYPES_NAME = {
    Types.IN: "Входящий",
    Types.OUT: "Исходящий",
    Types.INNER: "Внутренний",
}
