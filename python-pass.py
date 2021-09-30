class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        m = ''
        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(len(s) + 1):
                if len(m) >= j - i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    continue

        return m
print(Solution.longest_palindromic("babad"))