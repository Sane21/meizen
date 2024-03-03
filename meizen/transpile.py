from .dncl.lexer import compile_code
from .util.run import run as util_run


def make(path: str, filename: str):
    """
    legacy : 処理はbuildに委譲
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    build(path, filename)


def build(path: str, filename: str):
    """
    DNCLからPythonへの翻訳関数
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    compile_code(path=path, filename=filename)


def run(path: str, filename: str):
    """
    DNCLからPythonへの翻訳-実行関数
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成し、filename.pyを実行する
    作成部はbuildに委譲
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    build(path=path, filename=filename)
    util_run(path=path + filename + ".py")


def make_run(path: str, filename: str):
    """
    legacy : 処理はrunに委譲
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成し、filename.pyを実行する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    """
    run(path, filename)
