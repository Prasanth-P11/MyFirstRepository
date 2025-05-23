# Given dictionary
# dict_user = {1: 2, 3: 4, 5: [6, 7, 8], 9: 10}

def convert_dict_to_list(user_dict):
    # Initialize an empty list
    result = []

    # Iterate over the dictionary items
    for key, value in user_dict.items():
        if isinstance(key, tuple):
            result.extend(key)
        else:
            result.append(key)
        if isinstance(value, list):  # If the value is a list, extend the list
            result.extend(value)
        elif isinstance(value, dict):
            result.extend(convert_dict_to_list(value))
        elif isinstance(value, set):
            result.extend(list(value))
        else:
            result.append(value)  # If not a list, just add the value
    return result


if __name__ == "__main__":
    '''# Initialize an empty dictionary
    user_dict = {}
    # Get the number of entries from the user
    num_entries = int(input("Enter the number of entries: "))
    # Loop to get each key and list value pair
    for _ in range(num_entries):
        key = int(input("Enter key: "))
        # Get the list elements from the user
        list_input = int(input("Enter values: "))
        # Split the input string by commas and convert to a list
        user_dict[key] = list_input
    print("User input dict:", user_dict)
    convert_dict_to_list(user_dict)'''
    user_dict = {(1, 2, 3): 1, "Hi": [4, 5, 6], 7: {8, 9, 10}, 11: {(9, 3, 6): 13, 14: 15}}
    output = convert_dict_to_list(user_dict)
    print(output)