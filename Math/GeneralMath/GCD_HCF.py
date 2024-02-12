# GCD or HCF

class GCD_HCF:
    def gcd(self, num1: int, num2: int) -> int:
        # Base condition
        if num1 == 0:
            return num2
        
        return self.gcd(num2 % num1, num1)


if __name__ == "__main__":
    euclid = GCD_HCF()
    gcd_hcf = euclid.gcd(21, 9)
    print(gcd_hcf)