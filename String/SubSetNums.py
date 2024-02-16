from typing import List

class SubSetNums:
    def subSet(self, unprocessed: List[int], processed:List[int]) -> List[List[int]]:
        set: List[List[int]] = []

        # Base condition
        if len(processed) == 0:
            return [unprocessed]
        
        # Get the ans from left call
        left: List[List[int]] = self.subSet(unprocessed + processed[0:1], processed[1:])

        # Get the ans from right call
        right: List[List[int]] = self.subSet(unprocessed, processed[1:])

        # Merge left and right
        return left + right
    

if __name__ == "__main__":
    obj = SubSetNums()
    arr: List[int] = [3, 5, 9]
    ans: List[List[int]] = obj.subSet([], arr)
    print(ans)