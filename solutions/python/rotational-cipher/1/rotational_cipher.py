def rotate(text, key):
    key %= 26
    result = []

    for letter in text:
        if 'a' <= letter <= 'z':
            base = ord('a')
            result.append(chr((ord(letter) - base + key) % 26 + base))
        elif 'A' <= letter <= 'Z':
            base = ord('A')
            result.append(chr((ord(letter) - base + key) % 26 + base))
        else:
            result.append(letter)

    return ''.join(result)
