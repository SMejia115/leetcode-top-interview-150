class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Ordenar por el extremo derecho
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for start, end in points[1:]:
            if start > current_end:
                # Necesitamos una nueva flecha
                arrows += 1
                current_end = end
        
        return arrows
        