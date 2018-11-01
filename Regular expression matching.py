# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Regular expression matching
   Description:
   Author:           God
   date：            2018/11/1
-------------------------------------------------
   Change Activity:  2018/11/1
-------------------------------------------------
"""
__author__ = 'God'


"""
直接调用re模块
"""
import re
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        return True if re.match('^'+pattern+'$', s) else False


"""
1.如果两个字符串都是空,返回true
2.如果pattern是空字符串,返回False
3.正式开始匹配
 (1)如果patten下一个不是'*',直接匹配当前字符,如果失败直接返回False,特殊情况就是patten中为'.',s中不为'\0'.
 (2)如果patten下一个是'*':
    a>当前'*'匹配0个字符,s当前字符不变,patten往后两位,跳过'*'
    b>当前'*'匹配一个或多个时,s移动一位,patten不变.
"""
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        self.s = s
        self.patten = pattern
        return self.fun(0, 0)

    def fun(self, a, b):
        if self.s[a] == '\0' and self.patten[b] == '\0':
            return True
        if self.s[a] != '\0' and self.patten[b] == '\0':
            return False
        if self.patten[b+1] != '*':
            if self.s[a] == self.patten[b] or self.s[a] != '\0' and self.patten[b] == '.':
                return self.fun(a+1, b+1)
            else:
                return False
        else:
            if self.s[a] == self.patten[b] or self.s[a] != '\0' and self.patten[b] == '.':
                return self.fun(a, b+2) or self.fun(a+1, b)
            else:
                return self.fun(a, b+2)



if __name__ == '__main__':
    print(Solution().match("a", "a."))