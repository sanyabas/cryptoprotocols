# Программа с закладкой

Программа запрашивает команду (используется для генерации ключа) и исходный текст, после чего зашифровывает его с помощью AES-256.

Если передать в качестве команды слово `hack`, то ключ будет равен 32 нулям.

## Подготовка
Нужно установить библиотеку pycrypto:
`pip3 install pycrypto`

##  Запуск
`python3 main.py` 
