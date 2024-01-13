from .io import load
from symbol import Symbol


def compile_code(path: str, filename: str):
    code_list: list = load(path=path + filename + ".dncl")
    code_word = []
    code_symbol = []
    for code in code_list:
        line = list(code)  # 一行の文字ごとのリスト
        num = len(line)  # 行の文字数
        pos = 0  # 見ているlineの場所
        word = ""  # 切り出す単語の入れ先
        current_char = ''
        next_char = ''
        symbol = Symbol.NULL  # 切り出した単語の種類

        while num != pos:
            current_char = line[pos]
            next_char = line[pos + 1]
            word += current_char

            # if symbol == Symbol.NULL:
            if current_char == " ":
                symbol = Symbol.SPACE
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "\t":
                symbol = Symbol.INDENT
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ",":
                symbol = Symbol.COMMA
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ".":
                symbol = Symbol.DOT
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "(":
                symbol = Symbol.L_PAREN
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ")":
                symbol = Symbol.R_PAREN
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "[":
                symbol = Symbol.L_BRACKET
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "]":
                symbol = Symbol.R_BRACKET
                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "+":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "+=":
                        symbol = Symbol.ASSIGN_ADD
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                elif next_char == "+":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "++":
                        symbol = Symbol.INCREMENT
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.ADD
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "-":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "-=":
                        symbol = Symbol.ASSIGN_SUB
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                elif next_char == "-":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "--":
                        symbol = Symbol.DECREMENT
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.SUB
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "*":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "*=":
                        symbol = Symbol.ASSIGN_MUL
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.MUL
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == "/":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "/=":
                        symbol = Symbol.ASSIGN_DIV
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                elif next_char == "/":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if next_char == "=":
                        if pos+1 == num:
                            if word == "//":
                                symbol = Symbol.DIV_INT
                                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                                      symbol=symbol)
                            else:
                                symbol = Symbol.ERROR
                        else:
                            pos, current_char, next_char = next_to(line=line, pos=pos)
                            word += current_char
                            if word == "//=":
                                symbol = Symbol.ASSIGN_DIV_INT
                                word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                                      symbol=symbol)
                    else:
                        if word == "//":
                            symbol = Symbol.DIV_INT
                            word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                                  symbol=symbol)
                        else:
                            symbol = Symbol.ERROR
                else:
                    symbol = Symbol.DIV
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == "%":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "%=":
                        symbol = Symbol.ASSIGN_MOD
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.MOD
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == "=":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "==":
                        symbol = Symbol.EQUAL
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.ASSIGN
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == "<":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "<=":
                        symbol = Symbol.LESS_EQUAL
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.LESS
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == ">":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == ">=":
                        symbol = Symbol.GREAT_EQUAL
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.GREAT
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == "!":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "!=":
                        symbol = Symbol.NOT_EQUAL
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.NOT
                    word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                          symbol=symbol)
            elif current_char == "&":
                if next_char == "&":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "&&":
                        symbol = Symbol.AND
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
            elif current_char == "|":
                if next_char == "|":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "||":
                        symbol = Symbol.OR
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
            elif current_char == "\"":
                while next_char != "\"" or pos+1 != num:
                    pos += 1
                    current_char = line[pos]
                    next_char = line[pos + 1]
                    word += current_char
                if next_char == "\"":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "":
                        symbol = Symbol.OR
                        word, symbol = append(code_word=code_word, code_symbol=code_symbol, word=word,
                                              symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.ERROR

            # 残りは数値系、文字列、変数名で分けて、変数名のうち、予約語に該当するものは予約語へ

            # 全角、半角の変換処理の導入、変数宣言の寛容さを要検討

            # elif symbol == Symbol.ON_ANALYSE:
            pos, current_char, next_char = next_to(line=line, pos=pos)

            # 行末の処理
            word = ""
            code_word.append("\n")
            code_symbol.append(Symbol.RETURN)
    code_data = ""


# 追加する
def append(code_word: list, code_symbol: list, word: str, symbol: Symbol) -> (str, Symbol):
    code_word.append(word)
    code_symbol.append(symbol)
    return "", Symbol.NULL


# 次に文字があるかどうか
def check_next(pos: int, num: int) -> bool:
    if pos + 1 == num:
        return False
    else:
        return True


# 次の文字に進む
def next_to(line: list, pos: int) -> (int, str, str):
    pos += 1
    current_char = line[pos]
    next_char = line[pos + 1]
    return pos, current_char, next_char


def format_code(symbol: Symbol, sentence: str) -> str:
    code = sentence
    return code
