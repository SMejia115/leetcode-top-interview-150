class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
    
        max_h = len(citations)

        for i in range (max_h, 0, -1):
            aux_citations = [x for x in citations if x >= i]
            if len(aux_citations) >= i:
                return i

        return 0