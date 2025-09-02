import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # use choose formula for pascal triangle's items
        triangle = []
        i = 0
        while i < numRows:
            row = []
            j = 0
            while j <= i:
                row.append( int(math.factorial(i)
                    / ((math.factorial(j)) * math.factorial(i - j))) )
                j += 1
            triangle.append(row)
            i += 1
        return triangle
