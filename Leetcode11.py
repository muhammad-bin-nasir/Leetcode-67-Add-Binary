class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        check = 0
        for i in range(len(s)):
            if s[i]!=" ":
                if check == 0:
                    count = count + 1
                else:
                    count = 1
                    check = 0
            else:
                check = 1
        return count
