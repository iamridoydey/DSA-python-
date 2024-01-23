from BinarySearch import BinarySearch
from typing import List


binarySearch = BinarySearch()

arr: List[int] = [2, 3, 5, 6, 8, 9, 11, 12]
ans:[int] = binarySearch.search(arr, target=7)

if __name__ == "__main__":
    print(ans)