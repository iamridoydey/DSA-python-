from typing import List

class Maze:
    def paths(self, arr: List[List], r: int, c: int) -> int:
        # Base condition
        if r == len(arr) - 1 and c == len(arr[0]) - 1:
            return 1
        

        # Check for the restriction
        if not arr[r][c]:
            return 0
        
        route: int = 0

        # Move towards right
        if c < len(arr[0]) - 1:
            route += self.paths(arr, r, c + 1)

        # Move diagonally
        if r == c and r < len(arr) - 1 and c < len(arr[0]) - 1:
            route += self.paths(arr, r + 1, c + 1)

        # Move to down
        if r < len(arr) - 1:
            route += self.paths(arr, r + 1, c)

        return route
    

    def printPaths(self, arr: List[List],up, r: int, c: int) -> None:
        # Base condition
        if r == len(arr) - 1 and c == len(arr[0]) - 1:
            print(up)
            return
        

        # Check for the restriction
        if not arr[r][c]:
            return
        

        # Move towards right
        if c < len(arr[0]) - 1:
            self.printPaths(arr, up + "R", r, c + 1)

        # Move diagonally (Askew)
        if r == c and r < len(arr) - 1 and c < len(arr[0]) - 1:
            self.printPaths(arr, up + "A", r + 1, c + 1)

        # Move to down
        if r < len(arr) - 1:
            self.printPaths(arr, up + "D", r + 1, c)

    


if __name__ == "__main__":
    obj = Maze()
    arr:List[List] = [
        [True, True, True],
        [True, False, True],
        [True, True, True],
        [True, True, True]
    ]

    paths: int = obj.paths(arr, 0, 0)
    obj.printPaths(arr, "", 0, 0)
    print(paths)