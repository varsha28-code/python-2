from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        st = set(wordList)

        if endWord not in st:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, step = q.popleft()

            if word == endWord:
                return step

            for ind in range(len(word)):
                original = word[ind]

                for ch in range(ord('a'), ord('z') + 1):
                    new_word = word[:ind] + chr(ch) + word[ind + 1:]

                    if new_word in st:
                        st.remove(new_word)
                        q.append((new_word, step + 1))

        return 0
