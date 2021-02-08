from mongoengine import *

# connect('tumblelog', host='w530kt')
db = connect('calendar', host='w530kt')



class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


def add_initial_data():
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
    john = User(email='john@example.com', first_name='John', last_name='Leylaw').save()

    post1 = TextPost(title='Fun with MongoEngine', author=john)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save()

# add_initial_data()


'''
for post in Post.objects:
    print(1, post.title)

for post in TextPost.objects:
    print(2, post.content)

for post in Post.objects:
    print(3, post.title)
    print(3, '=' * len(post.title))

    if isinstance(post, TextPost):
        print(4, post.content)

    if isinstance(post, LinkPost):
        print(5, 'Link: {}'.format(post.link_url))

for post in Post.objects(tags='mongodb'):
    print(6, post.title)

num_posts = Post.objects(tags='mongodb').count()
print('Found {} posts with tag "mongodb"'.format(num_posts))
'''

class Page(QueryFieldList):
    meta = {'collection': 'calendar'}


print(dir(Page.mro()))