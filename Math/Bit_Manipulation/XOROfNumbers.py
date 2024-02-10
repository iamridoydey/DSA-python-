class XOROfNumbers:
    def XOR_Of0_N(self, N:int) -> int:
        if N % 4 == 1:
            return 1
        elif N % 4 == 2:
            return N + 1
        elif N % 4 == 3:
            return 0
        else:
            return N
    

    def XORBetweenTwoNumbers(self, a: int, b: int) -> int:
        return self.XOR_Of0_N(b) - self.XOR_Of0_N(a)


if __name__ == "__main__":
    xor = XOROfNumbers()
    ans: int = xor.XORBetweenTwoNumbers(3, 9)
    print(ans)