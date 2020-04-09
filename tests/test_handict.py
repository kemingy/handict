import pathlib
from handict import Handict

USER_DICTIONARY = pathlib.Path(__file__).absolute().parent / 'userdict.txt'


def test_handict():
    handict = Handict(USER_DICTIONARY)
    assert list(handict.segment('研究生命起源')) == ['研究', '生命', '起源']
