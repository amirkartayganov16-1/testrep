def get_list() -> list:
    return list(range(0, 1_000_000, 2))


class Solution:
    def find_target(self, list, target):
        left = 0
        right = len(list)
        f = 0
        while left < right:
            f += 1
            mid = (left + right) // 2
            if list[mid] == target:
                return f, target
            elif list[mid] < target:
                left = mid + 1
            elif list[mid] > target:
                right = mid - 1
        return f, target


print(Solution().find_target(get_list(), 888_888))
