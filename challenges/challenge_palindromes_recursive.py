def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif word[low_index] == word[high_index]:
        word = word[1:-1]
        if len(word) <= 1:
            return True
        # print(word, len(word), "ÖIA AQUI")
        return is_palindrome_recursive(word, 0, len(word) - 1)
    else:
        return False
