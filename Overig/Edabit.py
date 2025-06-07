def evenly_divisible(x, y, z):
    return [i for i in range(x,y+1) if i % z == 0]

evenly_divisible(1, 10, 0)