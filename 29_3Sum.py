class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Ordenamos el array para facilitar el uso de los punteros
        res = []  # Lista para almacenar los tripletes únicos
        
        for i in range(len(nums) - 2):
            # Evitar duplicados en el primer número
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Inicializar los punteros
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])  # Agregar el triplete válido
                    
                    # Evitar duplicados en el segundo número
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Evitar duplicados en el tercer número
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Si la suma es menor a 0, mover el puntero izquierdo
                else:
                    right -= 1  # Si la suma es mayor a 0, mover el puntero derecho
        
        return res
