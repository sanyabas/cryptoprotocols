from Crypto.PublicKey import RSA


def main():
    n = int(input('Documents count: '))
    amount = int(input('Document amount: '))

    # Публичный и секретный ключи RSA банка
    bank_priv = RSA.generate(2048)
    bank_pub = bank_priv.publickey()
    # Публичный и секретный ключи Боба
    bob_priv = RSA.generate(2048)
    bob_pub = bob_priv.publickey()

    # Боб готовит n документов, маскирует их уникальными множителями
    documents = [bob_priv.sign(amount, _) for _ in range(n)]

    # Банк случайно выбирает n-1 документ
    verify_documents = documents[:-1]

    # Банк вскрывает их и убеждается в корректности
    for signature in verify_documents:
        assert bob_pub.verify(amount, signature)

    # Банк подписывает оставшийся документ
    message = documents[-1]
    print('Signed document: ', bank_priv.sign(message[0], None)[0])


if __name__ == '__main__':
    main()
