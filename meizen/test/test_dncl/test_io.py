from meizen.dncl.io import load, write


def test_load():
    path = "C:/Users/readb/pycharm/meizen/meizen/dncl/sample/test.dncl"
    code_list: list = load(path=path)
    print(len(code_list))
    for code in code_list:
        print(code)


def test_write():
    path = "C:/Users/readb/pycharm/meizen/meizen/dncl/sample/sample.hoge"
    msg: list = ["# hoge", "# test"]
    write(path=path, code_list=msg)


test_load()