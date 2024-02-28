from typing import List

class Permutation:
    def permutation(self, s: str) -> List[str]:
        return self.__helper("", s)
    
    
    def __helper(self, processed: str, unprocessed: str) -> List[str]:
        # Base Condition
        if len(unprocessed) == 0:
            return [processed]
        
        # Get the length of the processed String
        N: int = len(processed)

        allList: List[str] = []
        for i in range(N + 1):
            s1 = processed[0:i]
            s2 = unprocessed[0]
            s3 = processed[i:]
            s = s1 + s2 + s3

            # Get the ans of the current function call and add it to the allList
            allList += self.__helper(s, unprocessed[1:])

        return allList



if __name__ == "__main__":
    obj = Permutation()
    allStr: List[str] = obj.permutation("abc")
    print(allStr)

