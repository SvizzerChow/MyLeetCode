from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        result = []
        self._heapSort(arr, len(arr))
        for i in range(k):
            result.append(arr[0])
            arr[0] = arr[len(arr) - i - 1]
            self._re(arr, len(arr) - i - 1, len(arr) - i - 1)
        return result

    def _heapSort(self, arr, length):
        h = 0
        m = length
        while m > 1:
            m = m // 2
            h += 1
        while h > 0:
            left = 2 ** h
            max = 2 ** (h + 1)
            root = 2 ** (h - 1)
            while left < max and left <= length:
                right = left + 1
                if (left <= length and right <= length and arr[left - 1] < arr[right - 1]) or (left <= length < right):
                    if arr[left - 1] < arr[root - 1]:
                        temp = arr[root - 1]
                        arr[root - 1] = arr[left - 1]
                        arr[left - 1] = temp
                elif right <= length and arr[right - 1] < arr[root - 1]:
                    temp = arr[root - 1]
                    arr[root - 1] = arr[right - 1]
                    arr[right - 1] = temp
                left += 2
                root += 1
            h -= 1
        return arr

    def _judge(self, arr, node, length):








arr = [0,1,1,2,4,4,1,3,3,2]
print(Solution().getLeastNumbers(arr, 6))



