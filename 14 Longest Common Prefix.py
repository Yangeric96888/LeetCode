def longestCommonPrefix(self, strs: list[str]) -> str:
    length = len(min(strs))
    prefix = ""
    for i in range(length):
        for ii in strs:
            if ii[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]

    return prefix
