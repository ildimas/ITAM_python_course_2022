def sumilation(start, end):
    if start > end:
        new_start = end
        end = start
    else:
        new_start = start
    return sum([int(i) for i in range(new_start, end+1)])
start = int(input())
end = int(input())
print(sumilation(start, end))
