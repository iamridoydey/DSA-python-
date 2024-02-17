from typing import List

class SubSetIteration:
    def subSet(self, nums: List[int]) -> List[List[int]]:
        sets: List[List[int]] = []

        # Put the first List to the sets
        sets.append([])

        for i in range(len(nums)):

            # Get the length of sets
            N: int = len(sets)
            for j in range(N):
                # Create a list to put new item
                new: List[int] = sets[j] + [nums[i]]
                # If there is an duplicate item
                # Then there is the possibilities to add list again hence need to skip
                if new not in sets:
                    sets.append(new)

        return sets
    
    

if __name__ == "__main__":
    obj = SubSetIteration()
    arr: List[int] = [1, 2, 2, 3]
    sets: List[List[int]] = obj.subSet(arr)
    print(sets)
