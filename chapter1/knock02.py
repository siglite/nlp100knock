#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ.

text1  = u"パトカー"
text2  = u"タクシー"
answer = u"パタトクカシーー"

list1  = list(text1)
list2  = list(text2)

# Case 1
##########
result = u""
for i in range(len(list1)):
    result += list1[i] + list2[i]

assert result == answer
print("Case 1: '" + result + "'")
# => Case 1: 'パタトクカシーー'


# Case 2
##########
result = u""
for (char1, char2) in zip(list1, list2):
    result += char1 + char2

assert result == answer
print("Case 2: '" + result + "'")
# => Case 2: 'パタトクカシーー'
