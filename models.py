from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Group(db.Model):
    name = db.StringProperty(required=True)
    info = db.TextProperty()

class File(db.Model):
    file = db.BlobProperty(required=True)
    info = db.StringProperty()
    owner = db.ReferenceProperty(required=True)

class User(polymodel.PolyModel):
    user = db.UserProperty(required=True)
    name = db.StringProperty(required=True)
    surname = db.StringProperty(required=True)
    birthdate = db.DateProperty()
    isHeadman = db.BooleanProperty()
    photo = db.ReferenceProperty(File)
    info = db.TextProperty()
    icq = db.StringProperty()
    skype = db.StringProperty()
    vk = db.StringProperty()
    facebook = db.StringProperty()
    
class Student(User):
    group = db.ReferenceProperty(Group,required=True)
    
class Employee(User):
    position = db.StringProperty(required=True)

class UserMessage(db.Model):
    from_user = db.ReferenceProperty(User, collection_name='from_user')
    to_user = db.ReferenceProperty(User, collection_name='to_user')
    text = db.TextProperty()
    date_time = db.DateProperty(required=True)

class Topic(db.Model):
    author = db.ReferenceProperty(User,required=True)
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)

class TopicMessage(db.Model):
    user = db.ReferenceProperty(User,collection_name='author',required=True)
    topic = db.ReferenceProperty(Topic,collection_name='topic',required=True)
    text = db.TextProperty(required=True)
    date = db.DateProperty(required=True)
    
class News(db.Model):
    user = db.ReferenceProperty(required=True)
    text = db.TextProperty(required=True)
    date = db.DateProperty(required=True)