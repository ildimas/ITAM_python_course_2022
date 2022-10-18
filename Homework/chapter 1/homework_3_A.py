def clear_conflict():
    for i in range(len(sorting_list)-1):
        for j in range(i+1, len(sorting_list)):
            if (sorting_list[i])[1] == (sorting_list[j])[1]:
                if (sorting_list[i])[2] > (sorting_list[j])[2]:
                    (sorting_list[j])[1] += 1
                elif (sorting_list[i])[2] < (sorting_list[j])[2]:
                    (sorting_list[i])[1] += 1
                elif (sorting_list[i])[2] == (sorting_list[j])[2]:
                    if (sorting_list[i])[3] < (sorting_list[j])[3]:
                        (sorting_list[j])[1] += 1
                    elif (sorting_list[i])[3] > (sorting_list[j])[3]:
                        (sorting_list[i])[1] += 1
                    else:
                        (sorting_list[j])[1] = 1
num_of_members = int(input())
list_of_tasks = [int(i) for i in range(1, num_of_members+1)]
main_list = []

for i in range(num_of_members):
    main_list.append(input().split())

alphabet_main_list = main_list[:]
alphabet_main_list.sort()

#! определение места в списке

alphabet_placement_list = []
for a in main_list:
    alphabet_placement_list.append(alphabet_main_list.index(a))

#! первоначальная отборка
sorting_list = []
for i in range(len(main_list)):
    if int((main_list[i])[2]) < int((main_list[i])[3]):
        task = round((int((main_list[i])[2]) + int((main_list[i])[3])) / 2)
    elif int((main_list[i])[2]) > int((main_list[i])[3]):
        task = int((main_list[i])[2])
    elif int((main_list[i])[2]) == int((main_list[i])[3]):
        task = 1
    rate = int((main_list[i])[-1])
    sorting_list.append([i, task, rate, alphabet_placement_list[i]])

#! перераспределение на основе рейтинга и алфавита 
flag = 0
while flag != 1:
    cap = set()
    clear_conflict()
    for o in range(len(sorting_list)):
        cap.add((sorting_list[o])[1])
    if len(cap) == num_of_members:
        flag = 1

new_str = f"{(sorting_list[0])[1]}"
for a in range(1, len(sorting_list)):
    new_str = new_str + " " + f"{(sorting_list[a])[1]}"
print(new_str)


        


    


