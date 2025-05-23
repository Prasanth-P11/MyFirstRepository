import inflect

# Initialize the inflect engine
p = inflect.engine()

# Define the number
a = 897650  # You can change this to any number you'd like

# Convert number to words
output = p.number_to_words(a)

# Print the output
print(output)
