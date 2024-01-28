from typing import List

class SelectionSort:

    def sort(self, arr):
        N: int = len(arr)

        if N == 0 or N == 1:
            return

        self.sortHelper(arr, N, N - 1)
    
    def sortHelper(self, arr: List[int], row:int, endIndex:int):
        # Base Condition 
        if row == 0 and endIndex < 1:
            return
        
        # Find the max value index
        index = self.maxIndex(arr, endIndex)

        # Swap the max element with the end index
        temp: int = arr[endIndex]
        arr[endIndex] = arr[index]
        arr[index] = temp
        
        self.sortHelper(arr, row - 1, endIndex - 1)

    def maxIndex(self, arr, endIndex) -> int:
        max: int = 0
        for i in range(endIndex + 1):
            if arr[max] < arr[i]:
                max = i
        
        return max
            



if __name__ == "__main__":
    arr: List[int] = [1, 8, 2, 9, 5, 21]

    sorting = SelectionSort()
    sorting.sort(arr)

    print(arr)

    