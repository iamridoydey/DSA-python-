class SkipCharacter:
    def skip(self, text: str, skipChar: str) -> str:
        if len(text) in (0, 1):
            return text
    
        temp = text[0] if text[0] != skipChar else ""

        return temp + self.skip(text[1:], skipChar)
    

if __name__ == "__main__":
    obj = SkipCharacter()
    ans: str = obj.skip("baccad", "a")
    print(ans)