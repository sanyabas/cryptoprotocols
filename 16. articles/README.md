# "Протокол извращенца"

## Описание
Искомое извращение задается в переменной secret. От этой переменной вычисляется sha1-хэш и последние 9 десятичных символов становятся номером телефона.

Проверяются объявления в газете, если номер телефона совпал с заданным хэшом, мы нашли нужного человека.

## Запуск
`python3 main.py`