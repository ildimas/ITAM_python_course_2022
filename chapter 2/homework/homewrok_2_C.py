def converter(value, base):
    alphabet = "0123456789"
    for i in range(65,91):
        alphabet += chr(i)
    b = alphabet[value % base]
    while value >= base:
        value = value // base
        b += alphabet[value % base]
    return b[::-1]
print(converter(35, 362))