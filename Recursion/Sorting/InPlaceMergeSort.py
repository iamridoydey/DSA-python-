from typing import List

class MergeSort:

    def sort(self, arr: List[int]) -> None:
        self.sortHelper(arr, 0, len(arr) - 1)


    def sortHelper(self, arr: List[int], start: int, end: int) -> None:
        # Base condition 
        if start == end:
            return
        
        
        # Get half length of the array
        mid: int = start + (end - start) // 2

        # Sort the left part of the array
        self.sortHelper(arr, start, mid)

        # Sort the right part of the array
        self.sortHelper(arr, mid + 1, end)

        # Merge this two array
        self.merge(arr, start, mid, mid + 1, end)


    def merge(self, arr: List[int], start1: int, end1: int, start2: int, end2: int) -> None:
        
        # Merged array
        merged: List[int] = []

        # Create two pointers for this two array
        i: int = start1
        j: int = start2

        while i <= end1 and j <= end2:
            if arr[i] < arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1

        
        # Put all the remaining elements in the merged array
        while i <= end1:
            merged.append(arr[i])
            i += 1

        while j <= end2:
            merged.append(arr[j])
            j += 1

        for i in range(len(merged)):
            arr[start1 + i] = merged[i]


    


if __name__ == "__main__":
    arr: List[int] = [5, 2, 4, 3, 0, 8, 9, 21, 1, 6, 13, 11]
    obj = MergeSort()
    obj.sort(arr)
    print(arr)