codes = {'A': '0', 'B': '10', 'C': '110', 'D': '111'}
words = list(codes.values())
assert all(not b.startswith(a) for a in words for b in words if a != b)
message = 'ABACADABAA'
stream = ''.join(codes[c] for c in message)
inverse = {v: k for k, v in codes.items()}
decoded, prefix = '', ''
for bit in stream:
    prefix += bit
    if prefix in inverse:
        decoded += inverse[prefix]
        prefix = ''
assert not prefix and decoded == message
print('Encoded bits:', len(stream), 'Fixed length:', 2*len(message))
