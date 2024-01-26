from typing import List

class BubbleSort:
    def sort(self, arr: List[int]):
        # Length of the array
        N: int = len(arr)

        for i in range(N):
            isSwapped = False

            # inner loop
            for j in range(N - i - 1):
                if arr[j] > arr[j + 1]:
                    # swap the elment
                    temp: int = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    
                    isSwapped = True


            # If array is sorted after one pass it should not swapped
            if not isSwapped:
                break


if __name__ == "__main__":
    sorted = BubbleSort()

    arr: List[int] = [5, 3, 4, 1, 2]
    sorted.sort(arr)

    print(arr)