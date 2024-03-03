import subprocess


def run(path: str):
    """
    実行関数
    pathに存在する.pyファイルをsubprocessで実行し、標準出力とエラー出力をそれぞれ表示する
    :param path: 実行したいpythonファイル
    :return:
    """
    command = ["python", path]
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    output = result.stdout
    err = result.stderr
    print("コマンドを実行: " + str(command))
    print(output)
    print(err)


def run_args(path: str, args: list[str]):
    """
    実行関数
    pathに存在する.pyファイルに引数argsを渡してsubprocessで実行し、標準出力とエラー出力をそれぞれ表示する
    :param path: 実行したpythonファイル
    :param args: 実行時に渡す引数
    :return:
    """
    command = ["python", path]
    command += args
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    output = result.stdout
    err = result.stderr
    print("コマンドを実行: " + str(command))
    print(output)
    print(err)
