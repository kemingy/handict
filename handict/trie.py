import pathlib


class Node:
    def __init__(self, word=None):
        self.word = word
        self.trans = {}
        self.freq = 0

    def __len__(self):
        return len(self.word) or 0

    def __repr__(self):
        return f'<{self.word}:{self.freq}>'


class Trie:
    def __init__(self, dictionary):
        self.root = Node()
        self.num = 0
        self.load(dictionary)

    def add(self, word, freq):
        node = self.root
        for char in word:
            if char not in node.trans:
                node.trans[char] = Node()
            node = node.trans[char]

        node.word = word
        node.freq = freq
        self.num += 1

    def load(self, dictionary, toleration=0.2):
        assert pathlib.Path(dictionary).is_file(), f'Wrong file path: {dictionary}'
        failure = 0
        with open(dictionary, mode='r', encoding='utf-8') as f:
            for line in f:
                cols = line.strip().split(' ')
                if len(cols) >= 2:
                    try:
                        word, freq = cols[0], int(cols[1])
                    except ValueError:
                        failure += 1
                        continue
                elif len(cols) == 1 and cols[0]:
                    word, freq = cols[0], 0
                else:
                    continue
                self.add(word, freq)

        if failure / self.num > toleration:
            raise ValueError(f'Too many parse errors. ({failure}/{self.num})')

    def search(self, text):
        words = []
        node = self.root

        for char in text:
            if char not in node.trans:
                break
            node = node.trans[char]
            if node.word:
                words.append(node)

        return words
