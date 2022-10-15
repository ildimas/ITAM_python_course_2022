def greetings(stroke):
    stroke = stroke.split()
    return f"Доброго времени суток, {stroke[0]} {stroke[1]}"
name_and_surname = input()
print(greetings(name_and_surname))
#