from typing import List

class MergeSort:

    def sort(self, arr: List[int]) -> List[int]:
        # Base condition 
        if len(arr) == 1:
            return arr
        
        # Get half length of the array
        start: int = 0
        end: int = len(arr)
        mid: int = start + (end - start) // 2

        # Sort the left part of the array
        left: List[int] = self.sort(arr[start : mid])

        # Sort the right part of the array
        right: List[int] = self.sort(arr[mid:])

        # Merge this two array
        return self.merge(left, right)


    def merge(self, nums1: List[int], nums2 :List[int]) -> List[int]:
        # Get the length of nums1 and nums2 array
        N1: int = len(nums1)
        N2: int = len(nums2)
        
        # Merged array
        merged: List[int] = []

        # Create two pointers for this two array
        i: int = 0
        j: int = 0


        while i < N1 and j < N2:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        
        # Put all the remaining elements in the merged array
        while i < N1:
            merged.append(nums1[i])
            i += 1

        while j < N2:
            merged.append(nums2[j])
            j += 1

        return merged
    


if __name__ == "__main__":
    arr: List[int] = [3, 5, 2, 4, 7, 1, 6]
    obj = MergeSort()
    ans: List[int] = obj.sort(arr)
    print(ans)