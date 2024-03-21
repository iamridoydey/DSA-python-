class BasicMaze:
    def numsOfPath(self, grid: int) -> int:
        return self.paths(grid - 1, grid - 1)
    
    def paths(self, x: int, y: int) -> int:
        # Base Condition
        if x == 0 or y == 0:
            return 1
        
        left: int = self.paths(x - 1, y)
        right: int = self.paths(x, y - 1)

        return left + right
    

if __name__ == "__main__":
    obj = BasicMaze()
    paths: int = obj.numsOfPath(3)
    print(paths)