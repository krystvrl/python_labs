def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if not mat:
        return []
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        raise ValueError("Рваная матрица")
    return [[mat[i][j] for i in range(len(mat))] for j in range(row_len)]


print(
    f"transpose\n[[1, 2, 3]] -> {transpose([[1, 2, 3]])}\n[[1], [2], [3]] -> {transpose([[1], [2], [3]])}\n[[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}\n[] -> {transpose([])}"
)
# print(f"[[1, 2], [3]] -> {transpose([[1, 2], [3]])}")


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]


print(
    f"row_sums\n[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}\n[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}\n[[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}"
)
# print(f"[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}")


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        raise ValueError("Рваная матрица")
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(row_len)]


print(
    f"col_sums\n[[1, 2, 3], [4, 5, 6]] -> {col_sums([[1, 2, 3], [4, 5, 6]])}\n[[-1, 1], [10, -10]] -> {col_sums([[-1, 1], [10, -10]])}\n[[0, 0], [0, 0]] -> {col_sums([[0, 0], [0, 0]])}"
)
print(f"[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}")
