# Handict

![Python package](https://github.com/kemingy/handict/workflows/Python%20package/badge.svg)

Yet another word segmentation tools.

## Tutorial

**Install**: `pip install handict`

```python
from handict import Handict

han = Handict('path_of_user_dict_file') # the same format as jieba dict 
han.segment('中文自然语言处理太难了')
```

## References

* http://technology.chtsai.org/mmseg/
* http://yongsun.me/2013/06/simple-implementation-of-mmseg-with-python/