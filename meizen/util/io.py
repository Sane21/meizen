# 読み込み
def load(path: str) -> list:
    """
    外部ファイルの読み取り関数
    pathのファイルをutf-8でエンコードする
    :param path: ファイルのパス
    :return: 読み取り結果(1行ごと)
    """
    file = open(path, 'r', encoding="utf-8")
    data: list = file.readlines()
    file.close()
    return data


# 書き込み
def write(path: str, code_list: list[str], mode="w"):
    """
    書き込み関数
    pathのファイルが存在している場合の挙動はmodeで設定する(初期値は上書き)
    :param path: ファイルのパス
    :param code_list: 書き込む内容(1行ごと)
    :param mode: 書き込みモードの選択 追記ならa
    :return: なし
    """
    file = open(path, mode=mode, encoding="utf-8")
    for code in code_list:
        file.write(code+"\n")
        print(code)
    file.close()
    return
