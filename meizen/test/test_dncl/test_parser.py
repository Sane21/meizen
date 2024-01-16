from meizen.dncl.lexer import compile_code


def test_compile():
    path = "C:/Users/readb/pycharm/meizen/meizen/dncl/sample/"
    filename = "sample"
    compile_code(path=path, filename=filename)


test_compile()
