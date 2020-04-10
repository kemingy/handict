from math import log1p
from statistics import variance
from typing import List, Iterator

from .trie import Trie, Word


class Chunk:
    def __init__(self, words: List[Word]):
        self.words = words
        self.lens: List[int] = list(map(len, words))
        self.total_len: int = sum(self.lens)
        self.num = len(words)
        self.mean = self.total_len / len(words)
        self.var = -variance(self.lens) if len(words) > 1 else 0
        self.degree = sum(log1p(word.freq) for word in words if len(word) == 1)

    def __lt__(self, other):
        return (self.total_len, self.mean, self.var, self.degree) < \
               (other.total_len, other.mean, other.var, other.degree)


class Handict:
    def __init__(self, dictionary: str):
        self.trie = Trie(dictionary)

    def _get_chunks(self, text: str, offset: int, depth: int = 3, words: List[Word] = None):
        if words is None:
            words = []

        if depth == 0 or offset >= len(text):
            if words:
                yield Chunk(words)
        else:
            matches = self.trie.search(text, offset)
            if not matches:
                yield from self._get_chunks(text, offset + 1, depth - 1, words + [Word(text[offset])])
            for word in matches:
                yield from self._get_chunks(text, offset + len(word), depth - 1, words + [word])

    def segment(self, text: str) -> Iterator[str]:
        i = 0
        while i < len(text):
            best_chunk = max(self._get_chunks(text, i))
            match = best_chunk.words[0]
            i += len(match)
            yield match.word
