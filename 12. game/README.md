# Игра
Два игрока играют в камень-ножницы-бумага.

Алгоритм хода:
* Игроки шифруют свои значения с помощью AES-128
* Отправляют друг другу зашифрованные значения
* Обмениваются ключами
* Расшифровывают значения друг друга

## Подготовка
Нужно установить библиотеку pycrypto:
`pip3 install pycrypto`

## Запуск
`python3 main.py`
