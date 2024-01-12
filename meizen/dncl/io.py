def load(path: str) -> list:
    file = open(path, 'r')
    data = file.readlines()
    return data
