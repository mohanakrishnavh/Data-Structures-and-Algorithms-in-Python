import sys


def hour_glass_sum(arr):
    rows = cols = len(arr) - 1
    max_sum = -sys.maxsize

    for i in range(rows - 1):
        for j in range(cols - 1):
            current_hour_glass_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                j + 1] + arr[i + 2][j + 2]

            if current_hour_glass_sum > max_sum:
                max_sum = current_hour_glass_sum
    return max_sum
