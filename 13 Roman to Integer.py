class Solution:
    def convertToInt(self, s: str) -> int:
        if s == "I": return 1
        if s == "V": return 5
        if s == "X": return 10
        if s == "L": return 50
        if s == "C": return 100
        if s == "D": return 500
        if s == "M": return 1000

    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            cur = self.convertToInt(s[i])
            if i < len(s) - 1:
                next = self.convertToInt(s[i+1])
                # Subtraction cases
                if cur < next:
                    sum += (next - cur)
                    i += 1
                else:
                    sum += cur
            else:
                sum += cur
            i += 1
        return sum
