def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if len(first_string) != len(second_string):
        return (None, None, False)

    sorted_first = merge_sort(list(first_string))
    sorted_second = merge_sort(list(second_string))

    return (
        "".join(sorted_first),
        "".join(sorted_second),
        sorted_first == sorted_second,
    )
