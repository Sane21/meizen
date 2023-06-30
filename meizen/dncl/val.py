# Valueクラス, address, value_type, valueを保持する
# ValueTableクラス, Valueの一覧を保持,addressの使用状況を管理, 使用可能なaddressを返却
from .type import ValueType


class Value:
    __address: str
    __value_type: ValueType
    __value: object

    def __init__(self, address: str, value_type: ValueType, value: object):
        self.__address = address
        self.__value_type = value_type
        self.__value = value

    @property
    def address(self) -> str:
        return self.__address

    @property
    def value_type(self) -> ValueType:
        return self.__value_type

    @property
    def value(self):
        return self.__value
