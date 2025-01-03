class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Puntero al final de nums1
        last = m + n - 1
        
        # Punteros al final de las partes relevantes de nums1 y nums2
        i = m - 1
        j = n - 1
        
        # Fusionar nums1 y nums2 desde el final
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        
        # Copiar los elementos restantes de nums2, si los hay
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1


        
        