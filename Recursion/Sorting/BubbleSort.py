from typing import List

class BubbleSort:

    def sort(self, arr):
        self.sortHelper(arr, len(arr), 0)
    
    def sortHelper(self, arr: List[int], row:int, col:int):
        # Base Condition 
        if row == 0:
            return
        
        
        if col < len(arr) - 1:
            # Check whether current element is greater than the next one
            # if it is then swap
            if arr[col] > arr[col + 1]:
                temp: int = arr[col]
                arr[col] = arr[col + 1]
                arr[col + 1] = temp

            self.sortHelper(arr, row, col + 1)
        
        else:
            self.sortHelper(arr, row - 1, 0)




if __name__ == "__main__":
    arr: List[int] = [4, 3, 2, 5, 1, 3, 5, 9]

    sorting = BubbleSort()
    sorting.sort(arr)

    print(arr)

    