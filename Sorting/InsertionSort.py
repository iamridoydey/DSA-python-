from typing import List

class InsertionSort:
    def sort(self, arr: List[int]):
        # Length of the array
        N: int = len(arr)

        for i in range(N - 1):
            # Inner loop
            for j in range(i + 1, 0, -1):
                if j >= 0 and arr[j - 1] > arr[j]:
                    # Swap
                    temp: int = arr[j - 1]
                    arr[j - 1] = arr[j]
                    arr[j] = temp
                
                else:
                    break


if __name__ == "__main__":
    sorted = InsertionSort()

    arr: List[int] = [5, 3, 4, 1, 2]
    sorted.sort(arr)

    print(arr)