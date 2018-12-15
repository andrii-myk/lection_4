


def encrypt(text, offset):
    result = ""
    for letter in text:
        if (letter >= 'a' and letter <= 'z'):
            s = (ord(letter) - ord('a') + offset) % 26 + ord('a')
            result += chr(s)
        else:
            s = (ord(letter) - ord('A') + offset) % 26 + ord('A')
            result += chr(s)
    return result


def decrypt(text, offset):
    result = ""
    for letter in text:
        if (letter >= 'a' and letter <= 'z'):
            s = (ord(letter) - ord('a') - offset) % 26 + ord('a')
            result += chr(s)
        else:
            s = (ord(letter) - ord('A') - offset) % 26 + ord('A')
            result += chr(s)
    return result


print(encrypt('zzz', 52))

s = encrypt("zzz", 8)
print(decrypt(s, 8))