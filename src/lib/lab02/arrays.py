def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        return ValueError
    else:
        return min(nums), max(nums)
