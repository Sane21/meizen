import subprocess


def run(path: str) -> (str, str):
    """
    実行関数
    pathに存在する.pyファイルをsubprocessで実行し、標準出力とエラー出力をそれぞれ表示する
    :param path: 実行したいpythonファイル
    :return: 標準出力結果, エラー出力結果
    """
    command = ["python", path]
    result = do(command=command)
    return result


def run_args(path: str, args: list[str]):
    """
    実行関数
    pathに存在する.pyファイルに引数argsを渡してsubprocessで実行し、標準出力とエラー出力をそれぞれ表示する
    :param path: 実行したpythonファイル
    :param args: 実行時に渡す引数
    :return: 標準出力結果, エラー出力結果
    """
    command = ["python", path]
    command += args
    result = do(command=command)
    return result


def do(command: list) -> (str, str):
    """
    実行関数の本処理, 引数をsubprocessで実行する
    :param command: 実行するコマンド
    :return: 標準出力結果, エラー出力結果
    """
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    output = result.stdout
    err = result.stderr
    return output, err
