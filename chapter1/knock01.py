#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ.

text   = u"パタトタカシーー"  # u"文字列" で unicode 文字列になる
answer = u"タタシー"

result = text[1::2]

assert result == answer
print("Result: '" + result + "'")
# => "Result: 'タタシー'"
