class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        w_list = s.split()

        reverse_list = w_list[::-1]

        return " ".join(reverse_list)