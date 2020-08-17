import re
PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")
value = "+380631312876"
value = input()
search = re.search(PHONE_REGEX, value)
country, operator, phone = search.group(1, 2, 3)

#print(search)
print("Код страны: "+country)
print("Код оператора: "+operator)
print("Номер телефона: "+ phone)
