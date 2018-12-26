import random


def selection_sort(l=None):
    l = l or []
    for i in range(0, len(l) - 1):
        (el, min_i) = min([(el, i) for i, el in enumerate(l[i:])])
        l[i], l[min_i + i] = l[min_i + i], l[i]
    return l


def selection_sort2(l=None):
    l = l or []

    for i in range(0, len(l) - 1):
        slice_ = l[i:]
        min_index, min_value = i, l[i]

        for index, value in enumerate(slice_):
            if value <= min_value:  # ?
                min_index, min_value = index + i, value
        l[i], l[min_index] = l[min_index], l[i]

    return l


# def insertionSort(alist):
#     for index in range(1, len(alist)):
#
#         currentvalue = alist[index]
#         position = index
#
#         while position > 0 and alist[position - 1] > currentvalue:
#             alist[position] = alist[position - 1]
#             position = position - 1
#
#         alist[position] = currentvalue
def insSort(lst=None):
    l = lst[:] or []

    for i in range(1, len(l)):
        curr = l[i]
        pos = i

        while pos > 0 and l[pos - 1] > curr:
            l[pos] = l[pos - 1]
            pos = pos - 1

        l[pos] = curr

    return l


def qsort(lst=None):
    l = lst[:] or []

    if len(lst) <= 1:
        return lst

    pivot = random.choice(lst)

    less = [x for x in lst if x < pivot]
    greater = [x for x in lst if x > pivot]
    equal = [x for x in lst if x == pivot]

    return qsort(less) + equal + qsort(greater)


def quicksort_r(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def quicksort_i(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


if __name__ == '__main__':
    list_origin = [50, 1, 15, 10, 12, ]
    testcase = [1, 10, 12, 15, 50]
    # for f in (selection_sort, selection_sort2):
    #     assert f(list_origin[:]) == testcase
    #     assert f([]) == []
    #     assert f([4]) == [4]

    # assert insSort([10, 5, 7, 1]) == [1, 5, 7, 10]
    assert qsort([10, 5, 7, 1]) == [1, 5, 7, 10]
