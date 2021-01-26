from mongoengine import *

connect("exercise2", host="192.168.1.200")


class People(Document):
    first_name = StringField()
    last_name = StringField()
    email = StringField()


my_person = People(
    first_name="Kent",
    last_name="Thureson",
    email="kth@gmail.com"
)

my_person.save()
