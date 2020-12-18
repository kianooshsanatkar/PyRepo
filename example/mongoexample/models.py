from mongoengine import Document, UUIDField, StringField, EmailField, BinaryField


class User(Document):
    """
    docstring
    """
    uid = UUIDField(primary_key=True)
    username = StringField(unique=True, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    Phone = StringField()
