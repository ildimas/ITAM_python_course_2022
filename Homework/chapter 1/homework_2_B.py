num_of_members = int(input())
adv_counter = [0, 0, 0]
for i in range(num_of_members):
    l = input().split()
    if (("False" in l) and ("True" in l)) or l.count("True") > 1 or l.count("False") > 1:
        if l[-1] == "True":
            adv_counter[0] += 1
        elif l[-1] == "False":
            adv_counter[1] += 1
        else:
            adv_counter[2] += 1
    elif l.count("True") + l.count("False") == 1:
        if "True" in l:
            adv_counter[0] += 1
        elif "False" in l:
            adv_counter[1] += 1
    print(adv_counter[0], adv_counter[1], adv_counter[2])