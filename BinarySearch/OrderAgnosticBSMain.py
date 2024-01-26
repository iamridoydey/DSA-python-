from typing import List
from OrderAgnosticBS import OrderAgnosticBS

if __name__ == "__main__":
    bs1 = OrderAgnosticBS()
    bs2 = OrderAgnosticBS()

    arr: List[int] = [2, 3, 5, 7, 8, 9, 12, 21]
    nums: List[int] = [29, 27, 24, 21, 18, 15, 12, 11, 9, 3, 1]

    ans1:int = bs1.search(arr, target=9) # Ans: 5
    print(f"Answer1: {ans1}")

    ans2:int = bs2.search(nums, target=21) # Ans: 3
    print(f"Answer2: {ans2}")
