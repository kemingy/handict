import pathlib
from typing import Dict, List, Optional


class Word:
    def __init__(self, word: Optional[str] = None):
        self.word = word
        self.trans: Dict[str, Word] = {}
        self.freq: int = 0

    def __len__(self) -> int:
        return len(self.word) if self.word else 0

    def __repr__(self) -> str:
        return f'<{self.word}:{self.freq}>'


class Trie:
    def __init__(self, dictionary: str):
        self.root: Word = Word()
        self.num: int = 0
        self.load(dictionary)

    def add(self, word: str, freq: int):
        node = self.root
        for char in word:
            if char not in node.trans:
                node.trans[char] = Word()
            node = node.trans[char]

        node.word = word
        node.freq = freq
        self.num += 1

    def load(self, dictionary: str, toleration: float = 0.2):
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

    def search(self, text: str) -> List[Word]:
        words: List[Word] = []
        node = self.root

        for char in text:
            if char not in node.trans:
                break
            node = node.trans[char]
            if node.word:
                words.append(node)

        return words
