# 読み込み
def load(path: str) -> list:
    file = open(path, 'r')
    data = file.readlines()
    file.close()
    return data


# 書き込み
def write(path: str, code_list: list):
    file = open(path, 'w')
    for code in code_list:
        file.write(code)
    file.close()
    return
