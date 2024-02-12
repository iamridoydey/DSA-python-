from GCD_HCF import GCD_HCF

class LCM:
    def lcm(self, num1: int, num2: int) -> int:
        return int((num1 * num2) / GCD_HCF().gcd(num1, num2))
    

if __name__ == "__main__":
    # Least Common Factors
    math = LCM()
    ans = math.lcm(21, 9)
    print(ans)