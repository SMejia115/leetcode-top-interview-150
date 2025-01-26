class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0

        for word in words:
            # Verificar si agregar la palabra actual excedería maxWidth
            if line_length + len(line) + len(word) > maxWidth:
                # Justificar la línea actual
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += " "
                result.append("".join(line))
                line = []
                line_length = 0

            # Agregar la palabra a la línea
            line.append(word)
            line_length += len(word)

        # Última línea (justificación izquierda)
        result.append(" ".join(line).ljust(maxWidth))

        return result
        