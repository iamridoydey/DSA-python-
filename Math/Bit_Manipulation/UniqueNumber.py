from typing import List
import math

class UniqueNumber:

    def uniqueNum(self, nums: List[int], appearance: int) -> int:
        # Get the max number binary representation length
        maxNum: int = self.getMax(nums)
        length = int(math.log(maxNum) / math.log(2)) + 1

        # Create an array of length 
        bits: List[int] = [0] * length

        # Get the binary representation of the number and when we got set bit
        # then just increase the ith position of the array for ith bit
        for num in nums:
            self.addBinary(num, bits)
        
        # Get the actual unique number
        ans: int = 0
        power:int = 1
        for i in range(length):
            if (bits[i] % appearance) == 1:
                ans += power
            
            power *= 2
        
        return ans
    
    def addBinary(self, num: int, bits: List[int]):
        i: int = 0

        while num != 0:
            bits[i] += num & 1

            num >>= 1
            i += 1
            

    def getMax(self, nums: List[int]) -> int:
        max: int = 0

        for i in nums:
            if max < i:
                max = i
        
        return max
    

if __name__ == "__main__":
    nums = [2, 2, 9, 2, 7, 7, 8, 7, 8, 8]
    unique = UniqueNumber()
    ans = unique.uniqueNum(nums, 3)
    print(ans)