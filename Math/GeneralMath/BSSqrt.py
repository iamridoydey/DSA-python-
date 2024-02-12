import math
class BSSqrt:
    def sqrt(self, num:int) -> int:
        start: int = 0
        end: int = num

        while start <= end:
            mid: int = start + (end - start) // 2

            square: int = mid * mid

            if square == num:
                return mid
            elif square < num:
                start = mid + 1
            else:
                end = mid - 1
        
        return end
    
    def sqrtPrecision(self, num: int, precision: float) -> float:
        # Get the integer value first
        root = self.sqrt(num)
        
        double: float = 0.1
        for _ in range(precision):
            guess: float = root + double
            i: int = 2
            while guess * guess <= num:
                claculateRoot = root + double * i
                i += 1
                if claculateRoot * claculateRoot > num:
                    root = guess
                    break
                guess = claculateRoot
                
            double /= 10
        
        return root



if __name__ == "__main__":
    bssqrt = BSSqrt()
    root = bssqrt.sqrtPrecision(55, 5)
    print(root)
    print(math.sqrt(55))