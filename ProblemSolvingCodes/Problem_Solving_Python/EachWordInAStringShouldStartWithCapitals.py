def camel_to_snake_case(sentence):
    words = sentence.split()  # Split the sentence into words
    capitalized_words = []

    for word in words:
        # Capitalize the first letter and keep the rest of the word unchanged
        capitalized_word = word[0].upper() + word[1:].lower()
        capitalized_words.append(capitalized_word)

    # Join the words back into a single sentence
    return ' '.join(capitalized_words)


if __name__ == "__main__":
    try:
        sentence = input("Enter the string: ")
        if not sentence.strip():
            raise ValueError("Input cannot be an empty or whitespace-only string.")
        if all(c.isalpha() or c.isspace() for c in sentence):
            out = camel_to_snake_case(sentence)
            print("Converting a camel case sentence to a snake case sentence:", out)
        else:
            raise ValueError("Invalid input!! Please pass only alphabetic characters.")
    except ValueError as e:
        print(e)