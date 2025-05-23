# Two-Pointer Technique
def reverse_list(a):
    left = 0
    right = len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a


if __name__ == "__main__":
    a = [1, 8, 2, 6]
    out = reverse_list(a)
    print("The reversed list is:", out)


def reverse_str(a):
    char_list = list(a)
    left = 0
    right = len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    reversed_str = ''.join(char_list)
    print("The reversed string is:", reversed_str)


if __name__ == "__main__":
    a = "hellow"
    reverse_str(a)
