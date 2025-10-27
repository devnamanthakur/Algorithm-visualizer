def binary_search(arr, target, visualize_step=None):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if visualize_step:
            visualize_step(arr, left, right, mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1