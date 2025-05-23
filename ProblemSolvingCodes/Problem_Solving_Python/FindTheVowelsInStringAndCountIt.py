def find_the_vowels_in_string_and_count_it(string):
    str1 = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    a=e=i=o=u=0
    remove_vowels = []
    for j in str1:
        if j == vowels[0]:
            a+=1
        elif j == vowels[1]:
            e+=1
        elif j == vowels[2]:
            i+=1
        elif j == vowels[3]:
            o+=1
        elif j == vowels[4]:
            u+=1
    print("a:", a)
    print("e:", e)
    print("i:", i)
    print("o:", o)
    print("u:", u)
    for k in str1:
        if k not in vowels:
            remove_vowels.append(k)
        elif k == " ":
            remove_vowels.append(k)
    print("String after removing vowels:", "".join(remove_vowels))


if __name__ == "__main__":
    try:
        string = input("Enter the string: ")
        if not string.strip():
            raise ValueError("Input cannot be an empty or whitespace-only string.")
        if all(c.isalpha() or c.isspace() or not c.isalnum() for c in string):
            find_the_vowels_in_string_and_count_it(string)
        else:
            raise ValueError("Invalid input!! Please pass only alphabetic characters.")
    except ValueError as e:
        print(e)