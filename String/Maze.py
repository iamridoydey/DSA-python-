class Maze:
    def maze(self, len: int) -> int:
        return self.__helper(0, 0, "", len)

    def __helper(self, x: int, y: int, s: str, len: int) -> int:
        # num of paths
        paths: int = 0
        # Base condition
        if x == len - 1 and y == len - 1:
            print(s)
            return 1
        
        # Move to the right
        if x < len - 1:
            paths += self.__helper(x + 1, y, s + "R", len)
        
        # Move to the down
        if y < len - 1:    
            paths += self.__helper(x, y + 1, s + "D", len)
        
        # Move diagonally
        if x < len - 1 and y < len - 1:    
            paths += self.__helper(x, y + 1, s + "d", len)
            

        return paths



if __name__ == "__main__":
    obj = Maze()
    paths: int = obj.maze(3)
    print(paths)