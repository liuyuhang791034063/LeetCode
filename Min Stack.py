"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.min_num = []  # 主要记录所有最小值的队列 如果最小值pop出去后 就需要在min_num pop出

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.min_num) == 0 or x <= self.min_num[-1]:
            self.min_num.append(x)
        self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.min_stack) == 0:
            return
        num = self.min_stack.pop()
        if num == self.min_num[-1]:
            self.min_num.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0:
            return []
        return self.min_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_num[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
obj.getMin()
obj.pop()
obj.getMin()