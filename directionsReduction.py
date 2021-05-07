def opposite(direction):
    if(direction == "NORTH"):
        return "SOUTH"
    elif (direction == "SOUTH"):
        return "NORTH"
    elif (direction == "EAST"):
        return "WEST"
    elif(direction == "WEST"):
        return "EAST"
    else:
        return "Wrong Direction!!"


def dirReduc(arr):
    temp = list(arr.copy())
    for i in range(0, len(arr) - 2, 2):
        if(arr[i] == opposite(arr[i + 1])):
            temp.remove(arr[i])
            temp.remove(arr[i + 1])
    return temp





    

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(a))
print(dirReduc(u))