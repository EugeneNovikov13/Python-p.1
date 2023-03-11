# nums_1 = [5, 2, 1, 8, 4, 2, 0, 9, 6, 7, 3]
# nums_2 = [5, 2, 1, 8, 4, 2, 0, 9, 6, 7, 3]
# nums_3 = [5, 2, 1, 8, 4, 2, 0, 9, 6, 7, 3]
#
#
# #пузырьковый метод сортировки
# def bubble_sort_1(_nums):
#     for i in range(len(_nums)):
#         for j in range(len(_nums) - 1):
#             if _nums[j] > _nums[j+1]:
#                 _nums[j], _nums[j+1] = _nums[j+1], _nums[j]
# #
# #
# # bubble_sort_1(nums_1)
# # print(nums_1)
#
#
# # улучшенный пузырьковый метод сортировки
# def bubble_sort_2(_nums):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(_nums) - 1):
#             if _nums[i] > _nums[i+1]:
#                 _nums[i], _nums[i+1] = _nums[i+1], _nums[i]
#                 swapped = True
# #
# #
# # bubble_sort_2(nums_2)
# # print(nums_2)
#
#
# # еще более быстрый пузырьковый метод сортировки
# def bubble_sort_3(_nums):
#     has_swapped = True
#     num_of_iteration = 0
#     while has_swapped:
#         has_swapped = False
#         for i in range(len(_nums) - num_of_iteration - 1):
#             if _nums[i] > _nums[i+1]:
#                 _nums[i], _nums[i + 1] = _nums[i + 1], _nums[i]
#                 has_swapped = True
#         num_of_iteration += 1
#
#
# # bubble_sort_3(nums_3)
# # print(nums_3)
#
#
# if __name__ == '__main__':
#     import timeit
#
#     print(timeit.timeit('bubble_sort_1(nums_1)', globals=globals()))
#     print(timeit.timeit('bubble_sort_2(nums_2)', globals=globals()))
#     print(timeit.timeit('bubble_sort_3(nums_3)', globals=globals()))


# алгоритм сортировки слиянием
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])
#
#     return merge(left_list, right_list)
#
#
# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_nums = merge_sort(random_list_of_nums)
# print(random_list_of_nums)


# алгоритм выборки
# def selection_sort(nums):
#     for i in range(len(nums)):
#         min_ind = i
#         for j in range(i+1, len(nums)):
#             if nums[j] < nums[min_ind]:
#                 min_ind = j
#         nums[i], nums[min_ind] = nums[min_ind], nums[i]
#
#
# random_list_of_nums = [120, 45, 68, 250, 176]
# selection_sort(random_list_of_nums)
# print(random_list_of_nums)


# алгоритм сортировки кучи
# from heapq import heappop, heappush
#
#
# def heap_sort(array):
#     heap = []
#     for elem in array:
#         heappush(heap, elem)
#
#     ordered = []
#
#     while heap:
#         ordered.append(heappop(heap))
#
#     return ordered
#
#
# arr = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
# print(heap_sort(arr))

# алгоритм Шелла


# быстрая сортировка


# функции сортировки
arr = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
# arr.sort()
# print(arr)

sorted_arr = sorted(arr)
print(sorted_arr)
