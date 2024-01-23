from typing import List

class BinarySearch:
    # Binary Search algorithm
    def search(self, arr: List[int], target: int) -> int:
        # Create start and end pointers
        start: int = 0
        end: int = len(arr) - 1

        while start <= end:
            # Calculate the middle
            mid: int = start + (end - start) // 2

            if (target == arr[mid]):
                return mid
            
            # Check in the left part of the array
            if (target < arr[mid]):
                end = mid - 1
            # Check in the right part of the array
            elif (target > arr[mid]):
                start = mid + 1

        
        # If the element not found then just return -1
        return -1
    




    
