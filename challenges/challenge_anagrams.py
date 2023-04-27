def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Dividir para conquistar
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    # ordena a palavra
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

    sorted_first = merge_sort(first_string)
    sorted_second = merge_sort(second_string)

    if len(first_string) == 0 or len(second_string) == 0:
        return ("".join(sorted_first), "".join(sorted_second), False)

    return (
        "".join(sorted_first),
        "".join(sorted_second),
        "".join(sorted_first) == "".join(sorted_second),
    )
