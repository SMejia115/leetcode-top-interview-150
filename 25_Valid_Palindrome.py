class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convertir a minúsculas y filtrar solo caracteres alfanuméricos
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        
        # Comparar la cadena filtrada con su reversa
        return filtered == filtered[::-1]
        