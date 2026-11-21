# https://www.codewars.com/kata/5717fbf85122b8f757001b3f/solutions/python
def rotate_corners(matrix):
    corners = get_ordered_corners(matrix)
    non_corners = get_non_corners(matrix)

    num_rotations = sum(value(corner) for corner in corners) * sum(value(non_corner) for non_corner in non_corners)
    rotated_corners = rotate(corners, num_rotations)
    return format_output(rotated_corners)


def value(elem):
    match elem:
        case str():
            return ascii_value(elem)
        case bool():
            return 1 if elem else 0
        case int():
            return elem
        case default:
            print(elem, type(elem))
            return 0

def ascii_value(elem):
    return ord(elem)

def get_ordered_corners(matrix):
    return [matrix[0][0], matrix[0][-1], matrix[-1][-1], matrix[-1][0]]

def get_non_corners(matrix):
    H, W = len(matrix), len(matrix[0])
    return [matrix[i][j] for i in range(H) for j in range(W) if not ((i in {0, H-1}) and (j in {0, W-1}))]

def rotate(corners, n):
    return [corners[(i-n) % 4] for i in range(4)]

def format_output(corners):
    return [[corners[0], corners[1]], [corners[3], corners[2]]]
