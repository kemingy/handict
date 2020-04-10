import pathlib
from handict import Handict

USER_DICTIONARY = pathlib.Path(__file__).absolute().parent / 'userdict.txt'


def test_handict():
    handict = Handict(USER_DICTIONARY)
    assert list(handict.segment('国际化')) == ['国际化']
    assert list(handict.segment('研究生命起源')) == ['研究', '生命', '起源']
    assert list(handict.segment('主要是因为')) == ['主要', '是', '因为']
