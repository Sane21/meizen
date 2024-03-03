from .io import load, write
from .symbol import Symbol


# トランスコンパイル
def compile_code(path: str, filename: str):
    """
    pathフォルダ内に存在するfilename.dnclを読み取り、同フォルダ内にfilename.pyを作成する
    :param path: 読み取りファイルと書き込みファイルの存在するディレクトリ(フォルダ)のパス
    :param filename: 読み取るファイル名 (拡張子は除く)
    :return:
    """
    read_file_path = path + filename + ".dncl"
    write_file_path = path + filename + ".py"
    code_word, code_symbol = lexical_analyse(path=read_file_path)
    print("字句解析完了")
    code_list = parse(code_word=code_word, code_symbol=code_symbol)
    print("構文解析完了")
    write(path=write_file_path, code_list=code_list)
    print("書き込み完了")


# 字句解析
def lexical_analyse(path: str) -> (list, list):
    """
    字句解析関数
    pathのファイルを読み取り、字句解析して単語ごとに切り分け、単語とSymbolのlistで返す
    :param path: 解析する.dnclファイルのパス
    :return: 字句解析した結果の単語のリスト, Symbolのリスト
    """
    code_list: list = load(path=path)
    # ここから 最後の１行を構文解析できないことのケアとして空行を追加する処理
    code_list[len(code_list) - 1] += "\n"
    code_list.append("")
    # ここまで 消しちゃだめ
    code_word: list = []
    code_symbol: list = []
    len_line = len(code_list)  # 行数
    count_line = 0  # 行数のカウント
    for code in code_list:
        count_line += 1
        line = list(code)  # 一行の文字ごとのリスト
        num = len(line)  # 行の文字数
        pos = -1  # 見ているlineの場所

        while pos + 1 != num:
            pos += 1

            # 読み取り情報の初期化
            symbol = Symbol.NULL  # 切り出した単語の種類
            current_char = line[pos]  # 現在の頭文字
            word = current_char  # 現在の単語
            next_char = ""
            if current_char == "\n":
                symbol = Symbol.RETURN
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
                break
            if not len_line == count_line or pos == num:
                next_char = line[pos + 1]  # 次の文字

            if current_char == "\n":
                symbol = Symbol.RETURN
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
                break
            elif current_char == " ":
                # スペース4つでインデント判定
                if next_char == " ":
                    current_pos = pos
                    current_word = word
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if next_char == " " and pos + 1 != num:
                        pos, current_char, next_char = next_to(line=line, pos=pos)
                        word += current_char
                        if next_char == " " and pos + 1 != num:
                            pos, current_char, next_char = next_to(line=line, pos=pos)
                            word += current_char
                            if word == "    ":
                                word = "\t"
                                symbol = Symbol.INDENT
                                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
                            else:
                                pos = current_pos
                                word = current_word
                                symbol = Symbol.SPACE
                                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
                        else:
                            pos = current_pos
                            word = current_word
                            symbol = Symbol.SPACE
                            append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
                    else:
                        pos = current_pos
                        word = current_word
                        symbol = Symbol.SPACE
                        append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
                else:
                    symbol = Symbol.SPACE
                    append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "\t":
                symbol = Symbol.INDENT
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ",":
                symbol = Symbol.COMMA
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ".":
                symbol = Symbol.DOT
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "(":
                symbol = Symbol.L_PAREN
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ")":
                symbol = Symbol.R_PAREN
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "[":
                symbol = Symbol.L_BRACKET
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "]":
                symbol = Symbol.R_BRACKET
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ":":
                symbol = Symbol.CORON
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == ";":
                symbol = Symbol.SEMI_CORON
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            # TODO 「」の処理について、このままだと内部がL_KAKKO_JP WORD R_KAKKO_JP になってるのでほんとはQUOTと同様の処理をしたいけど\
            #  一時的な急場を凌ぐ処理として変換だけはできるようにしておく。
            elif current_char == "「":
                symbol = Symbol.L_KAKKO_JP
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "」":
                symbol = Symbol.R_KAKKO_JP
                append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "+":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "+=":
                        symbol = Symbol.ASSIGN_ADD
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                elif next_char == "+":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "++":
                        symbol = Symbol.INCREMENT
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.ADD
                    append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "-":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "-=":
                        symbol = Symbol.ASSIGN_SUB
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                elif next_char == "-":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "--":
                        symbol = Symbol.DECREMENT
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.SUB
                    append(code_word=code_word, code_symbol=code_symbol, word=word, symbol=symbol)
            elif current_char == "*":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "*=":
                        symbol = Symbol.ASSIGN_MUL
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.MUL
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "÷":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "÷=":
                        symbol = Symbol.ASSIGN_DIV_JP
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.DIV_JP
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "/":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "/=":
                        symbol = Symbol.ASSIGN_DIV
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                elif next_char == "/":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if next_char == "=":
                        if pos + 1 == num:
                            if word == "//":
                                symbol = Symbol.DIV_INT
                                append(code_word=code_word, code_symbol=code_symbol, word=word,
                                       symbol=symbol)
                            else:
                                symbol = Symbol.ERROR
                        else:
                            pos, current_char, next_char = next_to(line=line, pos=pos)
                            word += current_char
                            if word == "//=":
                                symbol = Symbol.ASSIGN_DIV_INT
                                append(code_word=code_word, code_symbol=code_symbol, word=word,
                                       symbol=symbol)
                    else:
                        if word == "//":
                            symbol = Symbol.DIV_INT
                            append(code_word=code_word, code_symbol=code_symbol, word=word,
                                   symbol=symbol)
                        else:
                            symbol = Symbol.ERROR
                else:
                    symbol = Symbol.DIV
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "%":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "%=":
                        symbol = Symbol.ASSIGN_MOD
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.MOD
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "=":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "==":
                        symbol = Symbol.EQUAL
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.ASSIGN
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "<":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "<=":
                        symbol = Symbol.LESS_EQUAL
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.LESS
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == ">":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == ">=":
                        symbol = Symbol.GREAT_EQUAL
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.GREAT
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "←":
                symbol = Symbol.ASSIGN_ARROW
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif current_char == "!":
                if next_char == "=":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "!=":
                        symbol = Symbol.NOT_EQUAL
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.NOT
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
            elif current_char == "&":
                if next_char == "&":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "&&":
                        symbol = Symbol.AND
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
            elif current_char == "|":
                if next_char == "|":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word == "||":
                        symbol = Symbol.OR
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
            elif current_char == "\"":
                while next_char != "\"" and pos + 1 != num:
                    pos += 1
                    current_char = line[pos]
                    next_char = line[pos + 1]
                    word += current_char
                if next_char == "\"":
                    pos, current_char, next_char = next_to(line=line, pos=pos)
                    word += current_char
                    if word[0] == "\"" and word[len(word) - 1] == "\"":
                        symbol = Symbol.STRING
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR
                else:
                    symbol = Symbol.ERROR
            elif is_number_character(current_char):
                while is_number_character(next_char) and pos + 1 != num:
                    pos += 1
                    current_char = line[pos]
                    next_char = line[pos + 1]
                    word += current_char
                if next_char == ".":
                    pos += 1
                    current_char = line[pos]
                    next_char = line[pos + 1]
                    word += current_char
                    if is_number_character(next_char):
                        while is_number_character(next_char) and pos + 1 != num:
                            pos += 1
                            current_char = line[pos]
                            next_char = line[pos + 1]
                            word += current_char
                        if is_number(word=word):
                            symbol = Symbol.FLOAT
                            append(code_word=code_word, code_symbol=code_symbol, word=word,
                                   symbol=symbol)
                        else:
                            symbol = Symbol.ERROR
                    else:
                        symbol = Symbol.ERROR
                else:
                    if is_number(word=word):
                        symbol = Symbol.INTEGER
                        append(code_word=code_word, code_symbol=code_symbol, word=word,
                               symbol=symbol)
                    else:
                        symbol = Symbol.ERROR

            if symbol != Symbol.NULL:
                continue

            # ここから下は単語か予約語になる
            while not is_symbol_head_character(next_char) and pos + 1 != num:
                pos, current_char, next_char = next_to(line=list(line), pos=pos)
                word += current_char

            if word == str(Symbol.IF):
                symbol = Symbol.IF
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.THEN):
                symbol = Symbol.THEN
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.ELIF):
                symbol = Symbol.ELIF
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.ELSE):
                symbol = Symbol.ELSE
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.WHILE):
                symbol = Symbol.WHILE
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.BREAK):
                symbol = Symbol.BREAK
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.CONTINUE):
                symbol = Symbol.CONTINUE
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FOR_L):
                symbol = Symbol.FOR_L
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FOR_M):
                symbol = Symbol.FOR_M
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FOR_N):
                symbol = Symbol.FOR_N
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FOR_DEC):
                symbol = Symbol.FOR_DEC
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FOR_INC):
                symbol = Symbol.FOR_INC
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FUNCTION):
                symbol = Symbol.FUNCTION
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.PRINT):
                symbol = Symbol.PRINT
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.TRUE):
                symbol = Symbol.TRUE
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FALSE):
                symbol = Symbol.FALSE
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.TRUE_JP):
                symbol = Symbol.TRUE_JP
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FALSE_JP):
                symbol = Symbol.FALSE_JP
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.INPUT):
                symbol = Symbol.INPUT
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FUNC_LENGTH):
                symbol = Symbol.FUNC_LENGTH
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FUNC_STR):
                symbol = Symbol.FUNC_STR
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FUNC_INT):
                symbol = Symbol.FUNC_INT
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            elif word == str(Symbol.FUNC_FLOAT):
                symbol = Symbol.FUNC_FLOAT
                append(code_word=code_word, code_symbol=code_symbol, word=word,
                       symbol=symbol)
            else:
                if is_name(word=word):
                    symbol = Symbol.NAME
                    append(code_word=code_word, code_symbol=code_symbol, word=word,
                           symbol=symbol)
                else:
                    symbol = Symbol.ERROR

            if symbol == Symbol.ERROR:
                print("ERROR : word[" + word + "], pos[" + str(
                    pos) + "], cc[" + current_char + "], nc[" + next_char + "]")
    return code_word, code_symbol


# 構文解析
def parse(code_word: list, code_symbol: list) -> list:
    """
    構文解析関数
    引数に字句解析の結果を受け取り、解析してPythonに再生成したプログラムを行ごとに格納したlistを返す
    :param code_word: 字句解析結果の単語のlist
    :param code_symbol: 字句解析結果のSymbolのlist
    :return: 生成したPythonのコードを1行ごとに格納したlist
    """
    code_list: list[str] = []  # 各行を格納するリスト
    word_num = len(code_word)  # 単語の格納数
    symbol_num = len(code_symbol)  # 記号の格納数
    code_line: str = ""  # 見ている行
    tab_num: int = 0  # インデントの回数
    if word_num != symbol_num:
        return []

    pos = -1  # 一覧の現在見ている場所
    while not pos + 1 == word_num:
        pos += 1
        if code_symbol[pos] == Symbol.RETURN:
            indent = ""
            while tab_num > 0:
                indent += "\t"
                tab_num -= 1
            tab_num = 0
            code_list.append(indent + code_line)
            code_line = ""
        elif code_symbol[pos] == Symbol.INDENT:
            tab_num += 1
        elif code_symbol[pos] == Symbol.TRUE_JP:
            code_line += str(Symbol.TRUE)
        elif code_symbol[pos] == Symbol.FALSE_JP:
            code_line += str(Symbol.FALSE)
        elif code_symbol[pos] == Symbol.L_KAKKO_JP:
            code_line += str(Symbol.QUOTATION)
        elif code_symbol[pos] == Symbol.R_KAKKO_JP:
            code_line += str(Symbol.QUOTATION)
        elif code_symbol[pos] == Symbol.ASSIGN_ARROW:
            code_line += str(Symbol.ASSIGN)
        elif code_symbol[pos] == Symbol.DIV_JP:
            code_line += "//"
        elif code_symbol[pos] == Symbol.ASSIGN_DIV_JP:
            code_line += "//="
        elif code_symbol[pos] == Symbol.FUNCTION:
            code_line += "def"
        elif code_symbol[pos] == Symbol.PRINT:
            code_line += "print"
        elif code_symbol[pos] == Symbol.INPUT:
            code_line += "input(\"文字を入力してください\")"
        elif code_symbol[pos] == Symbol.FUNC_LENGTH:
            code_line += "len"
        elif code_symbol[pos] == Symbol.FUNC_INT:
            code_line += "int"
        elif code_symbol[pos] == Symbol.FUNC_STR:
            code_line += "str"
        elif code_symbol[pos] == Symbol.FUNC_FLOAT:
            code_line += "float"
        elif code_symbol[pos] == Symbol.IF:
            code_line += "if"
            while pos + 1 != word_num and code_symbol[pos + 1] != Symbol.THEN:
                pos += 1
                code_line += code_word[pos]
            pos += 1
        elif code_symbol[pos] == Symbol.ELIF:
            code_line += "elif"
            while pos + 1 != word_num and code_symbol[pos + 1] != Symbol.THEN:
                pos += 1
                code_line += code_word[pos]
            pos += 1
        elif code_symbol[pos] == Symbol.ELSE:
            code_line += "else"
        elif code_symbol[pos] == Symbol.WHILE:
            line = code_line
            code_line = ""
            is_while: bool = False
            for character in line:
                if character == "\t":
                    code_line += character
                else:
                    if not is_while:
                        code_line += "while "
                        code_line += character
                        is_while = True
                    else:
                        code_line += character
        elif code_symbol[pos] == Symbol.PRINT:
            code_line += "print"
        elif code_symbol[pos] == Symbol.FOR_L:
            line = code_line
            line_after_tab = ""  # i
            code_line = ""
            for character in line:
                if character == "\t":
                    code_line += character
                else:
                    line_after_tab += character

            code_line_l = "for "
            code_line_l += line_after_tab
            code_line_l += " in range("

            num_l = ""
            while pos + 1 != word_num and code_symbol[pos + 1] != Symbol.FOR_M:
                pos += 1
                num_l += code_word[pos]
            code_line_m = num_l
            code_line_n = ", "
            pos += 1

            num_m = ""
            while pos + 1 != word_num and code_symbol[pos + 1] != Symbol.FOR_N:
                pos += 1
                num_m += code_word[pos]
            code_line_n += num_m
            code_line_o = ", "
            pos += 1

            num_n = ""
            while pos + 1 != word_num and \
                    (code_symbol[pos + 1] != Symbol.FOR_INC and code_symbol[pos + 1] != Symbol.FOR_DEC):
                pos += 1
                num_n += code_word[pos]
            if code_symbol[pos + 1] == Symbol.FOR_INC:
                code_line_n += "+1"
                code_line_o += num_n
            elif code_symbol[pos + 1] == Symbol.FOR_DEC:
                code_line_n += "-1"
                code_line_o += "-" + num_n
            code_line = code_line_l + code_line_m + code_line_n + code_line_o
            code_line += ")"
            pos += 1
        else:
            code_line += code_word[pos]
    return code_list


# 追加する
def append(code_word: list, code_symbol: list, word: str, symbol: Symbol):
    """
    wordのlistとsymbolのlistの両方に対応する情報を追加する処理
    字句解析中に使用
    :param code_word: wordのlist
    :param code_symbol: symbolのlist
    :param word: 追加するword
    :param symbol: 追加するlist
    :return:
    """
    code_word.append(word)
    code_symbol.append(symbol)


def is_symbol_head_character(character: str) -> bool:
    """
    引数の文字が記号の頭文字かどうかを判別する関数
    新しい記号や予約語を追加する場合は、対応する字句解析や構文解析に加えてここも編集すること
    :param character: 判別したい文字
    :return: 頭文字か否か
    """
    result = False
    key_list = ["\n", " ", "\t", ",", ".", "(", ")", "[", "]", "+", "-", "*", "/", "%", "=", "<", ">", "!", "&", "|",
                "\"", "\0", ";", ":", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "「", "」", "←"]
    for key in key_list:
        if character == key:
            result = True
            break
    return result


# 文字が数値かどうかを判別
def is_number_character(character: str) -> bool:
    """
    引数の文字がアラビア数字がどうかを判別する関数
    :param character: 判定したい文字
    :return: アラビア数字か否か
    """
    result = False
    if character == "0" or character == "1" or character == "2" or character == "3" \
            or character == "4" or character == "5" or character == "6" or character == "7" \
            or character == "8" or character == "9":
        result = True
    else:
        result = False
    return result


# 文字列が数値かどうかを判別
def is_number(word: str) -> bool:
    """
    引数の文字列が数値かどうかを判別する関数
    浮動小数点数少数として扱えるかどうかを判別の基準としている
    :param word: 判別したい文字列
    :return: 数値か否か
    """
    try:
        float(word)
    except ValueError:
        return False
    else:
        return True


def is_name(word: str) -> bool:
    """
    未実装
    引数の文字列が変数名として許容可能かどうかを判別する関数
    :param word: 判別したい文字列
    :return: 変数名か否か
    """
    result = True
    # result = False
    # for character in word:
    #     if str.isalpha(character) or character == "_":
    #         result = True
    #     else:
    #         result = False
    #         break
    return result


# 次の文字に進む
def next_to(line: list, pos: int) -> (int, str, str):
    """
    文字送り関数
    字句解析中で使用
    :param line: 判定中の行
    :param pos: 判定中の位置
    :return: int判定箇所, str現在の文字, str次の文字
    """
    pos += 1
    current_char = line[pos]
    next_char = line[pos + 1]
    return pos, current_char, next_char
