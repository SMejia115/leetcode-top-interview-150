class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Puntero lento que indica la posición para los elementos únicos
        k = 0

        # Itera con el puntero rápido
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        # k es la última posición única, el número total de elementos únicos es k + 1
        return k + 1