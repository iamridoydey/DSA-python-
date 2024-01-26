from typing import List

class SelectionSort:

    def sort(self, arr: List[int]):
        # Length of the array
        N = len(arr)

        for i in range(N):
            endIndex:int = N - i - 1
            # Get the max value's index
            maxIndex: int = 0

            for j in range(1, N - i):
                if arr[maxIndex] < arr[j]:
                    maxIndex = j
            
            # swap
            temp: int = arr[maxIndex]
            arr[maxIndex] = arr[endIndex]
            arr[endIndex] = temp


if __name__ == "__main__":
    sorted = SelectionSort()

    arr: List[int] = [21, 3, 23, 1, 12, 15, 19, 2, 0]
    sorted.sort(arr)

    print(arr)
            