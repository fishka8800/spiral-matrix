from matrix.exceptions import MatrixFormatError


def parse_matrix(text: str) -> list[list[int]]:
    """Преобразует текст в квадратную матрицу"""
    matrix = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or "|" not in line:
            continue

        items = line.split("|")

        if items[0].strip() == "":
            items = items[1:]
        if items and items[-1].strip() == "":
            items = items[:-1]

        if not items:
            raise MatrixFormatError(f"Строка {line_number}: строка матрицы не содержит значений")

        numbers = []

        for column_number, item in enumerate(items, start=1):
            item = item.strip()
            if not item:
                raise MatrixFormatError(f"Строка {line_number}, столбец {column_number}: пустое значение")
            if not item.isdecimal():
                raise MatrixFormatError(
                    "Строка {line_number}, столбец {column_number}: "
                    f"некорректное значение '{item}'"
                )

            numbers.append(int(item))

        matrix.append(numbers)

    if not matrix:
        raise MatrixFormatError("Матрица пустая")

    size = len(matrix)

    for row in matrix:
        if len(row) != size:
            raise MatrixFormatError("Матрица должна быть квадратной")

    return matrix


def spiral_traversal(matrix: list[list[int]]) -> list[int]:
    """Обходит матрицу против часовой стрелки"""

    if not matrix:
        return []

    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for row in range(top, bottom + 1):
            result.append(matrix[row][left])
        left += 1
        for column in range(left, right + 1):
            result.append(matrix[bottom][column])
        bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][right])
            right -= 1
        if top <= bottom:
            for column in range(right, left - 1, -1):
                result.append(matrix[top][column])
            top += 1

    return result
