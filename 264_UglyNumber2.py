class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type num: int
        :rtype: bool
        """
        # Runtime: 116 ms, faster than 88.06% of Python online submissions for Ugly Number II.
        # Memory Usage: 11.7 MB, less than 91.56% of Python online submissions for Ugly Number II.

        if n<1: return None
        uglyN=[1]*n
        # save the pos of the smallest factor never used , the next min should be generated by these
        i2,i3,i5=0,0,0
        for i in range(1,n):
            uglyN[i]= min(uglyN[i2]*2,uglyN[i3]*3,uglyN[i5]*5)
            if uglyN[i]== uglyN[i2]*2:i2+=1
            if uglyN[i] == uglyN[i3]*3: i3 += 1
            if uglyN[i] == uglyN[i5]*5: i5 += 1
        return uglyN[n-1]

if __name__ == '__main__':
    s= 1690

    p = Solution()
    print(p.nthUglyNumber(s))