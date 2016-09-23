# Custom coding
Feel free to use your own coding table.
But be careful: it might be not bijective (more details later).

## Encoding
```python
>>> from custom_coding import Encoder
>>> coding_table = {
...   'a': '010',
...   'b': '101',
...   'c': '11'
... }
>>> encoder = Encoder()
>>> encoder.encode('abcbabca', coding_table)
'0101011110101010111010'
```

## Decoding
```python
>>> from custom_coding import Decoder
>>> coding_table = {
...   'a': '010',
...   'b': '101',
...   'c': '11'
... }
>>> decoder = Decoder()
>>> decoder.decode('0101011110101010111010', coding_table)
'abcbabca'
```
