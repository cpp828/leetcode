"""
7 
题目描述：给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret=0
        r=abs(x)
        while r:
            ret=ret*10+r%10
            r/=10
        if -ret>=-(2**31) and x<0:
            return -(ret)
       
        elif x>=0 and ret<=2**31-1:
            return ret
        else:
            return 0
