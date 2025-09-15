class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]

            # avanzar mientras sea consecutivo
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            end = nums[i]

            # construir string del rango
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))

            i += 1

        return result