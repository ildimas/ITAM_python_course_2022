def stairs(blocks):
    lvl = 0
    step = 1
    while blocks != 0:
        blocks -= step
        lvl += 1
        step += 1
    return lvl

blocks = int(input())
print(stairs(blocks))
        
        