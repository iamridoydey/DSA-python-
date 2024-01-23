from RotatedBS import RotatedBS
from typing import List

bs = RotatedBS()

arr: List[int] = [21, 17, 12, 7, 6, 5, 3, 1]
ans: int = bs.search(arr, target= 21)

if __name__ == "__main__":
    print(ans)