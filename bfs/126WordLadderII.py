from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        neighbors = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                placeholder = w[:i] + '_' + w[i + 1:]
                neighbors[placeholder] += [w]

        # bfs + build up tree
        tree = defaultdict(set)
        cur_layer = {beginWord}

        while cur_layer and not endWord in cur_layer:
            next_layer = defaultdict(set)

            for word in cur_layer:
                for i in range(len(word)):
                    placeholder = word[:i] + '_' + word[i + 1:]
                    for neigh in neighbors[placeholder]:
                        if not neigh in tree:
                            next_layer[neigh].add(word)

            tree.update(next_layer)
            cur_layer = next_layer

        def dfs(source, dest):
            if source == dest:
                return [[source]]
            return [pre_path + [dest] for parent in tree[dest] for pre_path in dfs(source, parent)]

        return dfs(beginWord, endWord)