from collections import defaultdict, deque
from typing import List


class Solution:
    @staticmethod
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList: return 0

        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(len(beginWord)):
                all_combo_dict[word[:i] + '_' + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            cur_word, dis = queue.popleft()

            for i in range(len(beginWord)):
                transform_word = cur_word[:i] + '_' + cur_word[i + 1:]

                for word in all_combo_dict[transform_word]:
                    if word == endWord: return dis + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, dis + 1))
        return 0


if __name__ == '__main__':
    beginWord, endWord = 'hit', 'cog'
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(Solution.ladderLength(beginWord, endWord, wordList))