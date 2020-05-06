def dfs(s, idxS, p, idxP, lenS, lenP):
    if idxP == lenP:
        return idxS == lenS
    elif idxP == lenP - 1 or p[idxP + 1] != '*':
        if idxS < lenS and (p[idxP] == '.' or p[idxP] == s[idxS]):
            return dfs(s, idxS + 1, p, idxP + 1, lenS, lenP)
        else:
            return False
    else:
        i = idxS - 1
        while i < lenS and (i < idxS or p[idxP] == '.' or p[idxP] == s[i]):
            if dfs(s, i + 1, p, idxP + 2, lenS, lenP):
                return True
            i += 1
        return False


def dfs(s, idxS, p, idxP, mem, lenS, lenP):
    if mem[idxS][idxP] is not None:
        return mem[idxS][idxP]

    if idxP == lenP:
        return idxS == lenS
    elif idxP == lenP - 1 or p[idxP + 1] != '*':
        if idxS < lenS and (p[idxP] == '.' or p[idxP] == s[idxS]):
            mem[idxS][idxP] = dfs(s, idxS + 1, p, idxP + 1, mem, lenS, lenP)
        else:
            return False
    else:
        i = idxS - 1
        while i < lenS and (i < idxS or p[idxP] == '.' or p[idxP] == s[i]):
            if dfs(s, i + 1, p, idxP + 2, mem, lenS, lenP):
                mem[idxS][idxP] = True
                return True
            i += 1
        mem[idxS][idxP] = False

    return mem[idxS][idxP]


class Solution:
    def isMatchNoPruning(self, s: str, p: str) -> bool:
        if not s or not p: return False
        return dfs(s, 0, p, 0, len(s), len(p))

    def isMatchWithPruning(self, s: str, p: str) -> bool:
        if not s or not p:
            return False

        mem = [[None for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        return dfs(s, 0, p, 0, mem, len(s), len(p))


if __name__ == '__main__':
    s = 'ab'
    p = '.*'
    # print(Solution().isMatchNoPruning(s, p))
    print(Solution().isMatchWithPruning(s, p))
