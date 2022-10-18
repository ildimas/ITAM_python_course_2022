l = list(map(int, input().split()))
ad_l = (l[0:len(l)-1])[::-1]
ad_l.append(l[-1])
ad_l = ad_l[::-1]
new_str = f"{ad_l[0]}"
for i in range(1, len(ad_l)):
    new_str = new_str + " " + f"{ad_l[i]}"
print(new_str)