# Valueクラス, address, value_type, valueを保持する
# ValueTableクラス, Valueの一覧を保持,addressの使用状況を管理, 使用可能なaddressを返却
from .type import ValueType


class Value:
    """
    基本値型
    """
    __address: int
    __value_type: ValueType
    __value: object

    def __init__(self, address: int, value_type: ValueType, value: object):
        self.__address = address
        self.__value_type = value_type
        self.__value = value

    @property
    def address(self) -> int:
        return self.__address

    @property
    def value_type(self) -> ValueType:
        return self.__value_type

    @property
    def value(self):
        return self.__value


class Array(Value):
    """
    配列値型
    """
    __array: list

    def __init__(self, address: int, value_type: ValueType, value: object):
        """
        Arrayの配列型
        :param address: 番地
        :param value_type: 型
        :param value: 値
        """
        super().__init__(address, value_type, value)
        self.__array = []

    def append(self, value: Value):
        self.__array.append(value)


class ValueTable:
    __value_list: dict


class AddressManager:
    # Singletonにしよう, 別ファイルでも良いかなあ
    __using_addresses: list = []
    __current_address: int = 0

    def next_address(self):
        self.__using_addresses.append(self.__current_address)
        self.__current_address += 1
        return self.__current_address

