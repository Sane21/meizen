import re


def check_re(sentence: str, pattern: str) -> bool:
    """
    正規表現による確認関数
    sentenceがpatternに合致するかどうかを確認する
    :param sentence: 確認対象となる文字列
    :param pattern: 答えとなる正規表現
    :return: 合致したか否か
    """
    match = re.fullmatch(string=sentence, pattern=pattern)
    result = match is not None
    return result


def check_str(sentence: str, string: str) -> bool:
    """
    文字列による確認関数
    sentenceがstringに一致するかどうかを確認する
    :param sentence: 確認対象となる文字列
    :param string: 答えとなる正規表現
    :return: 一致したか否か
    """
    result = sentence == string
    return result
