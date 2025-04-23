"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

# def find_first_sum(nums: list, goal: int) -> list:
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == goal:
#                 return [i, j]


def find_first_sum(nums: list, goal: int) -> list:
    seen = {}  # diccionario para guardar el nro y su indice
    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]
        seen[value] = index
    return None


print(find_first_sum([1, 2, 3, 4, 5], 4))
