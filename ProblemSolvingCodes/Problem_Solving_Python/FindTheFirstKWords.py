def get_first_k_words(s, k):
    words = s.split()  # Split the string into words
    first_k_words = words[:k]  # Get the first k words
    print(" ".join(first_k_words))  # Join the first k words back into a string


if __name__ == "__main__":
    try:
        s = input("Enter the string: ")
        k = int(input("Enter the num: "))
        if not s.strip():
            raise ValueError("Input cannot be an empty or whitespace-only string.")
        if all(c.isalpha() or c.isspace() or not c.isalnum() for c in s):
            get_first_k_words(s, k)
        else:
            raise ValueError("Invalid input!! Please pass only alphabetic characters.")
    except ValueError as e:
        print(e)