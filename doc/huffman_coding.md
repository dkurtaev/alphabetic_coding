# Huffman coding
Huffman coding - method which gives optimal prefix coding for source text.
Method considers characters frequency: for most frequently used characters used
binary sequences as shorter as possible (for prefix property).

## Encoding

```python
>>> from huffman_coding import HuffmanEncoder
>>> encoder = HuffmanEncoder()
>>> encoder.encode('my little string')
'101000000101101011111101110000011100111110101010111001'
```

## Decoding
```python
>>> from huffman_coding import HuffmanEncoder, HuffmanDecoder
>>> encoder = HuffmanEncoder()
>>> decoder = HuffmanDecoder()
>>> coding_table = encoder.get_coding_table('my little string')
>>> decoder.decode('101000000101101011111101110000011100111110101010111001',
                   coding_table)
'my little string'
```
