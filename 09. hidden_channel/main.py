import re

mapping = {
    'A': 'А',
    'B': 'В',
    'C': 'С',
    'D': 'Ⅾ',
    'E': 'Е',
    'F': '℉',
    'G': 'Ġ',
    'H': 'Н',
    'I': 'Ⅰ',
    'J': 'Ĵ',
    'K': 'К',
    'L': 'Ⅼ',
    'M': 'М',
    'N': 'Ń',
    'O': 'О',
    'P': 'Р',
    'Q': 'Ő',
    'R': 'Ř',
    'S': 'Ş',
    'T': 'Т',
    'U': 'Ů',
    'V': 'Ⅴ',
    'W': 'Ŵ',
    'X': 'Х',
    'Y': 'У',
    'Z': 'Ż'
}

rev_mapping = dict((v, k) for k, v in mapping.items())


def main():
    container = read_file('container.txt')
    payload = read_file('payload.txt')
    payload = re.sub(r'\W', '', payload)
    encoded = hide(payload, container)

    with open('result.txt', 'w') as f:
        f.write(encoded)

    extracted = extract(encoded)
    print(extracted)


def read_file(filename):
    with open(filename) as f:
        return f.read()


def hide(payload: str, container: str):
    payload_index = 0
    last_replacement = 0
    while payload_index < len(payload):
        current_char = payload[payload_index]
        index = container.find(current_char, last_replacement)
        if index < 0:
            break
        new_char = mapping[current_char]
        container = container[:index] + new_char + container[index + 1:]
        last_replacement = index
        payload_index += 1

    return container


def extract(inp: str):
    result = []
    for c in inp:
        if c in rev_mapping:
            result.append(rev_mapping[c])

    return ''.join(result)


if __name__ == '__main__':
    main()
