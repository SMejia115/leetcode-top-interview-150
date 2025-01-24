class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Si solo hay una fila o la longitud de la cadena es menor que numRows, devolvemos s
        if numRows == 1 or numRows >= len(s):
            return s

        # Crear una lista para almacenar las filas
        rows = [""] * numRows
        current_row = 0
        going_down = False

        # Construir las filas en el patrón zigzag
        for char in s:
            rows[current_row] += char
            # Cambiar de dirección al alcanzar la primera o última fila
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Avanzar en la dirección actual
            current_row += 1 if going_down else -1

        # Combinar todas las filas en el resultado final
        return "".join(rows)
