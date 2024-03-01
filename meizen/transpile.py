from .dncl.lexer import compile_code
from .util.run import run as util_run


def make(path: str, filename: str):
    """
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    build(path, filename)


def build(path: str, filename: str):
    compile_code(path=path, filename=filename)


def run(path: str, filename: str):
    compile_code(path=path, filename=filename)
    util_run(path=path + filename + ".py")


def make_run(path: str, filename: str):
    run(path, filename)
