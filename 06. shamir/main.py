import random


def random_prime(st, end):
    prime = False
    n = 3

    while not prime:
        n = random.randint(st, end)
        if n % 2 != 0:
            for x in range(3, int(n ** 0.5), 2):
                if n % x == 0:
                    break
            else:
                prime = True

    return n


def random_int():
    return random.randint(3, 100)


def generate_d(p, c):
    d = 3
    while (c * d) % (p - 1) != 1:
        d += 2

    return d


def encrypt(arg, exponent, modulus):
    return pow(arg, exponent, modulus)


def print_action(key, value):
    print(f'{key}: {value}')


def main():
    p = 7541
    e = random_prime(1000, 2000)
    d = generate_d(p, e)

    b = random_prime(1000, 2000)
    c = generate_d(p, b)

    key = int(input('Key to negotiate (<7541): '))

    x1 = encrypt(key, e, p)
    print(f'E(e,M)={x1}')
    x2 = encrypt(x1, b, p)
    print(f'E(b,E(e,M))={x2}')
    x3 = encrypt(x2, d, p)
    print(f'D(e,E(b,E(e,M)))={x3}')
    x4 = encrypt(x3, c, p)
    print(f'D(b,D(e,E(b,E(e,M))))={x4}')

    print(f'Negotiated key: {x4}')


if __name__ == '__main__':
    main()
