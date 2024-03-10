from .dncl.lexer import lexical_analyse, parse
from .util.run import run as util_run
from .util.regEx import check_str, check_re
from .util.log import logger
from .util.io import load, write


def make(path: str, filename: str):
    """
    legacy : 処理はbuildに委譲
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    build(path, filename)


def build(filename: str, path: str = "./"):
    """
    DNCLからPythonへの翻訳関数
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス (default:"./")
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    logger(":----------翻訳を開始します----------:")
    compile_code(path=path, filename=filename)


def compile_code(path: str, filename: str):
    """
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    read_file_path = path + filename + ".dncl"
    write_file_path = path + filename + ".py"
    code_list: list = load(path=read_file_path)
    # ここから 最後の１行を構文解析できないことのケアとして空行を追加する処理
    code_list[len(code_list) - 1] += "\n"
    code_list.append("")
    # ここまで 消しちゃだめ
    code_word, code_symbol = lexical_analyse(code_list=code_list)
    logger("字句解析完了")
    code_list = parse(code_word=code_word, code_symbol=code_symbol)
    logger("構文解析完了")
    write(path=write_file_path, code_list=code_list)
    logger("書き込み完了")


def run(filename: str, path: str = "./") -> (str, str):
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


def exam_re(answer: str, filename: str, path: str = "./"):
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


def exam_str(answer: str, filename: str, path: str = "./"):
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
