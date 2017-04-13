# unicode2utf8
**python代码展示unicode用utf8编码过程**  
**BUT! 这个不能用来做unicode的utf-8编码\!**

### 编码规则
|     Unicode           | UTF-8                               |
| --------------------- | ------------------------------------|
| 0000 0000 - 0000 007F | 0xxxxxxx                            |
| 0000 0080 - 0000 07FF | 110xxxxx 10xxxxxx                   |
| 0000 0800 - 0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx          |
| 0001 0000 - 0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

**举例说明编码过程**  
```python
# -*- coding: utf-8 -*-
print repr(u"你")    # u'\u4f60'
```
**可见“你”的unicode编码为十六进制4F60, 对应的二进制为100111101100000**  
**4F60在第三个区间内，对应的编码规则是 1110xxxx 10xxxxxx 10xxxxxx**  
**100111101100000从末尾开始6位一切，得到 100 111101 100000**  

|   part-1         |   part-2         | part-3          |
| --------:        | --------:        | --------:       |
| 1 0 0            | 1 1 1 1 0 1      | 1 0 0 0 0 0     |
| 1 1 1 0 x x x x  | 1 0 x x x x x x  | 1 0 x x x x x x |
| 1 1 1 0 0 1 0 0  | 1 0 1 1 1 1 0 1  | 1 0 1 0 0 0 0 0 |
| E4               | BD               | A0              |
_part-1 100填入1110xxxx不够的位，用0填补_

**最后看一下结果**
```python
# -*- coding: utf-8 -*-
print repr(u"你".encode("utf-8"))    # '\xe4\xbd\xa0'
```

**bingo!**