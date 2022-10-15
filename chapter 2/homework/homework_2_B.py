def key_difference(dict1, dict2):
    result_dict = {}
    x1 = list(dict1.items())
    y2 = list(dict2.items())
    for i in range(max(len(x1), len(y2))):
        try:
            if x1[i] == y2[i]:
                result_dict.update({(x1[i])[0]: "equal"})
            elif ((x1[i])[0] == (y2[i])[0]) and ((x1[i])[1] != (y2[i])[1]):
                 result_dict.update({(x1[i])[0]: "changed"})
        except IndexError:
            if len(x1) > len(y2):
                result_dict.update({(x1[i])[0]: "deleted"})
            elif len(x1) < len(y2):
                result_dict.update({(y2[i])[0]: "added"})


    return result_dict
 

dict1 = {"a":"b", "b":"a"}
dict2 = {"a":"b", "b":"a", "c":"d"}

print(key_difference(dict1, dict2))