import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        # Frecuencia de caracteres en t
        target_count = collections.Counter(t)
        required_chars = len(target_count)

        # Variables de la ventana deslizante
        left, right = 0, 0
        formed_chars = 0  # Cantidad de caracteres de t satisfechos en la ventana
        window_counts = {}

        # [start, end] almacena la mejor ventana encontrada
        min_len = float("inf")
        start, end = 0, 0

        while right < len(s):
            # Agregar el nuevo carácter a la ventana
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Verificar si el carácter satisface la cantidad en t
            if char in target_count and window_counts[char] == target_count[char]:
                formed_chars += 1
            
            # Intentar reducir la ventana cuando ya se tienen todos los caracteres de t
            while left <= right and formed_chars == required_chars:
                char = s[left]

                # Actualizar el mínimo si se encuentra una mejor ventana
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start, end = left, right

                # Remover el carácter del extremo izquierdo
                window_counts[char] -= 1
                if char in target_count and window_counts[char] < target_count[char]:
                    formed_chars -= 1
                
                left += 1  # Mover el inicio de la ventana

            right += 1  # Expandir la ventana

        return "" if min_len == float("inf") else s[start:end + 1]