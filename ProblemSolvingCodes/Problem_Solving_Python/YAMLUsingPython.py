import yaml

# Define data as a Python dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'occupation': 'Software Developer',
    'skills': ['Python', 'JavaScript', 'YAML'],
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'NY',
        'zip': '12345'
    }
}

# Define the path to save the YAML file
yaml_file_path = 'person.yaml'

# Write the YAML data to a file
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(data, yaml_file, sort_keys=False)
