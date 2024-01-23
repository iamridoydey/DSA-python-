from typing import List

class RotatedBS:
    def search (self, arr: List[int], target:int) -> int:
        
        # Set the start and end pointer
        start: int = 0
        end: int = len(arr) - 1

        while start <= end:
            # Calculate mid pointer
            mid = start + (end - start) // 2

            if (target == arr[mid]):
                return mid
            
            # if the target is less than arr[mid] then search in the right part
            if (target < arr[mid]):
                start = mid + 1
            
            # if teh target is greater than arr[mid] then search in the left part
            
            if (target > arr[mid]):
                end = mid - 1

        return -1