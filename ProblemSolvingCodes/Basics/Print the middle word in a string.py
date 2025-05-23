def print_mid_word(str):
    length = len(str)
    mid = length // 2
    if length % 2 == 0:
        return str[mid-1:mid+1]
    else:
        return str[mid]

if __name__ == "__main__":
    str = input("Enter the string:")
    out=print_mid_word(str)
    print(out)