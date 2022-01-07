def two_oldest_ages(ages):
    arr = sorted(ages,reverse=True)
    return [arr[1],arr[0]]

print(two_oldest_ages([1, 5, 87, 45, 8, 8]))