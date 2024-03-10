from .dncl.lexer import compile_code
from .util.run import run as util_run
from .util.regEx import check_str, check_re
from .util.log import logger


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
    logger(":----------翻訳を開始します----------:")
    compile_code(path=path, filename=filename)


def run(path: str, filename: str) -> (str, str):
    """
    DNCLからPythonへの翻訳-実行関数
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成し、filename.pyを実行する
    処理はdoに委譲
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    do(path=path, filename=filename)


def make_run(path: str, filename: str):
    """
    legacy : 処理はrunに委譲
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成し、filename.pyを実行する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    """
    run(path, filename)


def do(path: str, filename: str) -> (str, str):
    """
    DNCLからPythonへの翻訳-実行関数
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成し、filename.pyを実行する
    作成部はbuildに委譲
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return: 実行結果の標準出力, エラー出力
    """
    build(path=path, filename=filename)
    result = util_run(path=path + filename + ".py")
    return result


def exam_re(path: str, filename: str, answer: str):
    """
    変換と実行、実行結果の正規表現による確認まで行う関数
    python標準のreパッケージのfullmatchに基づく
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename:読み取るファイル名 (拡張子は除く)
    :param answer: 確認する正規表現
    :return:
    """
    out, _ = do(path=path, filename=filename)
    result: bool = check_re(sentence=out, pattern=answer)
    logger(":----------出力を確認します----------:")
    if result:
        logger("出力は正常です.")
    else:
        logger("出力に不備があります.想定される出力は次の通りです.")
        logger(answer)
    logger(":-----------確認は以上です-----------:")


def exam_str(path: str, filename: str, answer: str):
    """
    変換と実行、実行結果の文字列による確認まで行う関数
    完全一致のみを正答とする
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename:読み取るファイル名 (拡張子は除く)
    :param answer: 確認する文字列
    :return:
    """
    out, _ = do(path=path, filename=filename)
    result: bool = check_str(sentence=out, string=answer)
    logger(":----------出力を確認します----------:")
    if result:
        logger("出力は正常です.")
    else:
        logger("出力に不備があります.想定される出力は次の通りです.")
        logger(answer)
    logger(":-----------確認は以上です-----------:")
