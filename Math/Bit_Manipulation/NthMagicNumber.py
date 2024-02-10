# Find Nth Magic number:
    # Magic number should be like bit of a number 2: 10 -> 1 * 5^2 + 1 * 5^1

class Magic:
    def magicNum(self, N:int):
        base: int = 5
        magic: int = 0
        while N != 0:
            magic += (N & 1) * base
            base *= 5
            N >>= 1
        
        return magic
    


if __name__ == "__main__":
    magic = Magic()
    n: int = 5
    ans: int = magic.magicNum(n)
    print(ans)