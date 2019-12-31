from Crypto.Cipher import AES
from enum import Enum
from random import choice
from secrets import randbits


class Move(Enum):
    Stone = 'Stone'
    Scissors = 'Scissors'
    Paper = 'Paper'

    @classmethod
    def choice(cls) -> 'Move':
        return choice([cls.Stone, cls.Scissors, cls.Paper])


def pad(plaintext):
    pad_len = 16 - (len(plaintext) % 16)
    padding = ''.join([chr(pad_len) for _ in range(pad_len)])

    return plaintext + padding


def unpad(text):
    return text[:text[-1]]


def main():
    first_key = randbits(16 * 8).to_bytes(16, 'big')
    second_key = randbits(16 * 8).to_bytes(16, 'big')

    first_aes = AES.new(first_key)
    second_aes = AES.new(second_key)

    first_move = first_aes.encrypt(pad(Move.choice().value))
    second_move = second_aes.encrypt(pad(Move.choice().value))

    print('First player sent:', first_move)
    print('Second player sent:', second_move)

    print('Players exchanged their keys')

    first_decrypted = unpad(first_aes.decrypt(first_move))
    second_decrypted = unpad(second_aes.decrypt(second_move))

    print('Original moves: ', first_decrypted.decode(), second_decrypted.decode())


if __name__ == '__main__':
    main()
