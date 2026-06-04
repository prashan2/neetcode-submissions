from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    #print(f'r:{r} c:{c}')
    for row_cnt,row in enumerate(grid):
        for col_cnt, col in enumerate(row):
            if col_cnt > c:
                #print(f'col_cnt:{col_cnt} ')
                return False
        if row_cnt > r:
            #print(f'row_cnt:{row_cnt} ')
            return False
    return True

# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
