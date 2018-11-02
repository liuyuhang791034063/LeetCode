# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       a string representing a numeric value
   Description:
   Author:           God
   date：            2018/11/2
-------------------------------------------------
   Change Activity:  2018/11/2
-------------------------------------------------
"""
__author__ = 'God'

'''
尝试转化成float类型,失败返回False
'''
class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            ss = float(s)
            return True
        except:
            return False


'''
使用re判断
* 匹配前面出现的正则表达式零次或多次
+ 匹配前面出现的正则表达式1次或多次
? 匹配前面出现的正则表达式0次或1次
正则中三部分:
1. ^[\+\-]?[0-9]* 判断字符串头是否存在符号后面
2. (\.[0-9]*)? 判断是否存在小数点
3. ([eE][\+\-]?[0-9]+)? 这里[0-9]后面是+,因为出现e或者E后必须有数字.
'''
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)
