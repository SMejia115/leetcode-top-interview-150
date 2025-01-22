class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        # Ordenar las cadenas
        strs.sort()
        
        # Primera y última cadena
        first = strs[0]
        last = strs[-1]
        
        # Encontrar prefijo común
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]