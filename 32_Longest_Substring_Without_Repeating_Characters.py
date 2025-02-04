class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # Usamos un set para almacenar los caracteres únicos
        left = 0  # Puntero izquierdo de la ventana deslizante
        max_length = 0  # Variable para almacenar la longitud máxima
        
        for right in range(len(s)):
            # Si el caracter ya está en el set, movemos el puntero izquierdo
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Agregamos el caracter actual al set
            char_set.add(s[right])
            # Calculamos la longitud máxima encontrada
            max_length = max(max_length, right - left + 1)
        
        return max_length
