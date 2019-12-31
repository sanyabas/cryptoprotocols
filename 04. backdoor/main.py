from secrets import randbits
from Crypto.Cipher import AES


def main():
    command = input('Enter command: ')
    if len(command) < 4:
        print('Command should be at least 4 letters long')
        return
    key = get_key(command)
    print(key)
    aes = AES.new(key)
    plaintext = input('Enter plaintext: ')
    ciphertext = aes.encrypt(pad(plaintext))
    print(ciphertext)


def pad(plaintext):
    pad_len = 16 - (len(plaintext) % 16)
    padding = ''.join([chr(pad_len) for _ in range(pad_len)])

    return plaintext + padding


def get_key(command: str):
    key1 = randbits(16 * 8)
    key2 = key1
    key2 <<= ord(command[0])
    key2 >>= ord(command[1])
    key2 <<= ord(command[2])
    key2 >>= (ord(command[3]) - 1)

    return (key1 ^ key2).to_bytes(32, 'big')


if __name__ == '__main__':
    main()
