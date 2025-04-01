def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)

if __name__ == "__main__":
    arr = [1, 3, 4, 5, 6, 7]
    for i in range(10):
        print(binary_search(arr, i, 0, len(arr) - 1), end=' ')
