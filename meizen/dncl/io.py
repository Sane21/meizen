# 読み込み
def load(path: str) -> list:
    file = open(path, 'r', encoding="utf-8")
    data: list = file.readlines()
    file.close()
    return data


# 書き込み
def write(path: str, code_list: list[str]):
    file = open(path, 'w')
    for code in code_list:
        file.write(code+"\n")
        # print(code)
    file.close()
    return
