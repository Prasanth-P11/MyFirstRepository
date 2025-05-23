def reverse_a_sentence(string):
    char_list = string.split()
    left = 0
    right = len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    reversed_str = ' '.join(char_list)
    print("The reversed string is:", reversed_str)


if __name__ == "__main__":
    try:
        string = input("Enter the string: ")
        if not string.strip():
            raise ValueError("Input cannot be an empty or whitespace-only string.")
        if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
            reverse_a_sentence(string)
        else:
            raise ValueError("Invalid input!! Please pass only alphabetic characters.")
    except ValueError as e:
        print(e)