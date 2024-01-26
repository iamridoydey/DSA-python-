from typing import List

class OrderAgnosticBS:
    def search(self, arr: List[int], target: int) -> int:
        # Length of the array
        N: int = len(arr)

        if N == 0:
            return -1
        
        isAscen: bool = False
        # Check whether it is a assending order sorted array or just descending one
        if arr[0] < arr[N - 1]:
            # It's an ascending order array
            isAscen = True


        start: int = 0
        end: int = N - 1

        while start <= end:
            mid: int = start + (end - start) // 2

            if target == arr[mid]:
                return mid
            
            # if it is an ascending order array
            if isAscen:
                if target < arr[mid]:
                    end = mid - 1

                else:
                    start = mid + 1

            # If it is a descending order array
            else:
                if target > arr[mid]:
                    end = mid - 1

                else:
                    start = mid + 1

        return -1

