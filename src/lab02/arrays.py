def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if  len(nums)==0:
        raise ValueError
    else:
        return min(nums), max(nums)
#print(f"min_max\n[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}\n[42] -> {min_max([42])}\n[-5, -2, -9] -> {min_max([-5, -2, -9])}\n[1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}\n")
#print(f"[] -> {min_max([])}")


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(f"unique_sorted\n[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}\n[] -> {unique_sorted([])}\n[-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}\n[1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}")


def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for object in mat:
        for item in object:
            if type(item) is not int or not float:
                return TypeError
        else:
            for item in object:
                result.append(item)
    return result
print(f"flatten\n[[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}\n[[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}\n[[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}\n[[[1, 2], 'ab']] -> {flatten([[[1, 2], 'ab']])}")
