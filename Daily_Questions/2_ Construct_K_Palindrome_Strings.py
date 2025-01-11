from collections import Counter

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Si k es mayor que la longitud de s, no es posible construir k palíndromos
        if k > len(s):
            return False

        # Contar la frecuencia de cada carácter
        char_count = Counter(s)

        # Contar cuántos caracteres tienen frecuencia impar
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)

        # Debemos tener al menos `odd_count` palíndromos
        return odd_count <= k
