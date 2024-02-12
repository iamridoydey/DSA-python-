from typing import List

class FactorsOfNumber:
    def factors(self, num:int) -> List[int]:
        arr: List[int] = []

        for i in range(1, num):
            if i * i <= num:
                if num % i == 0:
                    arr.append(i)
                    
                    multiplier: int = int(num / i)
                    if i != multiplier:
                        arr.append(multiplier)
            else:
                break

        arr.sort()

        return arr
    

if __name__ == "__main__":
    factors = FactorsOfNumber()
    ans: List[int] = factors.factors(36)
    print(ans)
