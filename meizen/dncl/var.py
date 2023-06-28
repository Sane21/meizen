from type import NameType


class Variable:
    """変数クラス
    name_type: NameType型 変数型
    name: str型 変数名
    address: int型 変数の格納場所の番地
    """
    __name_type: NameType
    __name: str
    __address: str

    def __int__(self, name_type: NameType, name: str, address: str):
        """
        コンストラクタ
        :param name_type: 変数型名, NameType型
        :param name: 変数名, str型
        :param address: 変数の格納場所, int
        :return: self
        """
        self.__name_type = name_type
        self.__name = name
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @property
    def name_type(self) -> NameType:
        return self.__name_type

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

