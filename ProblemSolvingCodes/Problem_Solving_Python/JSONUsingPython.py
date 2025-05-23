import json
person = {}
person["Details of Person 1"] = {
    "Name":"Prasanth",
    "Age":"24",
    "Phone_num":"7871032790"
}
person["Details of person 2"] = {
    "Name":"Deepak",
    "Age":"17",
    "Phone_num":None
}
print(person)
a = json.dumps(person)
print(a)