import re

def is_valid_russian_phone_number(phone_number):
    pattern = r'^((\+7|8)( |-)?)?(\()?([489]\d{2})(?(3)\))[-.\s]?(\d{3})[-.\s]?(\d{2})[-.\s]?(\d{2})$'
    return re.match(pattern, phone_number) is not None

# Пример использования
phone_numbers = ['89199195195',
                 '999999999999999999999',
                 '88005553535',
                 ]

for phone_number in phone_numbers:
    if is_valid_russian_phone_number(phone_number):
        print(f"{phone_number} - корректный российский номер телефона")
    else:
        print(f"{phone_number} - некорректный российский номер телефона")