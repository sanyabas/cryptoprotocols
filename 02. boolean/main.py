import random


def main():
    pay = int(input('Who will pay? (0 - NSA или 1,2,3 - agents): '))

    first = throw_coin()
    second = throw_coin()
    third = throw_coin()

    print(f'Coins: {first} {second} {third}')

    first_result = third == first if pay != 1 else third != first
    second_result = first == second if pay != 2 else first != second
    third_result = second == third if pay != 3 else second != third

    print('First says that coins {}match'.format('' if first_result else 'don\'t '))
    print('Second says that coins {}match'.format('' if second_result else 'don\'t '))
    print('Third says that coins {}match'.format('' if third_result else 'don\'t '))

    result = first_result + second_result + third_result

    if result % 2:
        print('NSA will pay')
    else:
        print('Agent will pay')


def throw_coin() -> int:
    return random.choice([0, 1])


if __name__ == '__main__':
    main()
