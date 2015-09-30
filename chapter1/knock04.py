#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

text = (
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. "
    "New Nations Might Also Sign Peace Security Clause. "
    "Arthur King Can."
)
answer = {
    'H':  1,
    'He': 2,
    'Li': 3,
    'Be': 4,
    'B':  5,
    'C':  6,
    'N':  7,
    'O':  8,
    'F':  9,
    'Ne': 10,
    'Na': 11,
    'Mi': 12,   # 'Mg' から始まる英単語はない
    'Al': 13,
    'Si': 14,
    'P':  15,
    'S':  16,
    'Cl': 17,
    'Ar': 18,
    'K':  19,
    'Ca': 20,
}

result  = {}
words   = text.split()
trigger = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for (i, word) in enumerate(words, start=1):
    if i in trigger:
        result[word[:1:]] = i
    else:
        result[word[:2:]] = i

assert result == answer
print(result)
# => 順序はランダムに表示されるため不定
# 例:
# {'Be': 4, 'C': 6, 'B': 5, 'Ca': 20, 'F': 9, 'S': 16, 'H': 1, 'K': 19, 'Al':
# 13, 'Mi': 12, 'Ne': 10, 'O': 8, 'Li': 3, 'P': 15, 'Si': 14, 'Ar': 18, 'Na':
# 11, 'N': 7, 'Cl': 17, 'He': 2}
