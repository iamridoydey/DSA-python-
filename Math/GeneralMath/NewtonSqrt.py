# Newton Raphson Method

class NewtonSqrt:
    def sqrt(self, N:int, epsilon: float = 1e-10):
        # Assume x is N
        x: int = N
        root: float
        while True:
            root = 0.5 * (x + (N / x))

            # Check the error limit
            if abs(root - x) < epsilon:
                break
            
            x = root

        return root

if __name__ == "__main__":
    root = NewtonSqrt()
    N: int = 21
    ans: float = root.sqrt(N)
    print(ans)
