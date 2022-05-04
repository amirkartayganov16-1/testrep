# import re
#
# phone = input('Phone number: ')
# result = re.match(r"^\+([0-9]{1,3})-([0-9]{1,3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)
#
# try:
#     if phone[result.start():result.end()] == phone:
#         print('Phone number valid')
#     else:
#         raise "Is not valid phone number"
# except:
#     print('Is not valid phone number')

import re

email = "jackbarbara55official@yandex.ru"
result = re.match(r"^([a-zA-Z0-9]{5,30)@(gmail|mail|yandex|icloud|namba).(com|ru|kg)", email)

print(result)

