def camel_to_snake_case(sentence):
    result = sentence[0]  # Start with the first character
    for char in sentence[1:]:
        if char.isupper():
            result += '_'  # Add underscore before uppercase letters
        result += char
    return result


if __name__ == "__main__":
    try:
        sentence = input("Enter the string: ")
        if not sentence.strip():
            raise ValueError("Input cannot be an empty or whitespace-only string.")
        if all(c.isalpha() for c in sentence):
            out = camel_to_snake_case(sentence)
            print("Converting a camel case sentence to a snake case sentence:", out)
        else:
            raise ValueError("Invalid input!! Please pass only alphabetic characters.")
    except ValueError as e:
        print(e)