from typing import List

class CyclicSort:
    """
        arr parameter imply to pass an array, here rangeStart impy that first number of the range
        (0-n). In this case it is 0. But it can be anything 0, 1, 2, 3, 4,...,n
    """
    def sort(self, arr: List[int], rangeStart:int):
        s = rangeStart
        i = 0
        # rangeStart imply that first number of the range (0-N) in this case it is 0
        while i < len(arr):
            # Check whether the number are in correct index or not 
            # if not then swap with correct index
            if arr[i] - s != i:
                # swap
                temp: int = arr[i]
                arr[i] = arr[arr[i] - s]
                arr[temp - s] = temp
            
            elif arr[i] - s == i:
                i += 1



if __name__ == "__main__":
    sorting = CyclicSort()

    arr: List[int] = [3, 4, 0, 2, 5, 1]

    # it is (1, N) range array
    sorting.sort(arr, 0)

    print(arr)
