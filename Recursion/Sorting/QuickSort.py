from typing import List

class QuickSort:
    def sort(self, arr: List[int]) -> None:
        self.sortHelper(arr, 0, len(arr) - 1)
    
    def sortHelper(self, arr: List[int], start: int, end: int) -> None:
        # When start and end index are become same then just stop
        if start == end:
            return
        
        # Get the index of the pivot
        pivot: int = self.partition(arr, start, end)

        # Call the left part of the array to be sorted
        self.sortHelper(arr, start, pivot)
        # Call the right part of the array to be sorted
        self.sortHelper(arr, pivot + 1, end)
    

    def partition(self, arr: List[int], start: int, end : int) -> int:
        # Pick the pivot as mid element
        mid: int = start + (end - start) // 2

        # Pivot element
        p: int = arr[mid]

        while start != end:
            # Move forward until find a element which violets the condition
            while arr[start] < p:
                start += 1


            while arr[end] > p:
                end -= 1

            # When we find a violets position from the start and from the end,
            # then just swap the elment start with end
            if start < end:
                temp: int = arr[start]
                arr[start] = arr[end]
                arr[end] = temp

        # At the end of the loop start and end will pointing to the pivot index
        return start
    


if __name__ == "__main__":
    arr: List[int] = [4, 5, 8, 9, 1, 3]
    obj = QuickSort()

    obj.sort(arr)
    print(arr)