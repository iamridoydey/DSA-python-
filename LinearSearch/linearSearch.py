from typing import List

# linear search algorithm
def search (arr : List[int], target: int) -> int:
    # Run a for loop to check all the element to find the target
    for i in range(len(arr)):
        if (target == arr[i]):
            return i
        
    
if __name__ == "__main__":
    arr: List[int] = [2, 3, 5, 7, 1, 4, 12]
    ans: int = search(arr, 7)

    print(ans)