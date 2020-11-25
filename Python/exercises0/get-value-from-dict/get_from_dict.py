def get_age_from_person(person):
    return person["age"]


my_person = {
    "name": "Sarah",
    "age": 29
}

age = get_age_from_person(my_person)

print(age)
# The correct answer here should be `29`
