stroke = input()
first_letter = 0; second_letter = 0; i = 0; dot = stroke.find(".")
while first_letter == 0 or second_letter == 0:
    if stroke[i].isupper() == True and first_letter == 0:
        first_letter = i
    if stroke[i].isdigit() == True and second_letter == 0:
        second_letter = i+1
    i += 1

step = second_letter - first_letter

fin_stroke = ""
for a in range(first_letter, dot+1, step):
    fin_stroke += stroke[a]
print(fin_stroke)