from typing import List

class SubSetString:
    def subSet(self, processed: str, unprocessed: str) -> List[str]:
        set: List[str] = []

        # Base Condition
        if unprocessed == "":
            return [processed]
        
        # Left subset
        left: List[str] = self.subSet(processed + unprocessed[0:1], unprocessed[1:])

        # Right subset
        right: List[str] = self.subSet(processed, unprocessed[1:])

        set += left + right
        return set
    

if __name__ == "__main__":
    obj = SubSetString()
    set: List[str] = obj.subSet("", "abc")
    print(set)