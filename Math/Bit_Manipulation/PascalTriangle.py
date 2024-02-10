"""
    Pascal Triangle:
                    1
                1       1
            1       2       1
        1       3       3       1
"""

class PascalTriangle:
    def sumOfRow(self, Nth_row: int) -> int:
        return 1 << Nth_row - 1


if __name__ == "__main__":
    # Nth row sum of the pascal triangle
    triangle = PascalTriangle()
    N:int = 9
    ans = triangle.sumOfRow(9)
    print(ans)

    