import re
#PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")
#value = "+380631312876"

#PHONE_REGEX = re.compile(r"\.")
#value = "+380631312876"

PHONE_REGEX = re.compile(r"(\d.){19}")
value = "3 9 7 8 8 7 6 8 4 "



#value = input()
search = re.search(PHONE_REGEX, value)

print(search)
if search:
    print ("Строка соответствует регулярному выражению")
else:
    print ("Строка не соответствует регулярному выражению")
