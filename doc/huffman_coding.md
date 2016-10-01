# Huffman coding
Huffman coding - method which gives optimal prefix coding for source text.
Method considers characters frequency: for most frequently used characters used
binary sequences as shorter as possible (Keep prefix property: any code is not
prefix of any other).

## Encoding
```python
>>> from huffman_coding import encode_huffman
>>>
>>> encoded_text, coding_table = code_huffman('mamihlapinatapai')
>>> coding_table
{ 'a': '11',
  'i': '00',
  'm': '010',
  'p': '011',
  'h': '1000',
  'l': '1001',
  'n': '1010',
  't': '1011' }
>>> encoded_text
'01011010001000100111011001010111011110111100'
```

## Decoding
```python
>>> from huffman_coding import decode_huffman
>>>
>>> coding_table = {
...   'a': '11',
...   'i': '00',
...   'm': '010',
...   'p': '011',
...   'h': '1000',
...   'l': '1001',
...   'n': '1010',
...   't': '1011'
... }
>>> decode_huffman('01011010001000100111011001010111011110111100',
                   coding_table)
'mamihlapinatapai'
```
