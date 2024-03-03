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
def write(path: str, code_list: list[str]):
    """
    書き込み関数
    pathのファイルが存在していれば上書きし、なければ作成し書き込む
    :param path: ファイルのパス
    :param code_list: 書き込む内容(1行ごと)
    :return: なし
    """
    file = open(path, 'w', encoding="utf-8")
    for code in code_list:
        file.write(code+"\n")
        # print(code)
    file.close()
    return
