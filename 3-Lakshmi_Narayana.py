def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -99999  # 99999 used to represent infinity value
    _sum = 0
    for i in range(mid, low - 1, -1):
        _sum = _sum + A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i
    right_sum = -99999
    _sum = 0
    for j in range(mid, high):
        _sum = _sum + A[j]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j
    return max_left, max_right, left_sum + right_sum - A[mid]


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


A = [2, -1, 4, -5, 4, 3]


maximum_sum = find_maximum_subarray(A, 0, A.__len__() - 1)

print(maximum_sum)
