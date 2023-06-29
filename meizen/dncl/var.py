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

    def __init__(self, name_type: NameType, name: str, address: str):
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


class VariableTable:
    """
    変数,定数,配列の一覧を管理するクラス
    """
    __var_list: dict
    __name_type: NameType

    def __init__(self, name_type: NameType):
        self.__var_list = dict()
        self.__type = name_type

    def is_exit_key(self, name: str) -> bool:
        """
        keyが存在するかどうかを確認するメソッド
        :param name: keyとして存在するかどうか確認したい値(str)
        :return: 存在の是非(bool)
        """
        for item in self.__var_list.keys():
            if item == name:
                return True
        return False

    def get(self, name: str) -> Variable:
        """変数のゲッター
        nameの変数名が存在する場合、該当する変数を返す。なければNone。
        :param name: 変数名(str)
        :return: 変数(Variable)
        """
        if self.is_exit_key(name):
            return self.__var_list.get(name)

    def append(self, name: str, address: str):
        """変数の追加登録
        同名の変数が存在しない場合のみ追加処理を行う
        :param name: 変数名(str)
        :param address: 番地(str)
        :return:
        """
        if not self.is_exit_key(name):
            self.__var_list[name] = Variable(name_type=self.__name_type, name=name, address=address)
