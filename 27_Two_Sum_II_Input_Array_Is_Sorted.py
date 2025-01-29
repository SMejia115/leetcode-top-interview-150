class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1  # Dos punteros: inicio y final

        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # +1 porque la lista es 1-indexada
            elif current_sum < target:
                left += 1  # Mover el puntero izquierdo si la suma es muy pequeña
            else:
                right -= 1  # Mover el puntero derecho si la suma es muy grande
        
        return []  # Nunca se ejecutará, ya que se garantiza que hay una solución
