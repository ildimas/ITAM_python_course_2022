length = int(input())
l = list(map(int, input().split()))
new_str = f"{l[0]}"
for j in range(2, len(l), 2):
    new_str = new_str + " " + str(l[j])
print(new_str)