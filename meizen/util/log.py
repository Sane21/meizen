import datetime

from .io import write


def logger(msg: str):
    print(msg)


def debug(msg: str):
    print("[debug_log] : " + msg)


class Logger:
    __filename__: str
    _user: str
    _date: str
    _dncl: str
    _py: str
    _std_out: str
    _err_out: str

    def __init__(self, user):
        """
        コンストラクタ
        :param user: USERの識別子を記入
        """
        self._user = user
        self._date = str(datetime.datetime.now())
        self.__filename__ = "log_" + self._user + "_" + self._date + ".md"
        content = ["# " + self._user, self._date]
        write(path="./" + self.__filename__, code_list=content)
        self._dncl = "None"
        self._py = "None"
        self._std_out = "None"
        self._err_out = "None"

    def dncl(self, msg: str, code_list: list[str]):
        """
        DNCLファイルに関する出力
        :param code_list: 記録するDNCLファイルの内容
        :param msg: 表示するメッセージ
        :return:
        """
        self._dncl = ""
        for code in code_list:
            self._dncl += code + "\n"
        logger(msg=msg)

    def py(self, msg: str, code_list: list[str]):
        """
        Pyファイルに関する出力
        :param code_list: 実行するPyファイルの内容
        :param msg: 表示するメッセージ
        :return:
        """
        self._py = ""
        for code in code_list:
            self._py += code + "\n"
        logger(msg=msg)

    def std_out(self, msg: str, code: str):
        """
        標準出力に関する出力
        :param msg: 表示するメッセージ
        :param code: 標準出力の内容
        :return:
        """
        self._std_out = code
        logger(msg=msg)
        logger(msg=code)

    def err_out(self, msg: str, code: str):
        """
        エラー出力に関する出力
        :param msg: 表示するメッセージ
        :param code: エラー出力のの内容
        :return:
        """
        self._err_out = code
        logger(msg=msg)
        logger(msg=code)

    def dump(self, path="./"):
        self._date = str(datetime.datetime.now())
        content = ["## " + self._date,
                   "'''dncl",
                   self._dncl,
                   "'''",
                   "'''py",
                   self._py,
                   "'''"]
        if self._std_out is not "None":
            content += ["'''std_out",
                        self._std_out,
                        "'''",
                        "'''err_out",
                        self._err_out,
                        "'''"]
        print(content)

        write(path=path + self.__filename__, mode="a", code_list=content)

    def get_file(self) -> str:
        return self.__filename__
