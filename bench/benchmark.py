import pathlib
from time import time

import jieba

from handict import Handict

FILE = pathlib.Path(__file__).absolute().parent / 'weicheng.txt'
DICT = pathlib.Path(__file__).absolute().parent / 'jieba_dict.txt'


def bench(func, round=5):
    t0 = time()
    for _ in range(round):
        with open(FILE, 'r', encoding='utf-8') as f:
            for line in f:
                list(func(line))

    return (time() - t0) / round


if __name__ == '__main__':
    jieba.initialize()
    print(f'> jieba: {bench(jieba.cut)}')

    t0 = time()
    handict = Handict(DICT)
    print(f'Building trie tree takes {time() - t0}s')
    print(f'> handict: {bench(handict.segment)}')
