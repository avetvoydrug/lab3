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






























# import re
# 
# def is_valid_phone_number(phone_number):
#     pattern = r'^(\+\d{1,3}\s?)?(\()?(\d{3})(?(2)\))[-.\s]?(\d{3})[-.\s]?(\d{4})$'
#     return re.match(pattern, phone_number) is not None
# 
# # Пример использования
# phone_numbers = [
#     "+1 123-456-7890",
#     "1234567890",
#     "(123) 456-7890",
#     "+91 1234567890",
#     "123-456-7890",
#     "123.456.7890",
#     "+123 4567890",
#     "+12 (345) 678-90",
#     "12-34-5678-90"
# ]
# 
# for phone_number in phone_numbers:
#     if is_valid_phone_number(phone_number):
#         print(f"{phone_number} - корректный номер телефона")
#     else:
#         print(f"{phone_number} - некорректный номер телефона")
# st = '89159153128'
# if len(st) == 11 and st[:2] == '89':
#     cnt = 2
#     for i in range(2, len(st)):
#         if st[i] in '0123456789':
#             cnt += 1
#     if cnt == 11:
#         print('good blyat 89')
#     else:
#         print('eto ne nomer')
# elif len(st) == 12 and st[:3] == '+79':
#     cnt = 2
#     for i in range(2, len(st)):
#         if st[i] in '0123456789':
#             cnt += 1
#     if cnt == 12:
#         print('good blyat num +7')
#     else:
#         print('eto ne nomer')


        