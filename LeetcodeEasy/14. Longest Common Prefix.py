from typing import List


class Solution:
    def longestCommonPrefix1(self, strs:List[str]) ->str:
        l = list(zip(*strs))
        print(l)
        # l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        prefix = ""
        for i in l:
            if(len(set(i))) == 1:
                prefix += i[0]
            else:
                break
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0: return ""

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

        # for i in range(len(strs[0])):
        #     ch = strs[0][i]
        #
        #     for j in range(1, len(strs)):
        #         if i == len(strs[j]) or strs[j][i] != ch:
        #             return strs[0][:i]
        #
        # return strs[0] if strs else ""


if __name__ == "__main__":
    lists = [["flower","flow","flight"], ["dog","racecar","car"]]

    for l in lists:
        print(Solution().longestCommonPrefix2(l))
