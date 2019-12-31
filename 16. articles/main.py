from hashlib import sha1

secret = 'secret'
articles_for_test = [
    {
        'text': 'Вакансия python-программиста. Справки по телефону.',
        'tel': '79368110558'
    },
    {
        'text': 'Продается гараж.',
        'tel': '79800079860'
    },
    {
        'text': 'Сдам квартиру в центре. Недорого.',
        'tel': '79510096299'
    }
]


def get_hash(msg):
    sha_hash = int.from_bytes(sha1(msg.encode()).digest(), 'big')

    return '79' + str(sha_hash)[-9:]


def check_article(article):
    return get_hash(secret) == article['tel']


def main():
    result = [(check_article(articles_for_test[i]), i) for i in range(len(articles_for_test))]
    matches = map(lambda x: str(x[1]), filter(lambda x: x[0], result))

    print('Matched articles: ', ' '.join(matches))


if __name__ == '__main__':
    main()
