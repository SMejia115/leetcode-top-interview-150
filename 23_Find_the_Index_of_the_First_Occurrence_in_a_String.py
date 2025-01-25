class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Si el needle está vacío, por convención devolver 0
        if not needle:
            return 0
        
        # Uso del método find para buscar la primera ocurrencia
        index = haystack.find(needle)
        
        return index
