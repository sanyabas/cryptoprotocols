import random

PRIME = 2 ** 127 - 1


def main():
    share_count = int(input('People number to share a secret: '))
    recover_count = int(input('People number to recover a secret: '))

    secret, shares = create_secret(recover_count, share_count)

    print('Generated secret:', secret)
    print('Shared secret parts:\n\t' + '\n\t'.join(map(str, shares)))

    for i in range(2, share_count + 1):
        print(f'{i} people recovered: ', recover_secret(shares[:i]))


def create_secret(recover_count: int, share_count: int):
    if recover_count > share_count:
        raise ValueError('Invalid parameters')

    polynomial = [random.randint(0, PRIME) for _ in range(recover_count)]
    shares = [(i, eval_polynomial(polynomial, i)) for i in range(1, share_count + 1)]

    return polynomial[0], shares


def eval_polynomial(polynomial, x: int) -> int:
    result = 0

    for c in reversed(polynomial):
        result = (result * x + c) % PRIME

    return result


def recover_secret(shares):
    if len(shares) < 2:
        raise ValueError('Too few points')

    return interpolate_polynomial(0, *zip(*shares), PRIME)


def interpolate_polynomial(x, x_s, y_s, p):
    k = len(x_s)

    numbers = []
    dividers = []

    for i in range(k):
        others = list(x_s)
        current = others.pop(i)

        numbers.append(eval_pi(x - o for o in others))
        dividers.append(eval_pi(current - o for o in others))

    divider = eval_pi(dividers)
    number = sum([divide_mod(numbers[i] * divider * y_s[i] % p, dividers[i], p) for i in range(k)])

    return (divide_mod(number, divider, p) + p) % p


def eval_pi(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


def divide_mod(number: int, divider: int, modulo: int) -> int:
    return number * extended_euclidean(divider, modulo)


def extended_euclidean(a: int, b: int) -> int:
    old_x, x = 0, 1
    old_y, y = 1, 0

    while b != 0:
        q = a // b

        a, b = b, a % b

        old_x, x = x - q * old_x, old_x
        old_y, y = y - q * old_y, old_y

    return x


if __name__ == '__main__':
    main()
