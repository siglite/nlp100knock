#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 00. 文字列の逆順
# 文字列 "stressed" の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ.

text   = "stressed"
answer = "desserts"

# Case 1
##########
case1 = text[::-1]  # str[start:end:step] : start から end まで step 毎の文字列を取得
                    # text[1:7:2] => "tes"  (1 から 7 まで 2 文字毎)
                    # text[:-1:2] => "srse" (最初から後ろの 2 文字目まで 2 文字毎)
                    # text[::-1]  => 最初から最後まで -1 文字ずつ

assert case1 == answer
print("Case 1: '" + case1 + "'")
# => Case 1: 'desserts'


# Case 2
##########
lst = list(text)        # => ['s', 't', 'r', 'e', 's', 's', 'e', 'd']
lst.reverse()           # => ['d', 'e', 's', 's', 'e', 'r', 't', 's']
case2 = ''.join(lst)    # => "desserts" ( '' で文字列を連結)

assert case2 == answer
print("Case 2: '" + case2 + "'")
# => Case 2: 'desserts'


# Case 3
##########
lst = list(text)        # => ['s', 't', 'r', 'e', 's', 's', 'e', 'd']
rvs = reversed(lst)     # => ['d', 'e', 's', 's', 'e', 'r', 't', 's']
case3 = ''.join(rvs)    # => "desserts"

assert case3 == answer
print("Case 3: '" + case3 + "'")
# => Case 3: 'desserts'
