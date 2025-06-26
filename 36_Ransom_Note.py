class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for i in magazine:
            if i in ransomNote:
                ransomNote = ransomNote.replace(i, '', 1)
                
        if len(ransomNote) == 0:
            return True
        return False
        
        
# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("a", "b"))  # False
    print(solution.canConstruct("aa", "ab"))  # False
    print(solution.canConstruct("aa", "aab"))  # True
    print(solution.canConstruct("", "abc"))  # True
    print(solution.canConstruct("abc", ""))  # False
    print(solution.canConstruct("abc", "cba"))  # True
    print(solution.canConstruct("abc", "def"))  # False