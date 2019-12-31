from secrets import randbits
from Crypto.Cipher import AES
from hashlib import md5


def main():
    print("Storing bit with encryption")
    encrypt()
    print()
    print("Storing bit with hash")
    hashing()


def encrypt():
    key = randbits(16 * 8)
    r = randbits(15 * 8 + 7)
    b = randbits(1)
    input_bytes = r << 1 | b
    aes = AES.new(key.to_bytes(16, "big"))

    ciphertext = aes.encrypt(input_bytes.to_bytes(16, "big"))
    print(f'Alice sent E(k,rb),r to Bob: {ciphertext}, {r}')

    b2 = randbits(1)
    print(f'Bob sent his bit to Alice: {b2}')
    print(f'Alice sent her key to Bob: {key}')

    plaintext = aes.decrypt(ciphertext)
    b3 = int.from_bytes(plaintext, "big") & 1
    print(f'Bob decrypted data and got: {str(b3)}')
    if b2 == b3:
        print("bits are the same")
    else:
        print("bits are different")


def hashing():
    r1 = randbits(7 * 8)
    r2 = randbits(8 * 8)
    b = randbits(1)
    alice_hash = get_hash(r1,r2,b)
    print(f'Alice sent H(r1,r2,b),r1 to Bob: {alice_hash}, {r1}')

    b2 = randbits(1)
    print(f'Bob sent his bit to Alice: {b2}')
    print(f'Alice sent r2 to Bob: ${r2}')

    bob_hash = get_hash(r1, r2, b2)
    if alice_hash == bob_hash:
        print("bits are the same")
    else:
        print("bits are different")


def get_hash(r1, r2, b):
    input_bytes = r1 << 8 * 8 | r2 << 1 | b

    return md5(input_bytes.to_bytes(16, "big")).hexdigest()


if __name__ == '__main__':
    main()
