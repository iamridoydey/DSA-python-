from typing import List

class Maze:
    def allPaths(self, arr: List[List], r: int, c: int) -> int:
        #Base Condition
        if r == len(arr) - 1 and c == len(arr[0]) - 1:
            return 1
        
        # Mark the current cell as visited
        arr[r][c] = False

        route: int = 0
        # Move to right
        if c < len(arr[0]) - 1:
            if arr[r][c + 1] == True:
                route += self.allPaths(arr, r, c + 1)

        # Move to left
        if c > 0:
            if arr[r][c - 1] == True:
                route += self.allPaths(arr, r, c - 1)
        
        # Move to down
        if r < len(arr) - 1:
            if arr[r + 1][c] == True:
                route += self.allPaths(arr, r + 1, c)
        
        # Move to up
        if r > 0:
            if arr[r - 1][c] == True:
                route += self.allPaths(arr, r - 1, c)

        # Mark the cell as not visited (Backtrack)
        arr[r][c] = True
        return route
    

    
    def printAllPaths(self, arr: List[List], strs: List[List], up, r: int, c: int) -> None:
        #Base Condition
        if r == len(arr) - 1 and c == len(arr[0]) - 1:
            # Mark last cell as visited
            arr[r][c] = False
            self.display(strs)
            print(up)
            print()
            # Mark last cell as not visited
            arr[r][c] = True
            return
        
        # Mark the current cell as visited
        arr[r][c] = False

        # Move to right
        if c < len(arr[0]) - 1:
            if arr[r][c + 1] == True:
                strs[r][c + 1] = "R"
                self.printAllPaths(arr, strs, up + "R", r, c + 1)
                strs[r][c + 1] = ""

        # Move to left
        if c > 0:
            if arr[r][c - 1] == True:
                strs[r][c - 1] = "L"
                self.printAllPaths(arr, strs, up + "L", r, c - 1)
                strs[r][c - 1] = ""
        
        # Move to down
        if r < len(arr) - 1:
            if arr[r + 1][c] == True:
                strs[r + 1][c] = "D"
                self.printAllPaths(arr, strs, up + "D", r + 1, c)
                strs[r + 1][c] = ""
        
        # Move to up
        if r > 0:
            if arr[r - 1][c] == True:
                strs[r - 1][c] = "U"
                self.printAllPaths(arr, strs, up + "U", r - 1, c)
                strs[r - 1][c] = ""

        # Mark the cell as not visited (Backtrack)
        arr[r][c] = True
    

    def display(self, strs:List[List]) -> None:
        for str in strs:
            for s in str:
                if s:
                    print(s, end=" ")
                else:
                    print("X", end=" ")

            print()


if __name__ == "__main__":
    obj = Maze()  
    arr: List[List] = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True]
    ]  
    # arr: List[List] = [
    #     [True, True, True],
    #     [True, True, True],
    #     [True, True, True]
    # ] 

    # Initialize a 2D list of strings with the same dimensions as arr
    strs = [["" for _ in range(len(arr[0]))] for _ in range(len(arr))]

    obj.printAllPaths(arr, strs, "", 0, 0) 
    paths: int = obj.allPaths(arr, 0, 0)
    print(f"Total Paths: {paths}")