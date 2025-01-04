class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res

sol = Solution()
n1 = 11
n2 = 128
n3 = 2147483645
print(sol.hammingWeight(n1)) # 3
print(sol.hammingWeight(n2)) # 1
print(sol.hammingWeight(n3)) # 30