
if __name__ == '__main__':
    def convertToInt( s: str) -> int:
        if s == "I": return 1
        if s == "V": return 5
        if s == "X": return 10
        if s == "L": return 50
        if s == "C": return 100
        if s == "D": return 500
        if s == "M": return 1000


    def romanToInt( s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            print("heyy ", i)
            cur = convertToInt(s[i])
            if i < len(s) - 1:
                cur = convertToInt(s[i])
                next = convertToInt(s[i + 1])
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

    print(romanToInt("IV"))

