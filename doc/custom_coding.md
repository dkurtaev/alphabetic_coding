# Custom coding
Feel free to use your own coding table.
But be careful: it might be is not bijective.  
Coding ```f(x)``` has not bijection property if exists two different
words ```A``` and ```B``` for which ```f(A) = f(B)```.

## Encoding
```python
>>> from custom_coding import encode_custom
>>>
>>> coding_table = {
...   'a': '010',
...   'b': '101',
...   'c': '11'
... }
>>> encode_custom('abcbabca', coding_table)
'0101011110101010111010'
```

## Decoding
```python
>>> from custom_coding import decode_custom
>>>
>>> coding_table = {
...   'a': '010',
...   'b': '101',
...   'c': '11'
... }
>>> decode_custom('0101011110101010111010', coding_table)
'abcbabca'
```
