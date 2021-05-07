def sum_of_intervals(intervals):
    liste = []
    for x in range(len(intervals)):
        for y in range(intervals[x][0], intervals[x][1]):
            liste.append([intervals[x][y]])
    return set(liste)

print(sum_of_intervals([(1, 5)]))