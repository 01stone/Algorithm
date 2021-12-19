def solution(arr):
    return [num for i, num in enumerate(arr) if arr[i] != arr[i-1] or i == 0]