num_of_members = int(input())

main_list = []
och = 0
zaoch = 0

for i in range(num_of_members):
    main_list.append(input().split())

for j in range(len(main_list)):
    if (main_list[j])[-1] == "True":
        och += 1
    else:
        zaoch += 1
        
print(och, zaoch)