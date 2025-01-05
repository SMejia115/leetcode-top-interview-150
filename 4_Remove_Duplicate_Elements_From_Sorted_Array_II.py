class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Puntero lento para marcar la posición de inserción
        k = 0

        # Recorremos el array con un puntero rápido
        for num in nums:
            # Solo añadimos el número si es el primer o segundo duplicado
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k

