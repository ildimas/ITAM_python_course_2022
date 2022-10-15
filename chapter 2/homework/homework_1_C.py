def eraser(numerical):
    if numerical < 0:
        numerical *= -2
    return numerical
def del_max(numerical, l):
    return numerical / max(l)

def sumilation(str_of_nums):
    l = list(map(int, str_of_nums.split()))
    l = list(map(lambda x: eraser(x), l))
    l = list(map(lambda x: del_max(x, l), l))
    return sum(l)

x = input()
print(sumilation(x))